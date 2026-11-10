<!-- HƯỚNG DẪN
Mẫu: Từ đánh giá tổng quan tình hình nghiên cứu, nêu được hướng giải quyết vấn đề còn tồn tại liên quan đến đề tài; làm rõ mức độ cần thiết của việc thực hiện đề tài, đóng góp mới của đề tài đối với ngành, đối với tổ chức chủ trì, đối với xã hội.
Barem BT2: mô tả tình hình thực tế; chỉ ra thiếu sót của nghiên cứu trước; nêu đề tài giải quyết thế nào, đóng góp gì cho khoa học và thực tiễn.
Slide: thể hiện cấp thiết bằng số liệu thống kê, báo cáo uy tín, xu hướng, so sánh quốc tế.

Khung gợi ý (4 đoạn):
1. Thực trạng: số liệu lừa đảo qua tin nhắn SMS tại Việt Nam, có nguồn chính thống (cơ quan nhà nước, báo cáo an ninh mạng). KHÔNG mở bằng "Trong thời đại 4.0".
2. Thiếu sót: tóm một câu từ mục 8.4.
3. Hướng giải quyết của đề tài: dữ liệu gì, mô hình gì, đo bằng gì.
4. Đóng góp: cho ngành (bộ dữ liệu, kết quả so sánh), cho Trường ĐH Sài Gòn (sinh viên làm NCKH, công bố), cho xã hội (công cụ cảnh báo).

Checklist:
- Có ít nhất 2 số liệu thực tế, mỗi số liệu có [n] và năm
- Không lặp lại nguyên văn mục 8
- Đóng góp nêu đủ ba đối tượng: ngành, tổ chức chủ trì, xã hội
- Không hứa kết quả chưa đo được ("đạt độ chính xác cao")
-->

## 9. Tính cấp thiết của đề tài

Lừa đảo trên không gian mạng gây thiệt hại lớn ở Việt Nam. Theo Cục Cảnh sát hình sự, Bộ Công an, giai đoạn 2020-2025 cả nước xảy ra 24.295 vụ lừa đảo chiếm đoạt tài sản trên không gian mạng, gây thiệt hại gần 40.000 tỷ đồng. Riêng năm 2025 tội phạm lừa đảo giảm hơn 20% [17]. Dù tội phạm lừa đảo giảm, thiệt hại do lừa đảo trực tuyến trong 11 tháng đầu năm 2025 vẫn được ước tính trên 6.000 tỷ đồng [18]. Các số liệu chính thức nhóm tìm được không tách riêng kênh SMS. Tuy vậy, các nghiên cứu trong nước đã nêu lừa đảo là một tác hại của tin nhắn rác [8], [16], và cơ quan quản lý đã đưa tin nhắn có dấu hiệu lừa đảo thành một loại riêng trong dự thảo nghị định thay thế Nghị định 91/2020/NĐ-CP. Dự thảo chia tin nhắn rác thành tin quảng cáo không được người dùng đồng ý, tin kinh doanh vi phạm quy định, tin vi phạm nội dung bị cấm và tin nhắn có dấu hiệu lừa đảo [19].

Các nghiên cứu phân loại SMS tiếng Việt hiện có chưa chia rõ theo cách này. Bộ SMSVN có nhãn lừa đảo và quảng cáo, nhưng một tin có thể mang nhiều nhãn nên hai loại không tách hẳn nhau [14]. Như mục 8 đã phân tích, các nghiên cứu dùng PhoBERT cho SMS tiếng Việt đều phân loại hai lớp, và các bộ dữ liệu xếp tin quảng cáo không thống nhất, lúc vào lớp "rác" [7], lúc vào lớp "hợp lệ" [15]. Vì vậy tin lừa đảo, loại làm người nhận mất tiền, luôn bị gộp với một loại tin ít nguy hiểm hơn, và bộ lọc chỉ báo được tin "rác" hay "không rác". Bài tổng quan trong nước cũng nhận xét rằng cảnh báo hai mức như vậy là chưa đủ [16].

Đề tài giải quyết vấn đề này bằng cách gán lại ba nhãn lừa đảo, quảng cáo và bình thường cho một mẫu SMS tiếng Việt thật lấy từ bộ dữ liệu công khai [15], với hướng dẫn gán nhãn viết sẵn và độ đồng thuận giữa hai người gán đo bằng Cohen's kappa. Trên mẫu này, đề tài so sánh PhoBERT, ViSoBERT và mô hình cơ sở TF-IDF kết hợp Logistic Regression bằng F1 của từng lớp, tỉ lệ nhầm giữa tin lừa đảo và tin quảng cáo, và mức giảm F1 khi tin bị bỏ dấu hoặc chèn ký tự, là hai cách viết thấy ngay trong dữ liệu tin rác tiếng Việt [10], [15], trong khi các bộ lọc hiện có dễ bị né tránh khi tin bị cố ý viết biến dạng [3].

Với ngành công nghệ thông tin, đề tài cung cấp một bộ nhãn ba lớp kèm hướng dẫn gán nhãn có đo độ đồng thuận, cùng kết quả so sánh ba mô hình trên chính bộ nhãn đó. Các nghiên cứu phân loại tin lừa đảo tiếng Việt sau này có thể bắt đầu từ đây. Với Trường Đại học Sài Gòn, đề tài là một sản phẩm nghiên cứu của sinh viên Khoa Công nghệ Thông tin. Mã nguồn chạy lại được, nên giảng viên có thể dùng làm bài thực hành phân loại văn bản tiếng Việt. Với xã hội, kết quả cho biết mô hình nào tách được tin lừa đảo khỏi tin quảng cáo. Nhờ đó bộ lọc tin nhắn có cơ sở để cảnh báo riêng tin lừa đảo thay vì chỉ gắn nhãn "rác", khớp với loại tin có dấu hiệu lừa đảo mà dự thảo nghị định đã tách riêng [19].
