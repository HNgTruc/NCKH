# Bàn giao giữa các phiên làm việc

Cập nhật lần cuối: 08/11/2026 (Chủ nhật). Phiên mới đọc file này trước, rồi đọc `docs/ke-hoach/lich-trinh.md`.

## Hạn chót

Nhóm 5 nộp PDF và trình bày 10 phút cùng ngày thứ Ba 10/11/2026. Còn thứ Hai 09/11 để hoàn thiện.

## Trạng thái hiện tại

| Phần | Trạng thái | Ghi chú |
| --- | --- | --- |
| Mục 1, 3, 7, 10, 11, 12, 13, 16 | Xong nháp | Thời gian thực hiện 10/2026 đến 11/2026, 2 tháng (Trúc chốt lại 08/11). Mục tiêu MT1 đến MT3, không có demo |
| Mục 8, 9 | Xong nháp | 20 tài liệu, đánh số IEEE theo thứ tự xuất hiện, đã kiểm tra không lệch số |
| Mục 14 | Xong nháp | Còn 1 TODO: nơi gửi bản thảo bài báo |
| Mục 15 | 15.1, 15.2 xong | 15.3 "Kết luận và kiến nghị" chờ kết quả notebook |
| Mục 2, 4, 5, 6, bìa | Chờ thông tin | Xem bảng "Trúc cần gửi" |
| Danh mục tài liệu (99) | Xong | 20 tài liệu, mỗi tài liệu có phiếu trong `tong-quan/phieu-doc/` |
| Phản biện | Đã chạy 08/11 | Khoảng 7,2/10. Đã sửa hết 10 vấn đề, trừ việc đọc toàn văn [14] |
| Gán nhãn 600 tin | Trúc đang làm | File `nghien-cuu/du-lieu/processed/tran-2026/gan-nhan-so-bo.csv`, lọc `dot = 1`, điền `nhan_chot` |
| Kappa | Chưa | Khang gán mù `mau-kappa-100.csv` (Trúc chốt Khang là người gán thứ hai thật) |
| Notebook | Viết xong, chưa chạy GPU | `nghien-cuu/notebooks/thu-nghiem-so-bo.ipynb`. Phần không cần GPU đã chạy thử bằng nhãn giả |

## Việc tiếp theo, theo thứ tự

1. **Trúc duyệt xong 600 tin**, gửi `mau-kappa-100.csv` cho Khang. Mốc dừng: nếu tối 08/11 chưa xong thì bỏ phần chạy mô hình, thuyết minh chỉ mô tả kế hoạch.
2. **Trúc chạy notebook trên Colab:** Runtime, Change runtime type, T4 GPU; Run all; tải lên `gan-nhan-so-bo.csv`. Khi Khang gán xong, chạy ô cuối (kappa) với `mau-kappa-100.csv`. Chép `ket-qua-so-bo.json` vào `nghien-cuu/ket-qua/`.
3. **Claude đọc `ket-qua-so-bo.json`** rồi:
   - Viết mục 15.3 "Kết luận và kiến nghị": MT1 đến MT3 đạt tới đâu, H1, H2 có được ủng hộ không. Nói rõ đây là kết quả sơ bộ trên 600 tin.
   - Đưa số kappa, tỉ lệ chuyển nhãn (CH2), bảng F1, kết quả kiểm tra xóa thẻ QC vào chỗ phù hợp. Chỗ đặt kết quả sơ bộ trong thuyết minh: hỏi Trúc.
   - Nếu kappa dưới 0,60: báo đúng con số, theo dòng 5 bảng 13.2.
   - Nếu F1 giảm mạnh khi xóa thẻ: ghi rõ mô hình học thẻ, là hạn chế.
4. **Điền thông tin Trúc gửi** (bảng dưới) vào bìa, mục 2, 4, 5, 6, `docs/ke-hoach/phan-cong.md`, `gia-dinh.md` dòng 1, 2, 4.
5. **Sửa mục 8 theo bài [14]** sau khi Trúc đọc toàn văn hoang-2022. Nếu bộ SMSVN có nhãn lừa đảo riêng, điểm mới chuyển sang tổ hợp: ba lớp loại trừ nhau, hướng dẫn gán nhãn có kappa từ người gán mù, so sánh ba mô hình, đo độ bền khi tin bị biến dạng.
6. **Trúc tự viết lại các đoạn `[TỰ VIẾT LẠI]`:** 4 ở mục 8, 1 ở mục 9, 5 ở mục 12. Đây là phần thầy hỏi khi trình bày.
7. **Kiểm tra trước nộp:** `./scripts/build.ps1`, skill `kiem-tra-truoc-nop`, agent `kiem-tra-trich-dan`. Mục tiêu 0 chỗ `[TODO`, `[CẦN NGUỒN]`, `[TỰ VIẾT LẠI]`.
8. **Xuất PDF:** chép vào file mẫu .docx của trường (bìa theo PhuLuc_3), tên `PPNCKH_MSSV1_MSSV2_MSSV3.pdf`.
9. **Slide 10 phút** từ `trinh-bay/dan-y-slide.md`: thêm 1 slide kết quả sơ bộ, điền tên Khang, Nhân vào cột người nói. Tập 2 lần. Câu hỏi thầy dễ hỏi ở mục "Câu hỏi" bên dưới.
10. **In bản giấy** nộp Văn phòng Khoa.

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
