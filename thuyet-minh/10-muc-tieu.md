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

Tinh chỉnh và đánh giá mô hình phân loại tin nhắn SMS tiếng Việt thành ba nhóm lừa đảo, quảng cáo và bình thường dựa trên PhoBERT, để tách tin lừa đảo khỏi tin rác quảng cáo.

### 10.2. Mục tiêu cụ thể

- MT1. Gán lại ba nhãn lừa đảo, quảng cáo, bình thường cho 600 tin SMS chọn ngẫu nhiên phân tầng từ một bộ SMS tiếng Việt công khai chỉ có hai nhãn [15], theo một hướng dẫn gán nhãn viết sẵn. Nhãn sơ bộ do mô hình ngôn ngữ gán và người gán thứ nhất xem lại, người gán thứ hai gán độc lập 100 tin không xem nhãn, và độ đồng thuận giữa hai bên đo bằng Cohen's kappa với ngưỡng mục tiêu từ 0,60 trở lên.
- MT2. Đánh giá và so sánh ba mô hình TF-IDF kết hợp Logistic Regression (mô hình cơ sở), PhoBERT và ViSoBERT trên các tin đã gán nhãn của mẫu 600 tin (trừ tin không đủ căn cứ gán nhãn) bằng kiểm định chéo 5 phần, đo precision, recall, F1 của từng lớp, F1 trung bình macro và ma trận nhầm lẫn. Mục tiêu hoàn thành khi có bảng kết quả dạng trung bình ± độ lệch chuẩn qua 5 phần cho cả ba mô hình.
- MT3. Đánh giá mức giảm F1 lớp lừa đảo của ba mô hình khi tin nhắn trong tập kiểm tra bị bỏ dấu thanh, bị chèn ký tự hoặc bị xóa thẻ quảng cáo (QC), (TB) ở đầu tin, so với tin nguyên gốc. Phép xóa thẻ kiểm tra mô hình có chỉ học thẻ thay vì nội dung hay không. Mục tiêu hoàn thành khi có bảng mức giảm F1 cho cả ba kiểu biến đổi và cả ba mô hình.

### 10.3. Câu hỏi nghiên cứu

| # | Câu hỏi | Ứng với |
| --- | --- | --- |
| CH1 | Theo hướng dẫn gán nhãn của đề tài, người gán thứ hai và nhãn sơ bộ đồng thuận ở mức nào (Cohen's kappa) khi chia tin nhắn thành lừa đảo, quảng cáo và bình thường, và loại tin nào gây bất đồng nhiều nhất? | MT1 |
| CH2 | Tin mà bộ dữ liệu gốc gán nhãn "hợp lệ" và tin gán nhãn "rác hoặc lừa đảo" chuyển sang ba nhãn mới theo tỉ lệ nào? | MT1 |
| CH3 | Precision, recall và F1 của lớp lừa đảo ở PhoBERT, ViSoBERT và mô hình cơ sở TF-IDF kết hợp Logistic Regression chênh nhau bao nhiêu? | MT2 |
| CH4 | Ở từng mô hình, bao nhiêu phần trăm tin lừa đảo bị dự đoán thành tin quảng cáo, và bao nhiêu phần trăm tin quảng cáo bị dự đoán thành tin lừa đảo? | MT2 |
| CH5 | F1 lớp lừa đảo của mỗi mô hình giảm bao nhiêu điểm khi tin nhắn bị bỏ dấu thanh, bị chèn ký tự hoặc bị xóa thẻ quảng cáo, và mô hình nào giảm ít nhất? | MT3 |

### 10.4. Giả thuyết nghiên cứu

- H1. PhoBERT đạt F1 lớp lừa đảo cao hơn mô hình cơ sở TF-IDF kết hợp Logistic Regression.
- H2. Khi bỏ dấu thanh toàn bộ tập kiểm tra, F1 lớp lừa đảo của ViSoBERT giảm ít hơn của PhoBERT.

H2 dựa trên kết quả đã công bố của ViSoBERT với dữ liệu đánh giá sản phẩm tiếng Việt [5]. Dữ liệu đó không phải SMS, nên đề tài kiểm tra lại trên tin nhắn. Với 600 tin và 5 phần kiểm định chéo, kết quả cho H1 và H2 chỉ là bằng chứng sơ bộ, chưa đủ để kiểm định thống kê.
