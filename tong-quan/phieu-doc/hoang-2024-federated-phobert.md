# hoang-2024-federated-phobert: Federated Learning for Vietnamese SMS Spam Detection Using Pre-trained PhoBERT

Chỉ đọc tóm tắt. Claude điền ngày 06/11/2026 từ trang chương sách trên SpringerLink (tóm tắt, từ khóa, đơn vị, danh mục tham khảo). Toàn văn cần trả phí, không có bản xem trước. Semantic Scholar ghi "closed". Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu. Một số thông tin về dữ liệu lấy từ nguồn thứ cấp (bài tổng quan preprint của Pritom và cộng sự, 2026), ghi rõ ở từng ô. Trúc cần đọc toàn văn qua thư viện trường trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Hoang Quang Anh, Pham Tuan Anh, Pham Son Nguyen, Phan Duy Hung (tác giả liên hệ). Đơn vị: Trường Đại học FPT, Hà Nội (SpringerLink). Trang Springer rút gọn danh sách tác giả bằng dấu "…", Semantic Scholar ghi 4 tác giả |
| Năm | 2024 |
| Tên tạp chí hoặc hội nghị | Intelligent Data Engineering and Automated Learning (IDEAL 2024), Lecture Notes in Computer Science, vol. 15346, tr. 254-264, Springer |
| DOI hoặc link chính thức | [10.1007/978-3-031-77731-8_24](https://doi.org/10.1007/978-3-031-77731-8_24) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. CORE portal chặn truy cập tự động (lỗi 403, 06/11/2026). [TODO: Trúc tra hạng IDEAL trên CORE, ghi link] |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 06/11/2026. Trúc: [TODO: đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: phát hiện SMS rác được quan tâm vì thiết bị di động phổ biến. Phần lớn cách huấn luyện hiện nay cần gom dữ liệu tập trung |
| Khoảng trống tác giả muốn giải quyết | Tóm tắt: gom dữ liệu tin nhắn về một chỗ gây lo ngại về quyền riêng tư, nên cần cách huấn luyện không phải chia sẻ dữ liệu giữa các bên |
| Mục tiêu | Tóm tắt: đề xuất huấn luyện bằng học liên kết (federated learning, FL), mỗi bên giữ dữ liệu của mình |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS rác tiếng Việt (từ khóa: Vietnamese SMS spam detection) |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Bài không nêu (trong tóm tắt). Danh mục tham khảo không có nguồn bộ SMS tiếng Việt nào. Nguồn thứ cấp: bài tổng quan Pritom và cộng sự (arXiv 2604.11429, 2026) ghi dữ liệu là "Private (English + Vietnamese)" (Bảng 11) và mỗi client có phân bố tin "spam and non-spam" cân bằng (mục 5.1.5), tức 2 lớp và không công khai. Chưa đối chiếu với toàn văn |
| Đặc trưng, đầu vào | PhoBERT đã tinh chỉnh (fine-tuned) (tóm tắt) |
| Phương pháp, mô hình | PhoBERT kết hợp ba thuật toán FL: FedAvg, FedAvgM, FedAdam. Thử ở hai kịch bản phân bố dữ liệu IID (các bên giống nhau) và Non-IID (các bên khác nhau) (tóm tắt) |
| Chỉ số đánh giá | Accuracy (tóm tắt). Chỉ số khác: bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: FedAvg đạt accuracy 99,38% ở kịch bản IID. Ở Non-IID, FedAdam tốt nhất, tới 98,5%. Tác giả kết luận PhoBERT huấn luyện bằng FL đạt gần mức huấn luyện tập trung |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Bài quốc tế mới (2024) dùng PhoBERT cho SMS rác tiếng Việt, thêm bằng chứng PhoBERT đã được dùng cho bài toán này. Đặt vấn đề quyền riêng tư của tin nhắn, gần với mục đạo đức của đề tài. Ví dụ: mỗi nhà mạng tự huấn luyện trên tin của khách hàng mình, chỉ gửi trọng số mô hình đi, không gửi nội dung tin.

Hạn chế: Chưa đọc toàn văn. Tóm tắt không nêu dữ liệu, số lớp, cách chia tập. Theo nguồn thứ cấp, dữ liệu riêng, trộn tiếng Anh và tiếng Việt, 2 lớp. Chỉ báo accuracy, mà accuracy 99% trên dữ liệu 2 lớp không nói được mô hình bắt tin lừa đảo tốt đến đâu.

Dùng cho mục nào của thuyết minh: Mục 8.3, nhóm bài dùng PhoBERT cho SMS rác tiếng Việt. Mục 12 hoặc 15, gợi ý về bảo vệ dữ liệu tin nhắn. Chưa dùng làm bằng chứng "chỉ 2 lớp" cho tới khi đọc toàn văn, vì thông tin 2 lớp hiện chỉ đến từ nguồn thứ cấp.

## Trích dẫn IEEE

```
[n] Q. A. Hoang, T. A. Pham, S. N. Pham, and D. H. Phan, "Federated learning for Vietnamese SMS spam detection using pre-trained PhoBERT," in Intelligent Data Engineering and Automated Learning – IDEAL 2024 (Lecture Notes in Computer Science, vol. 15346). Cham, Switzerland: Springer, 2024, pp. 254–264, doi: 10.1007/978-3-031-77731-8_24.
```
