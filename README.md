# Phát hiện tin nhắn và email lừa đảo tiếng Việt

Đồ án cuối kì môn Phương pháp nghiên cứu khoa học trong CNTT (841324), Trường Đại học Sài Gòn. Nhóm viết thuyết minh đề tài NCKH sinh viên theo mẫu 16 mục của trường, nộp dưới dạng `PPNCKH_MSSV1_MSSV2_MSSV3.pdf`, rồi trình bày trước lớp. Sau môn học, nhóm dự định thực hiện đề tài, nên repo có sẵn chỗ cho dữ liệu và mô hình.

## Cấu trúc

```
NCKH/
├── CLAUDE.md                     Ngữ cảnh và quy tắc cho Claude Code
├── README.md
├── .claude/
│   ├── settings.json             Quyền: chặn đọc dữ liệu thô, cho chạy pandoc
│   ├── skills/                   6 lệnh gọi bằng /ten-skill
│   └── agents/                   4 trợ lý chạy riêng
├── docs/
│   ├── yeu-cau/                  Đề, barem, mẫu thuyết minh, kiến thức slide
│   ├── ke-hoach/                 Lịch trình, phân công, câu hỏi cho thầy
│   └── bien-ban-hop/             Biên bản họp hằng tuần
├── thuyet-minh/                  Bản thảo, mỗi mục một file (00 đến 16, 99)
├── tong-quan/
│   ├── README.md                 Chiến lược tìm bài, nhật ký tìm kiếm
│   ├── ma-tran-tong-quan.md
│   ├── phieu-doc/                Một phiếu cho mỗi bài đã đọc
│   └── references.bib            Xuất từ Zotero
├── nghien-cuu/
│   ├── huong-dan-gan-nhan.md
│   └── du-lieu/                  raw/ (không lên git), processed/
├── trinh-bay/dan-y-slide.md
├── scripts/
│   ├── build.ps1                 Ghép thuyết minh thành .docx
│   └── cai-dat-claude.ps1        Cài skills, agents vào .claude/ (chạy một lần)
└── xuat-ban/                     File xuất, không lên git
```

## Bắt đầu

0. Lần đầu, nếu repo còn thư mục `_claude-setup/`: chạy `./scripts/cai-dat-claude.ps1` để chuyển skills, agents và `settings.json` vào `.claude/`, rồi commit `.claude/`.
1. Clone repo, cài [Zotero](https://www.zotero.org/) và [pandoc](https://pandoc.org/installing.html) (`winget install --id JohnMacFarlane.Pandoc`).
2. Đọc `docs/ke-hoach/lich-trinh.md` để biết tuần này làm gì, và `docs/ke-hoach/phan-cong.md` để biết mục nào của mình.
3. Mở Claude Code ở thư mục gốc (`claude`). Claude tự đọc `CLAUDE.md`.
4. Viết vào đúng file của mục mình phụ trách trong `thuyet-minh/`. Phần hướng dẫn nằm trong khối chú thích `<!-- -->` ở đầu mỗi file, không bị xuất ra Word.

## Skills (gõ trong Claude Code)

| Lệnh | Việc |
| --- | --- |
| `/dat-ten-de-tai` | Đề xuất và chấm tên đề tài theo công thức và FINER |
| `/doc-bai-bao <DOI hoặc link>` | Kiểm tra chỉ mục, điền phiếu đọc, thêm vào ma trận và `references.bib` |
| `/viet-muc-thuyet-minh <số mục>` | Viết hoặc sửa một mục, đối chiếu barem |
| `/trich-dan-ieee` | Đánh số lại trích dẫn, rà định dạng IEEE |
| `/kiem-tra-truoc-nop` | Chạy checklist nộp bài, gọi hai agent phản biện |
| `/cap-nhat-tien-do` | Cập nhật bảng tiến độ, ghi biên bản họp |

## Agents

| Agent | Việc |
| --- | --- |
| `tong-quan-tai-lieu` | Tìm, đọc, tóm tắt bài báo vào phiếu đọc |
| `thiet-ke-phuong-phap` | Thiết kế dữ liệu, gán nhãn, mô hình, chỉ số đánh giá |
| `phan-bien-thuyet-minh` | Chấm bản thảo theo barem, chỉ đọc, không sửa |
| `kiem-tra-trich-dan` | Xác minh tài liệu tham khảo có thật và trích đúng |

## Tài liệu môn học

Thư mục gốc của thầy: [PPNCKH - SV](https://drive.google.com/drive/folders/1XJo3itEkFnyLw1XF3TOO87T2-ZNz9a3K). Bản tóm tắt các file nằm trong `docs/yeu-cau/`. Lịch trình kèm cột trạng thái cũng có bản Claude Docs: [Lịch trình đồ án PPNCKH](https://claude.ai/artifact/5dLNj8WykNyfFiK7Rh71MT).
