# Báo cáo kiểm tra trước khi nộp, 08/11/2026

Kiểm tra bản thảo trong `thuyet-minh/` (00 đến 99). Hai agent `phan-bien-thuyet-minh` và `kiem-tra-trich-dan` đọc độc lập, chỉ nhận đường dẫn file. Báo cáo này không sửa thuyết minh. Chưa có file PDF nộp nên bước 5 (tên file, bìa) chưa kiểm tra được.

## 1. Bảng kiểm tra 12 dòng

| # | Kiểm tra | Kết quả | Ghi chú |
| --- | --- | --- | --- |
| 1 | Tên đề tài 10 đến 15 từ, giống hệt ở bìa | Đạt | 14 từ, khớp bìa và mục 1 |
| 2 | Mục 8 có ưu và nhược từng nghiên cứu, kết thúc bằng khoảng trống | Cần sửa | Có đủ. Còn `[TODO` ở dòng 39. Một số nhận xét dựa trên tóm tắt. Câu khoảng trống ở 8.4 phụ thuộc bài [14] |
| 3 | Mục 9 có ít nhất 2 số liệu có [n] | Đạt tối thiểu | Có 2 số liệu [17], [18], cả hai về lừa đảo mạng nói chung, không riêng SMS. Cách diễn đạt [17] sai nhẹ |
| 4 | Mục 10: 1 mục tiêu tổng quát, 3 đến 5 MT, 5 câu hỏi gắn MT | Đạt về số lượng | 1 mục tiêu tổng quát, 3 MT, 5 CH. MT1 không khớp kết quả thật (xem 3.1) |
| 5 | Mỗi MT có nội dung ở 13.1 và công việc ở 13.2 | Đạt | Phép xóa thẻ có trong 13.2 nhưng không thuộc MT hay CH nào |
| 6 | Tổng thời gian 13.2 bằng số tháng mục 3 | Cần sửa | Về hình thức khớp 09 đến 11/2026. Việc thật chỉ từ 01/11. Chú thích đầu mục 13 còn ghi "6 tháng" |
| 7 | Người thực hiện ở 13.2 có trong mục 5 | Đạt | Trúc, Khang, Nhân |
| 8 | Mục 12 đủ nguồn dữ liệu, thu thập, gán nhãn, chỉ số, đạo đức, bias | Đạt, còn 1 `[TODO` | `[TODO` ở 12.3 (số tin Trúc đã xem lại) |
| 9 | Mục 16 cộng đúng tổng, có số tiền bằng chữ | Đạt | 500.000 × 3 + 500.000 = 2.000.000, "Hai triệu đồng". Phụ thuộc loại đề tài mục 2 |
| 10 | Trích dẫn IEEE khớp danh mục | Cần sửa | Thứ tự [1] đến [20] đúng, không số mồ côi. Có 3 tài liệu trích sai ý, 3 chỗ sai thông tin (xem mục 4) |
| 11 | Có Kết luận và kiến nghị | Đạt | 15.3, đã có kết quả sơ bộ |
| 12 | Không có "Trong thời đại", "—", in đậm trong thân bài | Đạt | 0 lần. Dấu "–" còn lại nằm trong số trang của danh mục tài liệu |

Dấu hiệu chưa xong còn lại: 4 `[TODO` (mục 2, mục 6, mục 8 dòng 39, mục 12 dòng 45). Mục 7 trống số điện thoại.

## 2. Kết quả agent phản biện theo barem

Barem không có thang điểm số nên agent chấm theo Đạt, Cần sửa, Thiếu. Nhận xét chung: nhóm khá. Khung và tổng quan tốt. Mất điểm ở MT1 (kappa), tiến độ không khớp thực tế, nhiều `[TODO`, độ tin cậy của nhãn.

| Mục | Mức |
| --- | --- |
| Bìa, mục 4 | Đạt |
| Mục 1, 3, 5, 7 | Cần sửa nhẹ |
| Mục 2, 6 | Thiếu (còn `[TODO`) |
| Mục 8 | Cần sửa, là phần mạnh nhất |
| Mục 9, 10, 12, 13, 14, 16, 99 | Cần sửa |
| Mục 11, 15 | Đạt |

Năm vấn đề nặng nhất (theo mức mất điểm):

1. **MT1 không đạt nhưng mục 10 và mục 14 vẫn viết như thể đạt.**
   - κ = 0,569 dưới ngưỡng 0,60. Mục 10 (MT1, CH1) và mục 14 dòng 3 vẫn ghi "hai người gán độc lập" và "ngưỡng 0,60", dòng 3 còn ghi "600 tin" (thực tế 597 tin có nhãn rõ).
   - Kappa đo mức người thứ hai đồng ý với nhãn sơ bộ do mô hình ngôn ngữ gán, không phải giữa hai người.
   - Mẫu kappa 100 tin chọn theo nhãn gợi ý, không có khoảng tin cậy. Với n = 100 sai số khoảng ±0,09, nên 0,569 và 0,60 chưa chắc khác nhau.
   - Sau họp xử lý 29 tin bất đồng không tính lại kappa (đúng, vì sẽ thành 1).
2. **Tiến độ và thời gian không thật với "3 tháng".** Mục 3 ghi 09 đến 11/2026, nhưng 8 trong 9 dòng của 13.2 nằm trong tháng 11. Mục 15.3 báo kết quả đã chạy ngày 08/11 trong khi 13.2 ghi huấn luyện đến 18/11, nên bài trộn thuyết minh với báo cáo. Khang có rất ít việc trong 13.2.
3. **Nhãn có nguy cơ vòng tròn và chưa nêu trong đạo đức.** Script gợi ý nhãn, mẫu chọn theo gợi ý, mô hình ngôn ngữ gán có xem gợi ý, TF-IDF học lại từ khóa. Mục 12.5 chưa nói nội dung 600 tin đã được gửi cho dịch vụ bên thứ ba, trong khi còn tin chứa họ tên. Chưa ghi phiên bản mô hình và prompt.
4. **So sánh mô hình yếu về thống kê.** Chênh lệch giữa ba mô hình nhỏ hơn độ lệch chuẩn. "H2 được ủng hộ" nên đổi thành mô tả. Tỉ lệ như 0,5% ứng với khoảng 1 tin, nên báo số tin. Với PhoBERT, bỏ dấu còn làm bộ tách từ sai, nên không tách được ảnh hưởng của mô hình.
5. **Còn nhiều `[TODO` và tuyên bố tính mới thiếu chiến lược tìm bài.** Chưa có nghiên cứu smishing nước ngoài. Câu "chưa có nghiên cứu nào gán ba lớp" không kèm từ khóa, cơ sở dữ liệu và ngày tìm. Điểm mới yếu vì 8.4 tự nhận dùng PhoBERT không còn mới.

Ba câu thầy dễ hỏi:
1. Kappa dưới ngưỡng tự đặt mà không đo lại, kappa này đo giữa ai với ai khi một bên là mô hình ngôn ngữ?
2. Nhãn có khỏi vòng tròn với từ khóa không, và tên đề tài "bằng PhoBERT" còn ý nghĩa khi PhoBERT không thắng mô hình cơ sở?
3. Thuyết minh ghi 3 tháng nhưng việc bắt đầu từ 01/11, kết quả có ngày 08/11 trong khi kế hoạch ghi huấn luyện đến 18/11. Đây là thuyết minh hay báo cáo?

Agent cũng nhắc: nếu việc Khang gán 100 tin và cuộc họp 08/11 không có thật thì kappa và mục 12.3 là sai sự thật. Trúc đã xác nhận cả hai là có thật.

## 3. Kết quả agent kiểm tra trích dẫn

Thứ tự [1] đến [20] đúng, không số mồ côi, bảng 8.5 cộng khớp (20 tài liệu). Không có tài liệu nào bịa. Chưa xác minh trực tiếp được số tập LNCS và CCIS của [6], [12], [13] vì Springer chặn truy cập, và nội dung file [19] vì tải về dạng nhị phân.

| Mức | Tài liệu và vấn đề |
| --- | --- |
| Trích sai ý, cần sửa | [3] mục 8.1, bảng 8.4: khẳng định "không xét riêng tin lừa đảo" khi mới đọc tóm tắt. |
| | [11] mục 8.3, bảng 8.4: trích cùng [10] cho hai con số trùng nhau, trái phiếu đọc. Số "khoảng 16.000 SMS" của [11] không có cơ sở. |
| | [8] mục 8.3: viết "không công khai" trong khi bài chỉ không nêu. |
| | [10] mục 8.3: hai con số 97,77% (LSTM, bản thêm dấu) và 95,56% (CNN, bản bỏ dấu) viết như một mô hình. |
| | [17] mục 9: "số vụ giảm" sai, nguyên văn là "tội phạm lừa đảo giảm hơn 20%". |
| | [9] bảng 8.4: "chủ yếu báo accuracy" sai, [9] báo cả precision, recall, F1. |
| | [2] bảng 8.4: bỏ sót bộ tweet rác. |
| | [15] mục 8.3: "xếp vào nhãn hợp lệ" là suy luận của nhóm từ số thẻ QC, nên ghi "theo thống kê của nhóm". |
| | [4] mục 8.2: "không thử phân loại văn bản" cần nói chính xác (có tác vụ NLI). |
| | [14] mục 8.3, 8.4: còn `[TODO`, câu khoảng trống dựa vào việc không có nhãn lừa đảo riêng. |
| Sai thông tin | [14]: tên tác giả đầu "Hè" (danh mục, phiếu) so với "Hà" (trang tạp chí), năm 2022 so với 2024. Trúc cần mở trang bài so lại. |
| | [15]: Mai Hoàng Đỉnh là cố vấn trên trang dataset, danh mục đưa vào danh sách tác giả. |
| | [6]: thiếu số tập LNCS. [8], [9]: thiếu "vol." (trang tạp chí ghi Tập 1). |
| | [20]: không có phiếu đọc riêng. |
| Định dạng IEEE | Hội nghị thiếu "City, Country" ([1], [3] đến [5], [7], [11] đến [13]). [17] đến [20] không thống nhất cách ghi nguồn trực tuyến. [14], [16] nối tác giả bằng "và", skill yêu cầu "and". Khối HƯỚNG DẪN đầu mục 99 cần xóa khi nộp. |

Phiếu đọc đều do Claude điền, cột "Trúc đọc" còn `[TODO]`. Nên đọc toàn văn [3], [11], [14] trước khi trình bày.

## 4. Việc cần sửa, xếp theo mức ảnh hưởng đến điểm

| # | Việc | Mục | Người phụ trách |
| --- | --- | --- | --- |
| 1 | Sửa MT1, CH1 và mục 14 dòng 3: ghi kappa 0,569, 597 tin có nhãn rõ, kappa đo giữa Khang và nhãn sơ bộ, bỏ "hai người gán độc lập" | 10, 14 | Nhân (mục 10), Trúc (mục 14) |
| 2 | Chọn cách xử lý tiến độ: giữ 3 tháng thì ghi rõ việc tháng 9, 10, nếu không thì sửa mục 3 và mục 16. Sửa ngày chồng nhau trong 13.2, sửa chú thích "6 tháng". Thêm câu mở 15.3 nói đây là kết quả thử nghiệm sơ bộ của học phần | 3, 13, 15 | Trúc |
| 3 | Sửa các chỗ trích sai ý ở mục 8 và mục 9 (xem bảng ở mục 3 của báo cáo này) | 8, 9, 99 | Khang |
| 4 | Điền số tin đã xem lại nhãn sơ bộ, ghi vai trò mô hình ngôn ngữ trong 12.5 (dữ liệu gửi bên thứ ba, phiên bản, prompt), thêm rủi ro vòng tròn vào bảng bias | 12 | Trúc, Nhân |
| 5 | Đổi "H2 được ủng hộ" thành mô tả, báo số tin thay phần trăm khi mẫu nhỏ, nêu giới hạn của bộ tách từ khi bỏ dấu | 15.3, 12 | Trúc |
| 6 | Đọc toàn văn bài [14] để điền `[TODO` ở mục 8, kiểm tra tên tác giả và năm | 8, 99 | Trúc |
| 7 | Điền mục 2 (loại đề tài), mục 6 (năng lực), số điện thoại thầy ở mục 7 | 2, 6, 7 | Trúc |
| 8 | Thêm smishing nước ngoài và chiến lược tìm bài (từ khóa, cơ sở dữ liệu, ngày) vào 8.4 | 8 | Khang |
| 9 | Thêm 1 số liệu về SMS rác hoặc lừa đảo qua SMS vào mục 9, rút gọn đoạn lặp 8.4 | 9 | Trúc |
| 10 | Thêm "xóa thẻ" vào MT3 hoặc CH, thêm tiêu chí thành công cho MT2, MT3 | 10 | Nhân |
| 11 | Thống nhất định dạng IEEE ([14], [16], [17] đến [20], City, Country), tạo phiếu cho [20], xóa khối HƯỚNG DẪN mục 99 | 99 | Khang |
| 12 | Xuất PDF `PPNCKH_3123411312_3123411143_3123411205.pdf`, bìa theo PhuLuc_3 | | Trúc |
