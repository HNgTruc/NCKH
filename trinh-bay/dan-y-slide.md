# Dàn ý trình bày (khoảng 10 phút)

Đề không yêu cầu nộp slide. Thời lượng 10 phút là giả định, sửa khi thầy công bố. Mỗi slide ghi người nói để chia đều phần cho ba thành viên. A là Huỳnh Ngọc Trúc, B là Phạm Trần Minh Khang, C là Ngô Nguyễn Thành Nhân.

| # | Slide | Nội dung | Lấy từ mục | Thời gian | Người nói |
| --- | --- | --- | --- | --- | --- |
| 1 | Tên đề tài | Tên, nhóm, giảng viên | 1, 4, 5 | 0:20 | Trúc |
| 2 | Vấn đề | Hai số liệu thực tế có nguồn, một ví dụ tin lừa đảo đã ẩn danh | 9 | 1:00 | Trúc |
| 3 | Đã có gì | Bảng so sánh 3 đến 5 nghiên cứu chính | 8 | 1:15 | Khang |
| 4 | Khoảng trống | Một câu, in to | 8.4 | 0:30 | Khang |
| 5 | Mục tiêu và câu hỏi | MT1 đến MT3, 5 câu hỏi, 2 giả thuyết | 10 | 0:50 | Nhân |
| 6 | Đối tượng, phạm vi | Làm gì, không làm gì | 11 | 0:40 | Nhân |
| 7 | Phương pháp | Sơ đồ quy trình: thu thập, ẩn danh, gán nhãn, mô hình, đánh giá | 12 | 1:45 | Nhân |
| 8 | Kết quả sơ bộ | Bảng F1 lớp lừa đảo ba mô hình, bốn dạng tin (gốc, bỏ dấu, chèn ký tự, xóa thẻ), kappa 0,569, H1 và H2 | 15.3 | 1:30 | Trúc |
| 9 | Tiến độ | Bảng 13.2 đến ngày 09/11 | 13.2 | 0:30 | Trúc |
| 10 | Sản phẩm, ứng dụng | Bảng sản phẩm, người dùng | 14, 15 | 0:40 | Trúc |
| 11 | Đạo đức và rủi ro | Ẩn danh, bias, dữ liệu gửi bên thứ ba, vòng tròn nhãn | 12.5 | 0:30 | Khang |
| 12 | Kết | Câu hỏi | | 0:20 | Trúc |

Tổng khoảng 10:10. Nếu quá giờ, rút slide 9 và 10 còn 0:20 mỗi slide.

## Nội dung slide 8 (kết quả sơ bộ)

Số lấy từ `nghien-cuu/ket-qua/ket-qua-so-bo.json`, 597 tin có nhãn rõ, kiểm định chéo 5 phần, seed 42. F1 lớp lừa đảo, trung bình ± độ lệch chuẩn:

| Mô hình | Gốc | Bỏ dấu | Chèn ký tự | Xóa thẻ |
| --- | --- | --- | --- | --- |
| TF-IDF + LR | 91,9 ± 3,4 | 88,5 ± 3,9 | 91,7 ± 3,0 | 91,7 ± 3,0 |
| PhoBERT-base | 90,8 ± 2,9 | 82,2 ± 5,3 | 84,9 ± 3,1 | 89,1 ± 3,5 |
| ViSoBERT | 92,7 ± 4,0 | 86,5 ± 8,3 | 89,2 ± 2,7 | 90,2 ± 3,4 |

Ba ý nói:
1. Kappa vòng đầu 0,569, dưới ngưỡng 0,60. Hai bên xử lý 29 tin bất đồng và thêm hai quy tắc (OTP, tin nhà mạng).
2. H1 không được ủng hộ: PhoBERT không hơn mô hình cơ sở (cao hơn ở 1 trong 5 phần).
3. H2 đúng chiều nhưng chưa chắc: bỏ dấu làm PhoBERT giảm 8,6 điểm, ViSoBERT giảm 6,2 điểm. Chênh lệch nhỏ hơn độ lệch chuẩn.

## Câu hỏi thầy có thể hỏi

Mỗi người chuẩn bị trả lời câu thuộc phần mình.

- Dữ liệu lấy ở đâu, có hợp pháp không, có thông tin cá nhân không? Bộ Hugging Face giấy phép CC BY 4.0, tác giả đã ẩn danh, nhóm quét thêm số điện thoại, còn sót 1 tin có họ tên trong 12 tin kiểm tra nên không đưa dữ liệu lên kho công khai. (Nhân)
- Tại sao không dùng accuracy làm chỉ số chính? Tin bình thường chiếm đa số thì mô hình đoán toàn "bình thường" vẫn có accuracy cao, không bắt tin lừa đảo nào. Dùng precision, recall, F1 từng lớp. (Nhân)
- Tin quảng cáo và tin lừa đảo phân biệt thế nào, hai người gán lệch nhau thì xử lý sao? Quảng cáo không giả danh và không đòi thông tin, lừa đảo giả danh, đòi tiền hoặc bấm link giả. Lệch thì xem 29 tin bất đồng, ghi lý do, thêm quy tắc vào hướng dẫn. (Khang)
- Kappa 0,569 dưới ngưỡng 0,60 mà không đo lại thì sao? Báo đúng con số vòng đầu. Sau họp hai bên thống nhất cả 29 tin nên kappa sẽ thành 1, vô nghĩa. Đo lại cần mẫu mới, đã ghi ở hướng phát triển. (Khang)
- Nhãn do mô hình ngôn ngữ gán thì có đáng tin không? Đã nói rõ trong mục 12: nhãn sơ bộ do Claude gán, Trúc xem lại 300 trong 600 tin, Khang gán độc lập 100 tin. Đây là hạn chế đã ghi. (Trúc)
- Mô hình có chỉ học thẻ (QC) không? Đã thử xóa thẻ: F1 lớp lừa đảo giảm 1,7 đến 2,5 điểm ở hai mô hình transformer, vì tin lừa đảo không mang thẻ. F1 quảng cáo của ViSoBERT giảm 5 điểm nên có học một phần từ thẻ. (Nhân)
- PhoBERT không thắng mô hình cơ sở thì tên đề tài còn ý nghĩa gì? Đây là kết quả thật. Nguyên nhân có thể là mẫu nhỏ, không dò siêu tham số và nhiều tin theo mẫu lặp, chưa phân biệt được. Điểm mới của đề tài nằm ở nhãn ba lớp. (Trúc)
- Đề tài khác gì nghiên cứu đã có cho tiếng Anh? Các nghiên cứu tiếng Anh và tiếng Việt phần lớn chia hai lớp. Đề tài tách tin lừa đảo khỏi tin rác quảng cáo. (Khang)
- Nhóm chưa biết Python, hai tháng có kịp không? Phần đã làm xong sơ bộ trong 8 ngày đầu tháng 11, chạy trên Google Colab bằng notebook có sẵn. Phần còn lại ghi ở hướng phát triển. (Trúc)
- Mô hình bị kẻ lừa đảo lách bằng cách viết không dấu, chèn ký tự thì sao? Đã đo: chèn ký tự làm PhoBERT giảm 5,9 điểm, ViSoBERT 3,5 điểm, mô hình cơ sở gần như không giảm. (Nhân)
