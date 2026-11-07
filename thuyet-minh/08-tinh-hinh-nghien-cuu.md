<!-- HƯỚNG DẪN
Mẫu: Tổng quan tình hình nghiên cứu trong và ngoài nước; phân tích, đánh giá những kết quả đạt được, xác định những tồn tại hạn chế của công bố liên quan đến lĩnh vực của đề tài; thống kê tài liệu tham khảo đã sử dụng.
Barem BT2: tóm tắt các nghiên cứu trước; phân tích ưu nhược điểm của từng nghiên cứu; làm rõ tính mới và đóng góp mới của đề tài.
Slide: tổ chức theo chủ đề, thời gian hoặc phương pháp; KẾT THÚC bằng khoảng trống nghiên cứu.
Nguồn dữ liệu cho mục này: tong-quan/ma-tran-tong-quan.md và tong-quan/phieu-doc/.

Khung gợi ý (tổ chức theo chủ đề):
8.1 Nghiên cứu ngoài nước: phát hiện tin rác và lừa đảo qua SMS, email (dữ liệu tiếng Anh)
8.2 Mô hình ngôn ngữ cho tiếng Việt dùng cho bài toán phân loại văn bản
8.3 Nghiên cứu và công cụ trong nước về lừa đảo trực tuyến
8.4 Tồn tại, hạn chế và khoảng trống mà đề tài giải quyết
8.5 Thống kê tài liệu đã dùng (bảng: số bài theo loại nguồn, theo năm)

Checklist:
- Mỗi nghiên cứu được nhắc có ít nhất một ưu điểm VÀ một hạn chế cụ thể
- Có cả nghiên cứu trong nước và ngoài nước
- Mọi câu nêu kết quả của người khác đều có [n]
- Đoạn cuối nêu khoảng trống bằng một câu rõ, và câu đó dẫn thẳng sang mục 9
- Có bảng thống kê tài liệu
- Không có [CẦN NGUỒN]
-->

## 8. Tình hình nghiên cứu liên quan đến đề tài

### 8.1. Nghiên cứu ngoài nước

Phát hiện SMS rác bằng học máy đã được nghiên cứu nhiều với dữ liệu tiếng Anh. Bộ SMS Spam Collection gồm 5.574 tin (4.827 tin hợp lệ, 747 tin rác) được Almeida và cộng sự công bố năm 2011 và trở thành bộ dữ liệu chuẩn để so sánh; trong các phương pháp thử nghiệm, SVM cho kết quả tốt nhất và được đề xuất làm mức cơ sở [1]. Ưu điểm của bộ này là công khai, có giấy phép rõ. Hạn chế là dữ liệu nhỏ, cũ, chỉ có hai lớp và tin hợp lệ với tin rác lấy từ các nguồn khác nhau. Liu và cộng sự đề xuất một mô hình Transformer có sửa đổi, đạt accuracy 98,92% và F1 0,9613 trên SMS Spam Collection [2]. Kết quả cho thấy mô hình dựa trên cơ chế chú ý (attention) phù hợp với văn bản ngắn, nhưng bộ dữ liệu lệch lớp nên accuracy cao chưa nói nhiều về khả năng bắt tin rác. Salman và cộng sự dùng hơn 68.000 tin để so sánh học máy nông, mạng sâu và các dịch vụ chống rác thương mại, và cho thấy mọi phương pháp đều dễ bị né tránh khi tin bị cố ý viết biến dạng [3]. Nghiên cứu này chỉ ra một điểm yếu thực tế của bộ lọc, nhưng vẫn phân loại hai lớp và không xét riêng tin lừa đảo. [TỰ VIẾT LẠI]

### 8.2. Mô hình ngôn ngữ cho tiếng Việt

PhoBERT là mô hình ngôn ngữ đơn ngữ tiếng Việt đầu tiên quy mô lớn, học trên 20GB văn bản Wikipedia và tin tức đã tách từ, và vượt XLM-R ở cả bốn tác vụ được thử, ví dụ F1 nhận dạng thực thể 94,7 so với 92,8 [4]. Ưu điểm của PhoBERT là công khai với giấy phép mở và được dùng rộng rãi. Hạn chế là bài gốc không thử tác vụ phân loại văn bản, dữ liệu tiền huấn luyện là văn bản chuẩn có dấu, và đầu vào phải được tách từ trước. ViSoBERT học trên 1GB bình luận Facebook, TikTok, YouTube để xử lý văn bản mạng xã hội [5]. Trên bộ ViSpamReviews bốn lớp, ViSoBERT đạt F1 trung bình macro 79,06 so với 76,88 của PhoBERT-large; khi bỏ hết dấu, PhoBERT-large giảm 4,99 điểm còn ViSoBERT giảm 2,94 điểm [5]. Đây là bằng chứng ViSoBERT chịu văn bản không dấu tốt hơn, nhưng mô hình chỉ được phép dùng cho nghiên cứu và chưa được thử với SMS. Dinh và cộng sự xây dựng ViSpamReviews gồm 19.868 đánh giá sản phẩm, gán hai lớp và bốn lớp với quy trình gán nhãn có đo Cohen's kappa (0,72 sau một vòng huấn luyện lại người gán), và PhoBERT đạt F1 trung bình macro 86,89 với hai lớp, 72,17 với bốn lớp [6]. Nghiên cứu cho thấy chia "rác" tiếng Việt thành nhiều loại là làm được, nhưng dữ liệu là đánh giá sản phẩm chứ không phải SMS và không có nhãn lừa đảo. [TỰ VIẾT LẠI]

### 8.3. Nghiên cứu trong nước về tin nhắn rác và lừa đảo

Pham và Le-Hong xây dựng hệ thống lọc SMS rác tiếng Việt với 6.599 tin từ Viettel và Vinaphone; SVM kết hợp túi từ và độ dài tin đạt tỉ lệ bắt tin rác 93,91% với tỉ lệ báo nhầm 0,45% [7]. Ưu điểm là có bước tiền xử lý riêng cho tiếng Việt và báo cả tỉ lệ báo nhầm. Hạn chế là chỉ hai lớp, dữ liệu năm 2016 từ hai nhà mạng, và khoảng 70% tin rác là quảng cáo của chính nhà mạng, nên tin lừa đảo bị gộp chung với tin quảng cáo.

Các nghiên cứu gần đây chuyển sang PhoBERT. Vu và cộng sự kết hợp PhoBERT với mạng nơ-ron sâu trên 5.113 tin, đạt accuracy 0,995 [8]; đây là một trong những bài đầu tiên đưa PhoBERT vào SMS rác tiếng Việt, nhưng dữ liệu nhỏ, không công khai và bài không mô tả cách gán nhãn. Một nghiên cứu khác của nhóm so sánh các cách biểu diễn từ trên khoảng 75.000 tin và đạt F1 0,941 với PhoBERT kết hợp CNN, so với 0,899 của TF-IDF kết hợp Naive Bayes [9]; bài có mô hình cơ sở rõ ràng, nhưng tin rác và tin hợp lệ lấy từ các nguồn khác nhau nên mô hình có thể học đặc điểm của nguồn thay vì nội dung. Vũ Minh Tuấn và cộng sự tạo ba phiên bản dữ liệu (gốc, bỏ dấu, thêm dấu) để xem ảnh hưởng của dấu thanh, với accuracy 97,77% trên bản có dấu và 95,56% trên bản không dấu [10], [11]; đây là nghiên cứu duy nhất tìm được xét riêng dấu thanh, nhưng trong dữ liệu gốc tin rác phần lớn không dấu còn tin hợp lệ có dấu, nên dấu thanh trùng với nhãn. Hoang Quang Anh và cộng sự đưa PhoBERT vào học liên kết (federated learning), cách huấn luyện không cần gom tin nhắn của người dùng về một nơi, và đạt accuracy 99,38% [12]. Ho-Lam và cộng sự dùng PhoBERT rút gọn cho tin song ngữ Anh, Việt và đạt 96,75% [13], cho thấy tin rác gửi tới người dùng Việt Nam có cả tiếng Anh. Hai bài [12], [13] chỉ báo accuracy và nhóm mới đọc được tóm tắt. Nhìn chung, các nghiên cứu này cho thấy PhoBERT cho kết quả cao với SMS tiếng Việt; các bài nhóm đọc được toàn văn [8]-[10] đều phân loại hai lớp và không công khai dữ liệu.

Hoàng Thị Hè và cộng sự là nghiên cứu duy nhất tìm được gán nhiều nhãn cho SMS tiếng Việt, trên bộ SMSVN 2.000 tin, có nhắc đến tin lừa đảo và tin quảng cáo, và chọn Classifier Chains kết hợp Gaussian Naive Bayes [14]. Hướng đa nhãn cho thấy một tin có thể thuộc nhiều loại, nhưng bộ dữ liệu nhỏ, chưa dùng mô hình tiền huấn luyện, và nhóm chưa đọc được bộ nhãn cụ thể [TODO: Trúc mở toàn văn hoang-2022-sms-da-nhan, kiểm tra SMSVN có nhãn lừa đảo riêng không, sửa câu này]. Về dữ liệu, bộ SMS tiếng Việt công khai duy nhất tìm được là bộ của Trần Nguyễn Thái Tuấn và cộng sự đăng trên Hugging Face năm 2026, gồm 2.991 tin theo giấy phép CC BY 4.0, với F1 của PhoBERT-base là 96,63% [15]. Bộ này có giấy phép rõ và dữ liệu mới, nhưng chỉ có hai nhãn, và tin quảng cáo của nhà mạng được xếp vào nhãn "hợp lệ", ngược với cách xếp ở [7]. Bài tổng quan của Vũ Duy Hiến và cộng sự nhận xét rằng các mô hình đạt độ chính xác trên 90% nhưng thiệt hại thực tế không giảm, rằng chỉ cảnh báo tin "thường" hay "rác" là chưa đủ, và khuyến nghị nhận diện riêng tin có dấu hiệu lừa đảo [16]. Bài tổng quan này chỉ đúng khoảng cách giữa kết quả trên giấy và thiệt hại thực tế, nhưng không nêu cách chọn bài và nhiều số liệu lấy lại từ báo chí. [TỰ VIẾT LẠI]

### 8.4. Tồn tại và khoảng trống nghiên cứu

| Nghiên cứu | Ngôn ngữ | Dữ liệu | Số lớp | Mô hình tốt nhất | Hạn chế chính |
| --- | --- | --- | --- | --- | --- |
| [1] | Anh | 5.574 SMS, công khai | 2 | SVM | Nhỏ, cũ, hai nguồn khác nhau |
| [2] | Anh | SMS Spam Collection | 2 | Transformer | Chỉ đánh giá trên dữ liệu lệch lớp |
| [3] | Không nêu trong tóm tắt | Hơn 68.000 SMS | 2 | So sánh nhiều nhóm | Không tách tin lừa đảo |
| [6] | Việt | 19.868 đánh giá sản phẩm | 2 và 4 | PhoBERT | Không phải SMS, không có nhãn lừa đảo |
| [7] | Việt | 6.599 SMS, năm 2016 | 2 | SVM | Quảng cáo nhà mạng tính là rác |
| [8], [9] | Việt | 5.113 và khoảng 75.000 SMS, không công khai | 2 | PhoBERT kết hợp DNN, CNN | Không công khai, chủ yếu báo accuracy |
| [10], [11] | Việt | Khoảng 16.000 SMS, không nêu công khai | 2 | LSTM, CNN | Dấu thanh trùng với nhãn |
| [14] | Việt | 2.000 SMS | Đa nhãn | Classifier Chains, Naive Bayes | Nhỏ, không dùng mô hình tiền huấn luyện |
| [15] | Việt | 2.991 SMS, công khai | 2 | PhoBERT-base | Quảng cáo tính là hợp lệ |

So sánh các nghiên cứu cho thấy ba điểm. Thứ nhất, PhoBERT đã được dùng cho SMS tiếng Việt và cho kết quả cao [8]-[13], [15], nên dùng PhoBERT không còn là điểm mới. Thứ hai, các nghiên cứu dùng PhoBERT cho SMS tiếng Việt đều phân loại hai lớp, và các bộ dữ liệu xếp tin quảng cáo không thống nhất: bộ năm 2016 tính quảng cáo nhà mạng là tin rác [7], bộ năm 2026 tính là tin hợp lệ [15]. Tin lừa đảo, loại gây thiệt hại tiền bạc, vì vậy luôn bị gộp với một loại tin ít nguy hiểm hơn. Thứ ba, chia "rác" tiếng Việt thành nhiều loại với quy trình gán nhãn có đo đồng thuận đã làm được với đánh giá sản phẩm [6], và bài tổng quan trong nước cũng khuyến nghị nhận diện riêng tin lừa đảo [16]. Trong phạm vi đã tìm, chưa có nghiên cứu nào gán nhãn SMS tiếng Việt thành ba lớp loại trừ nhau, tách riêng tin lừa đảo, tin quảng cáo và tin bình thường, theo hướng dẫn gán nhãn có đo độ đồng thuận, rồi đánh giá PhoBERT trên bộ nhãn đó. Đây là khoảng trống đề tài hướng tới, và mục 9 trình bày vì sao cần lấp khoảng trống này. [TỰ VIẾT LẠI]

### 8.5. Thống kê tài liệu đã sử dụng

| Loại tài liệu | Số lượng | Tài liệu |
| --- | --- | --- |
| Bài tạp chí quốc tế | 2 | [2], [3] |
| Bài tạp chí trong nước | 5 | [8]-[10], [14], [16] |
| Bài hội nghị | 8 | [1], [4]-[7], [11]-[13] |
| Bộ dữ liệu công khai | 1 | [15] |
| Bài báo và văn bản dự thảo của cơ quan nhà nước | 3 | [17]-[19] |
| Kho mã nguồn | 1 | [20] |
| Tổng | 20 | 3 nghiên cứu ngoài nước; 13 nghiên cứu hoặc bộ dữ liệu trong nước, về tiếng Việt; 3 nguồn số liệu, văn bản trong nước; 1 kho mã nguồn |

Theo năm công bố: 2011 (1), 2016 (1), 2020 (1), 2021 (1), 2022 (3), 2023 (4), 2024 (3), 2025 (2), 2026 (3); kho mã nguồn [20] không ghi năm. Bảy tài liệu [1]-[3], [11]-[14] nhóm mới đọc được tóm tắt, vì toàn văn không truy cập mở.
