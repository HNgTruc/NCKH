# Bàn giao giữa các phiên làm việc

Cập nhật lần cuối: 10/11/2026 (ngày nộp và trình bày). Phiên mới đọc file này trước, rồi đọc `docs/ke-hoach/bao-cao-kiem-tra-2026-11-08.md`.

## Hạn chót

Nhóm 5 nộp PDF và trình bày 10 phút ngày thứ Ba 10/11/2026.

## Trạng thái hiện tại

| Phần | Trạng thái | Ghi chú |
| --- | --- | --- |
| Thuyết minh mục 1 đến 16, bìa, 99 | Đủ bản thảo | Thời gian thực hiện 10/2026 đến 11/2026, 2 tháng. Bảng 13.2 kết thúc 09/11 |
| Chỗ còn `[TODO` | 2 chỗ | Mục 2 (loại đề tài, Trúc tick), mục 6 (năng lực, nhóm tự điền). Mục 8 đã xong sau khi Trúc đọc bài [14] ngày 10/11: SMSVN có 11 nhãn gồm Scam và Ads, gán đa nhãn, năm 2022, tên tác giả Hoàng Thị Hà |
| Mục 7 | Số điện thoại thầy để trống | Trúc chọn không ghi |
| Dữ liệu | Xong | 600 tin gán nhãn sơ bộ (Claude gán, Trúc xem lại 300/600), Khang gán độc lập 100 tin, 29 tin bất đồng đã họp xử lý 08/11 |
| Kappa | 0,569 vòng đầu | Dưới ngưỡng 0,60. Báo đúng con số, không tính lại sau họp |
| Kết quả | `nghien-cuu/ket-qua/ket-qua-so-bo.json` | 597 tin, 5-fold. H1 không được ủng hộ, H2 đúng chiều nhưng chưa chắc. Đã vào mục 15.3 |
| Kiểm tra trước nộp | Đã chạy 08/11 | Báo cáo ở `docs/ke-hoach/bao-cao-kiem-tra-2026-11-08.md`. Các lỗi nặng đã sửa, còn việc 6, 7, 8, 9 trong báo cáo |
| Slide | `trinh-bay/slide-trinh-bay.pptx` (12 slide) | Chưa xem bản dựng thật. Kịch bản ở `trinh-bay/kich-ban-thuyet-trinh.md` và `.docx` |
| File Word nháp | `xuat-ban/thuyet-minh-nhap.docx` | Ghép bằng thư viện docx, không phải file mẫu của trường |

## Việc còn lại

1. Trúc tick mục 2, nhóm điền mục 6.
2. Chép nội dung vào file mẫu .docx của trường (bìa theo PhuLuc_3), xuất PDF `PPNCKH_3123411312_3123411143_3123411205.pdf`.
3. Mở file slide và file Word xem bố cục.
4. In bản giấy nộp Văn phòng Khoa.
5. Tùy chọn: thêm nghiên cứu smishing nước ngoài và chiến lược tìm bài vào 8.4, thêm 1 số liệu SMS vào mục 9.
6. Commit: nhiều thay đổi chưa commit. Claude không tự commit, đưa lệnh cho Trúc chạy.

## Trúc cần gửi

| Thông tin | Dùng ở |
| --- | --- |
| Họ tên đầy đủ, MSSV, lớp của Khang và Nhân | Bìa, mục 5, tên file PDF |
| Lớp, điện thoại, email của Trúc | Mục 4, mục 5 |
| Loại đề tài (A1, B1, B2 hay C): Trúc hỏi nhóm khác | Mục 2, `gia-dinh.md` dòng 4 |
| Môn đã học, dự án, kỹ năng có thật của từng người | Mục 6 |
| Nơi gửi bản thảo bài báo | Mục 14 dòng 1 |
| Kênh nộp PDF, giới hạn trang | `gia-dinh.md` dòng 2, 6 |
| Kết quả đọc toàn văn bài [14] hoang-2022 | Mục 8 |

## Quyết định đã chốt (đừng hỏi lại)

- Dữ liệu: bộ Hugging Face tran-2026 (CC BY 4.0, commit `a90e2bd`), 2.629 tin sau bỏ trùng, dùng 600 tin đợt 1 (200 mỗi nhãn gợi ý, seed 42). Không tự thu tin nhắn trong học kỳ.
- Nhãn: `LUA_DAO`, `QUANG_CAO`, `BINH_THUONG`, `KHONG_RO`. Cờ bạc và hẹn hò "trợ cấp" là `LUA_DAO`. Tin nhà mạng gán theo nội dung, không theo thẻ.
- Kappa ≥ 0,60, tính cả `KHONG_RO`. Trúc duyệt có xem gợi ý (ghi là hạn chế neo), Khang gán mù.
- Mô hình: TF-IDF + LR, PhoBERT-base, ViSoBERT; 5-fold; MT3 đo bỏ dấu và chèn ký tự; thêm kiểm tra xóa thẻ QC/TB.
- Kinh phí 2.000.000 đồng, tự dự trù theo nhu cầu. Không có khoản thuê GPU hay thuê người gán.
- Phiếu đọc cho báo chí và văn bản pháp luật: phiếu đầy đủ theo mẫu.
- Giữ tên đề tài "Phân loại tin nhắn SMS lừa đảo và quảng cáo tiếng Việt bằng PhoBERT".

## Câu hỏi thầy dễ hỏi (theo phản biện)

1. Tin quảng cáo phần lớn có thẻ (QC), vậy mô hình có học gì ngoài thẻ không? Trả lời bằng kết quả xóa thẻ trong notebook.
2. Bài [14] đã gán nhiều nhãn cho SMS tiếng Việt, điểm mới ở đâu? Trả lời sau khi đọc toàn văn [14].
3. Ai gán nhãn, kappa có ý nghĩa không khi người thứ nhất thấy nhãn gợi ý? Khang gán mù; báo chênh lệch tỉ lệ trùng gợi ý giữa hai người.
4. 600 tin, mỗi phần kiểm tra khoảng 40 tin lừa đảo, F1 chênh 2 điểm nói được gì? Bằng chứng sơ bộ, có trung bình ± độ lệch chuẩn, bootstrap để ở 15.2.
5. Cờ bạc có phải lừa đảo không, dự thảo để loại khác? Nêu lý do của nhóm, thừa nhận là hạn chế.

## Lưu ý kỹ thuật cho Claude

- Notebook sinh từ script trong scratchpad của phiên cũ, không còn dùng được. Muốn sửa notebook thì sửa thẳng file `.ipynb`, rồi chạy thử phần không cần GPU bằng `/c/Users/hntruc/anaconda3/python.exe` (bản này có scikit-learn; `python` mặc định không có).
- Python mặc định in tiếng Việt lỗi mã hóa: dùng `python -I -X utf8`.
- Heredoc bash dài chứa tiếng Việt có lúc lỗi: ghi nội dung ra file tạm bằng Write rồi ghép bằng Python.
- Trích dẫn mới dùng dạng `[TODO: trích <mã phiếu>]` rồi đánh số bằng skill `trich-dan-ieee`.
- Claude không tự commit. Cuối mỗi việc đưa lệnh `git add` và `git commit` chia theo mục để Trúc chạy.
