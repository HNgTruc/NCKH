# vu-2023-nhung-tu: Evaluation of Word Embedding Techniques for the Vietnamese SMS Spam Detection Model

Claude điền từ toàn văn PDF trên VJOL (tr. 12-16) ngày 04/11/2026. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Vu Minh Tuan, Do Thuy Duong (Trường Đại học Hà Nội), Tran Quang Anh (Học viện Công nghệ Bưu chính Viễn thông) |
| Năm | 2023 (nhận bài 8/2023, chấp nhận 9/2023, tr. 12) |
| Tên tạp chí hoặc hội nghị | Journal of Science and Technology on Information and Communications (Tạp chí Khoa học Công nghệ Thông tin và Truyền thông), No. 03 (CS.01) 2023, tr. 12-16 |
| DOI hoặc link chính thức | Không thấy DOI. [Trang bài trên VJOL](https://vjol.info.vn/3126-3445/article/view/188182) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra danh mục tạp chí HĐGSNN 2025 và SCImago] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | SMS rác tiếng Việt ngày càng nhiều. Cách biểu diễn từ (word embedding) ảnh hưởng tới chất lượng mô hình phát hiện (tr. 12) |
| Khoảng trống tác giả muốn giải quyết | Chưa có nghiên cứu so sánh tác động của các kỹ thuật biểu diễn từ đối với phát hiện SMS rác tiếng Việt (tr. 13) |
| Mục tiêu | So sánh BoW, TF-IDF với Word2Vec, fastText, GloVe, PhoBERT cho phát hiện SMS rác tiếng Việt (tr. 12) |
| Câu hỏi hoặc giả thuyết | Bài không nêu tường minh |
| Đối tượng | SMS tiếng Việt, 2 lớp: spam và ham (tr. 13) |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tin rác: khoảng 50.000 tin, gồm khoảng 20.000 tin từ hệ thống bẫy (honeypot) 32 số điện thoại trên thiết bị sim-bank, khoảng 25.000 tin do VNCERT cung cấp, khoảng 5.000 tin do 30 tình nguyện viên gửi trong 3 tháng. Sau khi bỏ trùng còn khoảng 35.000 tin. Tin hợp lệ: 45.000 tin do 10 người tình nguyện gửi, còn khoảng 40.000 tin. Tỉ lệ tin không dấu: tin rác 35%, tin hợp lệ 5% (tr. 13, Bảng 1). Tóm tắt gọi đây là "private dataset" (tr. 12). Mọi thí nghiệm chạy trên bản có dấu. Chia 70% huấn luyện, 15% kiểm định, 15% kiểm tra (tr. 13). Bài không nêu cách gán nhãn |
| Đặc trưng, đầu vào | Làm sạch, đưa từ về dạng gốc (stemming), bỏ từ dừng, tách từ (tr. 13). Biểu diễn bằng BoW, TF-IDF, Word2Vec, GloVe, fastText, PhoBERT (tr. 13-14) |
| Phương pháp, mô hình | BoW và TF-IDF đi với Naive Bayes. Word2Vec, GloVe, fastText, PhoBERT đi với CNN (tr. 14) |
| Chỉ số đánh giá | Accuracy, precision, recall, F1 (tr. 15) |
| Kết quả chính (số liệu kèm trang, bảng) | PhoBERT + CNN tốt nhất: accuracy 0,968, precision 0,943, recall 0,939, F1 0,941. Word2Vec: accuracy 0,958, F1 0,921. fastText: 0,931 và 0,917. GloVe: 0,896 và 0,897. TF-IDF + NB: 0,932 và 0,899. BoW + NB: 0,913 và 0,885 (Bảng 3, tr. 15) |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Dữ liệu lớn, nhiều nguồn (honeypot, VNCERT, tình nguyện viên), mô tả rõ nguồn và tỉ lệ tin không dấu. Có chia tập kiểm tra riêng và báo đủ 4 chỉ số, kể cả F1. Cho thấy PhoBERT hơn TF-IDF khoảng 4 điểm F1 trên cùng dữ liệu (0,941 so với 0,899).

Hạn chế: Chỉ có 2 lớp. Không tách tin lừa đảo khỏi tin quảng cáo. Dữ liệu riêng, không công khai. Tin rác và tin hợp lệ đến từ nguồn khác nhau (bẫy, VNCERT, tình nguyện viên), nên mô hình có thể học theo nguồn thay vì nội dung. Ví dụ, gần như chỉ tin rác mới không dấu (35% so với 5%). So sánh chưa công bằng vì nhóm truyền thống dùng NB, nhóm hiện đại dùng CNN, khác cả cách biểu diễn lẫn bộ phân loại. Chỉ thử trên bản có dấu.

Dùng cho mục nào của thuyết minh: Mục 8.3. Mục 9, bằng chứng cho khoảng trống "chỉ có 2 lớp" và "dữ liệu không công khai". Mục 12, gợi ý dùng TF-IDF làm mô hình cơ sở và giữ cùng một bộ phân loại khi so sánh. Cũng là ví dụ về bias do nguồn dữ liệu để đưa vào phần bias.

## Trích dẫn IEEE

```
[n] M. T. Vu, T. D. Do, and Q. A. Tran, "Evaluation of word embedding techniques for the Vietnamese SMS spam detection model," J. Sci. Technol. Inf. Commun., no. 03 (CS.01), pp. 12–16, 2023.
```
