# vu-2022-phobert-dnn: Vietnamese SMS Spam Detection with Deep Learning and Pre-trained Language Model

Claude điền từ toàn văn PDF trên VJOL (tr. 71-75) ngày 04/11/2026. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Vu Minh Tuan, Nguyen Xuan Thang (Trường Đại học Hà Nội), Tran Quang Anh (Học viện Công nghệ Bưu chính Viễn thông) |
| Năm | 2022 (nhận bài 31/10/2021, chấp nhận 11/5/2022, tr. 71) |
| Tên tạp chí hoặc hội nghị | Journal of Science and Technology on Information and Communications (Tạp chí Khoa học Công nghệ Thông tin và Truyền thông), No. 02 (CS.01) 2022, tr. 71-75 |
| DOI hoặc link chính thức | Không thấy DOI. [Trang bài trên VJOL](https://vjol.info.vn/3126-3445/article/view/188283) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra danh mục tạp chí HĐGSNN 2025 và SCImago] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | SMS vẫn là kênh quảng cáo hiệu quả, kéo theo SMS rác. Người dùng bị trừ cước, bị lừa đảo trực tuyến (online phishing) hoặc nhiễm mã độc khi làm theo tin nhắn (tr. 71) |
| Khoảng trống tác giả muốn giải quyết | Các mô hình SMS rác tiếng Việt trước đó dùng đặc trưng chọn tay và bộ phân loại truyền thống, kém hiệu quả khi kẻ gửi rác liên tục đổi cách viết (tr. 72). Mô hình BERT gốc học trên tiếng Anh nên không hợp với tiếng Việt (tr. 72) |
| Mục tiêu | Đề xuất mô hình mạng nơ-ron sâu (DNN) kết hợp PhoBERT để phát hiện SMS rác tiếng Việt (tr. 71) |
| Câu hỏi hoặc giả thuyết | Bài không nêu |
| Đối tượng | SMS tiếng Việt, 2 lớp: spam (gần 1) và legitimate (gần 0) (tr. 74). Lừa đảo chỉ được nhắc ở phần mở đầu như một tác hại của tin rác (tr. 71), không phải một nhãn riêng |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | 5.113 tin tiếng Việt: 52% spam, 48% hợp lệ. Thu từ người dùng trên nhiều hệ điều hành và thiết bị, chỉ lấy tin gửi qua mạng viễn thông (tr. 72). Bài không nêu khoảng thời gian thu thập, cách gán nhãn, có công khai dữ liệu hay không |
| Đặc trưng, đầu vào | Xóa đường link, số điện thoại, ký tự vô nghĩa. Tách từ bằng RDRSegmenter (VnCoreNLP). Vector PhoBERT 768 chiều cộng 2 đặc trưng đã chuẩn hóa: số từ và số ký tự, tổng 770 chiều (tr. 73) |
| Phương pháp, mô hình | DNN 4 lớp ẩn có Dropout, huấn luyện 10 epoch. So sánh với SVM, Naive Bayes, kNN và CNN (tr. 73-74) |
| Chỉ số đánh giá | Accuracy, precision, recall (Bảng 1, tr. 74). Không có F1 |
| Kết quả chính (số liệu kèm trang, bảng) | DNN + PhoBERT: accuracy 0,995, precision 1,0, recall 0,99. CNN: accuracy 0,97. SVM: 0,96. NB: 0,93. kNN: 0,89 (Bảng 1, tr. 74). Các mô hình được thử "with the same training and validation dataset" (tr. 74). Bài không nêu tỉ lệ chia tập và không nhắc tới tập kiểm tra riêng |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài trong nước sớm dùng PhoBERT cho SMS rác. Có so sánh với nhiều mô hình truyền thống. Mô tả rõ kiến trúc và cách ghép đặc trưng độ dài với vector PhoBERT.

Hạn chế: Chỉ có 2 lớp, gộp tin lừa đảo vào chung với tin rác. Dữ liệu nhỏ (5.113 tin), không công khai, không mô tả cách gán nhãn và độ đồng thuận giữa người gán. Bài không nói rõ có tập kiểm tra riêng hay không, nên con số 99,5% khó so sánh. Không báo F1. Không kiểm tra trùng lặp tin nhắn giữa tập huấn luyện và tập đánh giá.

Dùng cho mục nào của thuyết minh: Mục 8.3, làm bằng chứng đã có người dùng PhoBERT cho SMS rác tiếng Việt, nên đề tài không nhận "dùng PhoBERT" là điểm mới. Mục 9, cho khoảng trống "chỉ có 2 lớp" và "dữ liệu không công khai". Mục 12, làm lý do để đề tài báo F1 từng lớp và tách riêng tập kiểm tra.

## Trích dẫn IEEE

```
[n] M. T. Vu, X. T. Nguyen, and Q. A. Tran, "Vietnamese SMS spam detection with deep learning and pre-trained language model," J. Sci. Technol. Inf. Commun., no. 02 (CS.01), pp. 71–75, 2022.
```
