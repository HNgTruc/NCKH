# pham-2016-vi-sms-spam: Content-based Approach for Vietnamese Spam SMS Filtering

Claude điền từ toàn văn bản arXiv (1705.04003v1, 4 trang) ngày 04/11/2026. Số trang trong phiếu là số trang của bản arXiv. Bản đăng ở IALP 2016 nằm ở tr. 41-44. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Thai-Hoang Pham (FPT Technology Research Institute), Phuong Le-Hong (ĐH Khoa học Tự nhiên, ĐHQG Hà Nội) |
| Năm | 2016 |
| Tên tạp chí hoặc hội nghị | 2016 International Conference on Asian Language Processing (IALP), IEEE, tr. 41-44 |
| DOI hoặc link chính thức | [10.1109/IALP.2016.7875930](https://doi.org/10.1109/IALP.2016.7875930). Bản mở: [arXiv 1705.04003](https://arxiv.org/abs/1705.04003) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra được. CORE chặn truy cập tự động, Trúc tra tay trên [CORE portal](https://portal.core.edu.au/conf-ranks) |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | SMS rác là vấn đề lớn ở Việt Nam vì có các gói tin nhắn trả trước rất rẻ. Bài dẫn báo cáo năm 2015 của BKAV: mỗi ngày có 13,9 triệu tin rác, cứ hai người thì một người từng nhận (tr. 1). Người dùng có thể mất tiền khi gọi tới số tính cước cao, đăng ký dịch vụ đắt hoặc vào trang độc hại (tr. 1) |
| Khoảng trống tác giả muốn giải quyết | Tiếng Việt đã có nghiên cứu lọc email rác nhưng chưa có nghiên cứu nào về SMS. Công cụ tách từ tiếng Việt có sẵn không hợp với SMS vì tin nhắn viết tắt, sai chính tả, dùng biểu tượng cảm xúc (tr. 1-2) |
| Mục tiêu | Xây hệ thống đầu tiên lọc SMS rác tiếng Việt dựa trên nội dung tin nhắn (tr. 1) |
| Câu hỏi hoặc giả thuyết | Bài không nêu câu hỏi nghiên cứu tường minh. Các thí nghiệm lần lượt so sánh: có và không có tiền xử lý, BoW và TF-IDF, năm bộ phân loại (tr. 3) |
| Đối tượng | Tin nhắn SMS tiếng Việt, phân loại 2 lớp: spam và legitimate (tr. 3). Trong code công khai, nhãn là Spam và Ham |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | 6.599 tin gán nhãn tay, lấy từ Viettel và Vinaphone: 5.557 tin hợp lệ, 1.042 tin rác (tr. 3). Khoảng 70% tin rác do chính nhà mạng gửi và có thẻ như [QC], [TB] (tr. 2-3). Bộ dữ liệu do nhóm CyRadar cung cấp (tr. 4). Bài ghi "made available for research purpose" tại github.com/pth1993 (tr. 3). Ngày 04/11/2026 Claude mở repo [vie-spam-sms-filtering](https://github.com/pth1993/vie-spam-sms-filtering): thư mục gốc chỉ có code, không có file giấy phép. Thư mục src/ chỉ có file `data_sample` gồm 10 tin mẫu, không có bộ 6.599 tin |
| Đặc trưng, đầu vào | Gom 6 loại thực thể thành thẻ: ngày, số điện thoại, đường link, tiền, biểu tượng cảm xúc, số. Tách từ bằng phương pháp ghép âm tiết hay đi cùng nhau (collocation), không cần dữ liệu huấn luyện trước. Biểu diễn bằng BoW hoặc TF-IDF, chọn đặc trưng theo tần suất văn bản, thêm đặc trưng độ dài tin (tr. 2, 4) |
| Phương pháp, mô hình | Mô hình cơ sở là luật bắt thẻ [QC*], (QC*), [TB*], (TB*). Các mô hình học máy: Naive Bayes, SVM, Logistic Regression, Decision Tree, kNN (tr. 2-3) |
| Chỉ số đánh giá | Kiểm định chéo 5 lần (5-fold cross-validation). Đo True Positive Rate, True Negative Rate, False Positive Rate, False Negative Rate, với lớp dương là spam (tr. 3) |
| Kết quả chính (số liệu kèm trang, bảng) | Luật bắt thẻ chỉ bắt được 69,76% tin rác (Bảng I, tr. 3). Tiền xử lý tăng TPR của SVM từ 91,79% lên 93,40% (Bảng II). BoW tốt hơn TF-IDF: TPR 93,40% so với 84,66% (Bảng III). Naive Bayes có TPR cao nhất (95,15%) nhưng FPR 3,75%, nên tác giả chọn SVM (Bảng IV, tr. 3-4). Hệ thống cuối: TPR 93,91%, FPR 0,45% (Bảng V, tr. 4) |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài đầu tiên về SMS rác tiếng Việt, nên làm mốc so sánh tốt. Tác giả giải thích rõ vì sao chặn nhầm tin hợp lệ (FPR) nguy hiểm hơn bỏ sót tin rác (tr. 3). Bước gom thực thể (link, số điện thoại, tiền) dùng lại được cho bước ẩn danh của đề tài.

Hạn chế: Chỉ có 2 lớp. Tin rác gộp cả quảng cáo của nhà mạng (khoảng 70%) lẫn các loại khác, không tách riêng tin lừa đảo. Dữ liệu cũ, chỉ từ hai nhà mạng, nên dễ bị sampling bias và historical bias. Dùng kiểm định chéo, không có tập kiểm tra tách theo thời gian. Không báo F1 hay precision cho từng lớp.

Dùng cho mục nào của thuyết minh: Mục 8.3 (nghiên cứu trong nước, mốc đầu tiên). Mục 9, làm bằng chứng cho khoảng trống "chưa tách tin lừa đảo khỏi tin quảng cáo". Mục 12, tham khảo cách gom thực thể và lý do chọn chỉ số. Số liệu BKAV 2015 ở tr. 1 là nguồn thứ cấp và đã cũ, không dùng cho mục 9.

## Trích dẫn IEEE

```
[n] T.-H. Pham and P. Le-Hong, "Content-based approach for Vietnamese spam SMS filtering," in Proc. 2016 Int. Conf. Asian Lang. Process. (IALP), 2016, pp. 41–44, doi: 10.1109/IALP.2016.7875930.
```
