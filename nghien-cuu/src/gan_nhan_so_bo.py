"""Gán nhãn sơ bộ 3 lớp cho bộ SMS tiếng Việt trên Hugging Face.

Bộ gốc (tran-2026-vi-sms-dataset, CC BY 4.0) chỉ có 2 nhãn: 0 = hợp lệ, 1 = rác/lừa đảo.
Script này KHÔNG quyết định nhãn cuối. Nó chỉ:
  1. Tải bộ dữ liệu về, cố định đúng một phiên bản để người khác chạy lại ra cùng kết quả.
  2. Bỏ tin trùng nguyên văn (bộ gốc có 362 dòng trùng).
  3. Quét thêm một lượt số điện thoại, số dài còn sót.
  4. Gợi ý nhãn LUA_DAO / QUANG_CAO / BINH_THUONG theo quy tắc đơn giản, ghi lý do.
  5. Đánh dấu tin cần người duyệt (cột can_xem = 1) và chọn đợt 1 gồm 200 tin mỗi nhãn (cột dot = 1)
     để duyệt trước ngày nộp.
  6. Tạo mẫu 100 tin không kèm nhãn để người thứ hai gán độc lập, dùng tính Cohen's kappa.

Người duyệt mở file gan-nhan-so-bo.csv bằng Excel, lọc dot = 1, điền cột nhan_chot cho từng tin.
Không sửa cột khác.

Chạy từ thư mục gốc repo:
    python nghien-cuu/src/gan_nhan_so_bo.py
Chỉ dùng thư viện có sẵn của Python, không cần cài thêm.
"""

import csv
import random
import re
import urllib.request
from collections import Counter
from pathlib import Path

# Phiên bản bộ dữ liệu: commit trên Hugging Face, kiểm tra ngày 06/11/2026.
REPO = "trannguyenthaituan/vietnamese_sms_dataset"
REVISION = "a90e2bd7e8df2376939658075ba8094dcee488ad"
URL = f"https://huggingface.co/datasets/{REPO}/resolve/{REVISION}/full_dataset.csv"

SEED = 42  # cố định để lần chạy nào cũng chọn cùng một mẫu

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "nghien-cuu" / "du-lieu" / "processed" / "tran-2026"
GOC = OUT_DIR / "full_dataset.csv"
SO_BO = OUT_DIR / "gan-nhan-so-bo.csv"
MAU_KAPPA = OUT_DIR / "mau-kappa-100.csv"

# ---------------------------------------------------------------------------
# Quy tắc gợi ý. Mỗi quy tắc là một biểu thức chính quy (regex) tìm trong tin.
# re.I: không phân biệt chữ hoa, chữ thường.
# Có cả dạng có dấu và không dấu vì khoảng một nửa số tin viết không dấu.
# ---------------------------------------------------------------------------
THE_QC = re.compile(r"\[QC\]|\(QC\)|^\s*QC\b", re.I)
TU_QUANG_CAO = re.compile(
    r"khuyến mãi|khuyen mai|ưu đãi|uu dai|giảm giá|giam gia|voucher|\bsale\b|"
    r"soạn \w+ gửi|soan \w+ gui|\bDK\b|đăng ký gói|dang ky goi|miễn phí|mien phi|"
    r"từ chối nhận|tu choi nhan|\bTC\b",
    re.I,
)
THONG_BAO_THAT = re.compile(
    r"\bOTP\b|mã xác thực|ma xac thuc|mã xác nhận|ma xac nhan|biến động số dư|"
    r"bien dong so du|số dư|so du|không chia sẻ|khong chia se",
    re.I,
)
# Thông báo về gói cước của chính thuê bao (đăng ký thành công, gia hạn lỗi...):
# là thông báo dịch vụ, không phải quảng cáo, dù có chữ "đăng ký", "miễn phí".
THONG_BAO_GOI = re.compile(
    r"thành công|thanh cong|gia hạn|gia han|đã hết|da het|sai cú pháp|sai cu phap|"
    r"không đủ|khong du|đã được|da duoc",
    re.I,
)
# Dấu hiệu nghi lừa đảo xuất hiện trong tin đang được gắn nhãn "hợp lệ":
# những tin này cần người xem lại, có thể bộ gốc gán sai.
NGHI_LUA_DAO = re.compile(
    r"bị khóa|bi khoa|xác minh|xac minh|cập nhật thông tin|cap nhat thong tin|"
    r"trúng thưởng|trung thuong|việc nhẹ|viec nhe|bit\.ly|zalo\.me|\.xyz|\.top|\.vip",
    re.I,
)

# Chủ đề của tin nhãn 1, để người duyệt dễ lọc trong Excel và để phân tích lỗi sau này.
CHU_DE = [
    ("co_bac", r"nhà cái|nha cai|cá cược|ca cuoc|casino|nổ hũ|no hu|tài xỉu|tai xiu|w88|qh88|\bslot|nạp đầu|nap dau"),
    ("viec_lam", r"việc nhẹ|viec nhe|làm nhiệm vụ|lam nhiem vu|cộng tác viên|cong tac vien|tuyển|tuyen"),
    ("gia_ngan_hang", r"vcb|vietcombank|techcombank|bidv|agribank|vietinbank|mb bank|ngân hàng|ngan hang|tài khoản|tai khoan"),
    ("vay_no", r"vay|khoản nợ|khoan no|bể nợ|be no|khởi kiện|khoi kien"),
    ("dau_tu", r"đầu tư|dau tu|sinh lời|sinh loi|lãi suất|lai suat|hợp tác|hop tac"),
    ("qua_tang", r"quà|qua tang|tri ân|tri an|trúng|trung thuong|miễn phí|mien phi"),
    ("hen_ho", r"hẹn hò|hen ho|sugar|tìm bạn|tim ban"),
]
CHU_DE = [(ten, re.compile(p, re.I)) for ten, p in CHU_DE]

# Quét thêm thông tin cá nhân còn sót (bộ gốc đã thay phần lớn bằng thẻ [PHONE], [NUMBER]...).
SDT = re.compile(r"(?<!\d)(?:\+?84|0)\d{9,10}(?!\d)")
SO_DAI = re.compile(r"(?<!\d)\d{8,}(?!\d)")


def tai_du_lieu():
    """Tải file gốc nếu chưa có trong máy."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not GOC.exists():
        print(f"Đang tải {URL}")
        urllib.request.urlretrieve(URL, GOC)
    with open(GOC, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def an_danh_them(tin):
    """Thay số điện thoại và dãy số dài còn sót. Trả về (tin mới, số chỗ đã thay)."""
    tin, n1 = SDT.subn("[PHONE]", tin)
    tin, n2 = SO_DAI.subn("[NUMBER]", tin)
    return tin, n1 + n2


def goi_y(tin, nhan_goc):
    """Trả về (nhãn gợi ý, lý do, chủ đề, cần xem 1/0)."""
    chu_de = ",".join(ten for ten, p in CHU_DE if p.search(tin))

    if nhan_goc == "1":
        # Bộ gốc nói đây là rác hoặc lừa đảo. Mặc định gợi ý lừa đảo,
        # nhưng mọi tin nhãn 1 đều phải có người xem, vì đây là lớp quan trọng nhất.
        if THE_QC.search(tin):
            return "QUANG_CAO", "nhãn gốc 1 nhưng có thẻ QC", chu_de, 1
        if "co_bac" in chu_de or "hen_ho" in chu_de:
            return "LUA_DAO", "nhãn gốc 1, cờ bạc/hẹn hò: LUA_DAO theo quy tắc 4, 5", chu_de, 1
        return "LUA_DAO", "nhãn gốc 1", chu_de, 1

    # nhan_goc == "0": bộ gốc nói hợp lệ. Tách thành quảng cáo và bình thường.
    if NGHI_LUA_DAO.search(tin):
        return "BINH_THUONG", "nhãn gốc 0 nhưng có dấu hiệu nghi lừa đảo", chu_de, 1
    if THE_QC.search(tin):
        return "QUANG_CAO", "có thẻ QC", chu_de, 0
    if THONG_BAO_GOI.search(tin):
        return "BINH_THUONG", "thông báo gói cước của thuê bao", chu_de, 1
    if TU_QUANG_CAO.search(tin):
        return "QUANG_CAO", "có từ khóa quảng cáo, không có thẻ QC", chu_de, 1
    if THONG_BAO_THAT.search(tin):
        return "BINH_THUONG", "thông báo OTP/số dư", chu_de, 0
    return "BINH_THUONG", "không có dấu hiệu quảng cáo", chu_de, 0


def main():
    rows = tai_du_lieu()

    # Bỏ tin trùng nguyên văn, giữ lần xuất hiện đầu tiên.
    da_thay, duy_nhat = set(), []
    for r in rows:
        khoa = r["message"].strip()
        if khoa and khoa not in da_thay:
            da_thay.add(khoa)
            duy_nhat.append(r)

    ket_qua, tong_thay = [], 0
    for r in duy_nhat:
        tin, n = an_danh_them(r["message"].strip())
        tong_thay += n
        nhan, ly_do, chu_de, can_xem = goi_y(tin, r["label"])
        ket_qua.append({
            "id": r["message_id"],
            "message": tin,
            "nhan_goc": r["label"],
            "nhan_goi_y": nhan,
            "ly_do": ly_do,
            "chu_de": chu_de,
            "can_xem": can_xem,
            "nhan_chot": "",
            "ghi_chu": "",
        })

    # Ngoài các tin đã đánh dấu, chọn ngẫu nhiên 10% tin còn lại để kiểm tra
    # xem quy tắc có sai nhiều không.
    rng = random.Random(SEED)
    con_lai = [k for k in ket_qua if k["can_xem"] == 0]
    for k in rng.sample(con_lai, len(con_lai) // 10):
        k["can_xem"] = 1
        k["ly_do"] += " (kiểm tra ngẫu nhiên 10%)"

    # Đợt 1 (thử nghiệm sơ bộ): chọn ngẫu nhiên tối đa 200 tin cho mỗi nhãn gợi ý.
    # Chỉ các tin đợt 1 được duyệt trước ngày nộp; phần còn lại duyệt khi làm thật đề tài.
    for k in ket_qua:
        k["dot"] = 2
    theo_nhan = {}
    for k in ket_qua:
        theo_nhan.setdefault(k["nhan_goi_y"], []).append(k)
    for nhan, ds in sorted(theo_nhan.items()):
        for k in rng.sample(ds, min(200, len(ds))):
            k["dot"] = 1

    # Đợt 1 xếp lên đầu, trong mỗi đợt tin cần xem đứng trước.
    ket_qua.sort(key=lambda k: (k["dot"], -k["can_xem"], k["nhan_goi_y"], k["chu_de"]))

    # utf-8-sig để Excel đọc đúng tiếng Việt.
    with open(SO_BO, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(ket_qua[0].keys()))
        w.writeheader()
        w.writerows(ket_qua)

    # Mẫu kappa: 100 tin lấy trong đợt 1, chia đều theo nhãn gợi ý, KHÔNG kèm nhãn,
    # để người gán thứ hai không bị ảnh hưởng. Sau đó so nhãn của họ với cột nhan_chot.
    dot1 = {}
    for k in ket_qua:
        if k["dot"] == 1:
            dot1.setdefault(k["nhan_goi_y"], []).append(k)
    mau = []
    for nhan, ds in sorted(dot1.items()):
        mau += rng.sample(ds, min(34, len(ds)))
    mau = mau[:100]
    rng.shuffle(mau)
    with open(MAU_KAPPA, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "message", "nhan"])
        w.writeheader()
        w.writerows({"id": k["id"], "message": k["message"], "nhan": ""} for k in mau)

    # Tóm tắt
    print(f"Số dòng gốc: {len(rows)}. Sau khi bỏ trùng: {len(ket_qua)}")
    print(f"Số chỗ thay thêm số điện thoại/số dài: {tong_thay}")
    print("Nhãn gợi ý:", dict(Counter(k["nhan_goi_y"] for k in ket_qua)))
    print("Nhãn gốc x gợi ý:", dict(Counter((k["nhan_goc"], k["nhan_goi_y"]) for k in ket_qua)))
    print(f"Đợt 1 (duyệt trước ngày nộp): {sum(k['dot'] == 1 for k in ket_qua)} tin,",
          dict(Counter(k["nhan_goi_y"] for k in ket_qua if k["dot"] == 1)))
    print(f"Tin cần người duyệt (cả 2 đợt): {sum(k['can_xem'] for k in ket_qua)}")
    print("Lý do cần xem:", dict(Counter(k["ly_do"] for k in ket_qua if k["can_xem"])))
    print(f"Đã ghi {SO_BO}")
    print(f"Đã ghi {MAU_KAPPA} ({len(mau)} tin)")


if __name__ == "__main__":
    main()
