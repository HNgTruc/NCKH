<!-- HƯỚNG DẪN
Mẫu: Xác định rõ đối tượng nghiên cứu, phạm vi nghiên cứu phù hợp với tên đề tài, mục tiêu của đề tài.
Barem BT2: xác định rõ đối tượng; giới hạn phạm vi.
Slide: đối tượng (focus) là bản chất cần làm rõ; khách thể (population); mẫu khảo sát (sample); phạm vi chia không gian, thời gian, nội dung. Đủ rộng để có ý nghĩa, đủ hẹp để khả thi.

Câu cần trả lời cho đề tài này:
- Đối tượng là gì: các phương pháp phân loại văn bản để nhận diện tin lừa đảo? hay đặc điểm ngôn ngữ của tin lừa đảo tiếng Việt? Chọn một làm trọng tâm.
- Khách thể: tin nhắn SMS bằng tiếng Việt (tên đề tài đã chốt chỉ SMS).
- Không gian: tin gửi tới người dùng tại Việt Nam, nguồn công khai.
- Thời gian: dữ liệu thu thập trong khoảng nào (lưu ý historical bias).
- Nội dung: chỉ văn bản SMS, KHÔNG xử lý email, tin nhắn mạng xã hội (Zalo, Messenger), hình ảnh, giọng nói, cuộc gọi; chỉ phân loại, KHÔNG truy vết người gửi.

Checklist:
- Đối tượng xuất hiện trong tên đề tài
- Có đủ ba loại phạm vi
- Phạm vi nội dung nói rõ cái KHÔNG làm
- Phạm vi khớp với nguồn dữ liệu ở mục 12
-->

## 11. Đối tượng và phạm vi nghiên cứu

### 11.1. Đối tượng nghiên cứu

Đối tượng nghiên cứu là các mô hình phân loại văn bản dùng để phân biệt tin nhắn SMS lừa đảo, tin nhắn quảng cáo và tin nhắn bình thường viết bằng tiếng Việt. Trọng tâm là mô hình ngôn ngữ tiền huấn luyện PhoBERT, đặt cạnh ViSoBERT và mô hình cơ sở TF-IDF kết hợp Logistic Regression. Đề tài làm rõ ba điều: mức chính xác của các mô hình khi tách tin lừa đảo khỏi tin quảng cáo, kiểu nhầm lẫn giữa hai loại tin này, và mức giảm chính xác khi tin bị viết không dấu hoặc chèn ký tự để né bộ lọc.

Khách thể nghiên cứu: tin nhắn SMS tiếng Việt gửi tới người dùng điện thoại di động tại Việt Nam.

Mẫu nghiên cứu: 600 tin chọn ngẫu nhiên phân tầng từ bộ SMS công khai trên Hugging Face, bộ này còn 2.629 tin sau khi bỏ tin trùng [15]. Cách chọn và gán nhãn trình bày ở mục 12.

### 11.2. Phạm vi nghiên cứu

| Phạm vi | Giới hạn |
| --- | --- |
| Không gian | Tin nhắn SMS gửi tới thuê bao di động tại Việt Nam, viết bằng tiếng Việt, gồm cả tin có dấu, không dấu và tin bị viết biến dạng. Không xét tin viết bằng tiếng nước ngoài |
| Thời gian | Tin nhắn được đóng góp vào bộ dữ liệu công khai từ ngày 28/05/2026 đến ngày 03/08/2026, theo cột ngày của bộ dữ liệu. Cột này có thể là ngày đóng góp chứ không phải ngày nhận tin, vì 627 dòng cùng mang ngày 03/08/2026, trùng ngày đăng bộ dữ liệu. Kết luận của đề tài chỉ áp dụng cho kiểu tin lừa đảo trong khoảng thời gian này, vì kịch bản lừa đảo thay đổi theo thời gian |
| Nội dung | Đề tài làm: gán ba nhãn lừa đảo, quảng cáo, bình thường dựa trên nội dung văn bản của tin; so sánh ba mô hình đã nêu; đánh giá trên tin bỏ dấu và tin chèn ký tự; đo trên 600 tin trong thời gian học kỳ (09/2026 đến 11/2026). Đề tài không làm: gán nhãn toàn bộ 2.629 tin, thu thập thêm tin nhắn, xây bản demo (ba việc này để ở hướng phát triển, mục 15); tin trên Zalo, Messenger và mạng xã hội khác, email, hình ảnh, giọng nói, cuộc gọi; không dùng số điện thoại hay tên thương hiệu người gửi, thời điểm gửi; không mở đường link trong tin để kiểm tra trang đích; không xét người nhận đã đồng ý nhận quảng cáo hay chưa; không truy vết người gửi; không tích hợp vào điện thoại hay hệ thống của nhà mạng |
