<!-- HƯỚNG DẪN
Mẫu: Nêu mục tiêu chung, các mục tiêu cụ thể phù hợp với tên đề tài, tính cấp thiết của đề tài, kết quả cuối cùng mà đề tài hướng đến.
Barem BT2: mục tiêu tổng quát; mục tiêu cụ thể chia nhỏ, dễ đo lường, đánh giá tiến độ.
Bài tập 1: 05 câu hỏi nghiên cứu rút ra từ tổng quan.
Slide: tổng quát 1 câu; cụ thể 3 đến 5 ý, bắt đầu bằng động từ đo được (Xác định, Phân tích, Đánh giá, Đề xuất, Xây dựng); mỗi câu hỏi ứng với một mục tiêu; giả thuyết chỉ cho nghiên cứu định lượng (đề tài này là định lượng, nên có giả thuyết).

Ví dụ hình thức một mục tiêu đo được (số liệu là chỗ trống, nhóm tự đặt sau khi đọc tổng quan):
"MT3. Đánh giá [mô hình] trên tập kiểm tra bằng precision, recall, F1 cho lớp lừa đảo, so với [mô hình cơ sở]."

Checklist:
- 1 câu tổng quát khớp với tên đề tài
- 3 đến 5 mục tiêu cụ thể, đánh số MT1, MT2... để mục 13 tham chiếu
- Mỗi mục tiêu có thứ đo được hoặc sản phẩm kiểm tra được
- 5 câu hỏi nghiên cứu, mỗi câu ghi rõ ứng với MT nào
- Không có câu hỏi kiểu "Có thể xây dựng... không?"
- Giả thuyết (nếu có) phát biểu được thành phép so sánh kiểm chứng được
-->

## 10. Mục tiêu đề tài

### 10.1. Mục tiêu tổng quát

Xây dựng và đánh giá mô hình phân loại tin nhắn SMS tiếng Việt thành ba nhóm lừa đảo, quảng cáo và bình thường dựa trên PhoBERT, để tách tin lừa đảo khỏi tin rác quảng cáo.

### 10.2. Mục tiêu cụ thể

- MT1. Xây dựng bộ dữ liệu khoảng 3.000 tin nhắn SMS tiếng Việt đã ẩn danh, gán ba nhãn lừa đảo, quảng cáo, bình thường theo một hướng dẫn gán nhãn viết sẵn, với độ đồng thuận giữa hai người gán đo bằng Cohen's kappa đạt ngưỡng nêu ở mục 12.
- MT2. Đánh giá và so sánh ba mô hình TF-IDF kết hợp Logistic Regression (mô hình cơ sở), PhoBERT và ViSoBERT trên cùng tập kiểm tra bằng precision, recall, F1 của từng lớp, F1 trung bình macro và ma trận nhầm lẫn.
- MT3. Đánh giá mức giảm F1 của ba mô hình khi tin nhắn trong tập kiểm tra bị bỏ dấu thanh hoặc bị chèn ký tự, so với tin nguyên gốc.
- MT4. Xây dựng bản demo web dùng mô hình có F1 lớp lừa đảo cao nhất ở MT2: người dùng dán một tin nhắn vào và nhận lại nhãn dự đoán kèm xác suất của từng nhãn.

### 10.3. Câu hỏi nghiên cứu

| # | Câu hỏi | Ứng với |
| --- | --- | --- |
| CH1 | Theo hướng dẫn gán nhãn của đề tài, hai người gán độc lập đồng thuận ở mức nào (Cohen's kappa) khi chia tin nhắn thành lừa đảo, quảng cáo và bình thường, và loại tin nào gây bất đồng nhiều nhất? | MT1 |
| CH2 | Trên cùng tập kiểm tra, precision, recall và F1 của lớp lừa đảo ở PhoBERT, ViSoBERT và mô hình cơ sở TF-IDF kết hợp Logistic Regression chênh nhau bao nhiêu? | MT2 |
| CH3 | Ở từng mô hình, bao nhiêu phần trăm tin lừa đảo bị dự đoán thành tin quảng cáo, và bao nhiêu phần trăm tin quảng cáo bị dự đoán thành tin lừa đảo? | MT2 |
| CH4 | F1 lớp lừa đảo của mỗi mô hình giảm bao nhiêu điểm khi tin nhắn bị bỏ dấu thanh hoặc bị chèn ký tự, và mô hình nào giảm ít nhất? | MT3 |
| CH5 | Khi chạy trong bản demo trên máy tính không có GPU, mô hình được chọn cần bao lâu để phân loại một tin nhắn? | MT4 |

### 10.4. Giả thuyết nghiên cứu

- H1. Trên cùng tập kiểm tra, PhoBERT đạt F1 lớp lừa đảo cao hơn mô hình cơ sở TF-IDF kết hợp Logistic Regression.
- H2. Khi bỏ dấu thanh toàn bộ tập kiểm tra, F1 lớp lừa đảo của ViSoBERT giảm ít hơn của PhoBERT.

H2 dựa trên kết quả đã công bố của ViSoBERT với dữ liệu đánh giá sản phẩm tiếng Việt [TODO: số trích dẫn của nguyen-2023-visobert sau khi đánh số IEEE]. Dữ liệu đó không phải SMS, nên đề tài kiểm tra lại trên tin nhắn.
