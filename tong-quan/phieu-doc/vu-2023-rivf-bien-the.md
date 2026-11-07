# vu-2023-rivf-bien-the: Proposing Appropriate SMS Spam Detection Approaches for Variations of the Vietnamese Language

Chỉ đọc tóm tắt. Claude điền ngày 06/11/2026. IEEE Xplore trả trang trống với truy cập tự động. Semantic Scholar và OpenAlex ghi bài "closed", không có bản mở. Tóm tắt lấy từ OpenAlex (dựng lại từ chỉ mục từ), tác giả và trang lấy từ Crossref. Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu. Trúc cần đọc toàn văn qua thư viện trường trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Vu Minh Tuan, Do Thuy Duong (Khoa CNTT, Trường Đại học Hà Nội), Tran Quang Anh (Học viện Công nghệ Bưu chính Viễn thông). Tên theo Crossref, đơn vị theo OpenAlex. Semantic Scholar ghi sai tác giả thứ hai là "Doan-Tung Duong" |
| Năm | 2023 (xuất bản 23/12/2023 theo Crossref) |
| Tên tạp chí hoặc hội nghị | 2023 RIVF International Conference on Computing and Communication Technologies (RIVF), tr. 1-5, IEEE |
| DOI hoặc link chính thức | [10.1109/RIVF60135.2023.10471859](https://doi.org/10.1109/RIVF60135.2023.10471859). [IEEE Xplore](https://ieeexplore.ieee.org/document/10471859) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. CORE portal chặn truy cập tự động (lỗi 403, 06/11/2026). [TODO: Trúc tra hạng RIVF trên CORE, ghi link] |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 06/11/2026. Trúc: [TODO: đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: đề xuất cách phát hiện SMS rác phù hợp với các dạng (biến thể) khác nhau của tiếng Việt |
| Khoảng trống tác giả muốn giải quyết | Bài không nêu (trong tóm tắt) |
| Mục tiêu | Tóm tắt: so sánh năm thuật toán trên ba bộ dữ liệu tiếng Việt để chọn cách phù hợp cho từng biến thể |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS rác tiếng Việt, bản có dấu đầy đủ và bản không dấu |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tóm tắt: ba bộ dữ liệu tiếng Việt, có bộ có dấu đầy đủ và bộ không dấu. Nguồn, số mẫu, số lớp, có công khai không: bài không nêu (trong tóm tắt). Bài cùng nhóm vu-2023-bien-the-tieng-viet dùng 2 lớp spam/ham và dữ liệu VNCERT (tr. 34 bài đó), nhưng chưa xác nhận được bài RIVF dùng cùng bộ |
| Đặc trưng, đầu vào | Tóm tắt: PhoBERT bổ trợ cho CNN và LSTM. Đặc trưng cho mô hình truyền thống: bài không nêu (trong tóm tắt) |
| Phương pháp, mô hình | SVM, Naive Bayes, Random Forest, CNN, LSTM, có PhoBERT (tóm tắt) |
| Chỉ số đánh giá | Accuracy (tóm tắt). Chỉ số khác: bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: LSTM và CNN có PhoBERT tốt hơn học máy truyền thống. LSTM cao nhất trên bộ có dấu đầy đủ, accuracy 97,77%. CNN và PhoBERT cao nhất trên bộ không dấu, accuracy 95,56% |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Bản hội nghị quốc tế (IEEE) của hướng nghiên cứu dấu thanh trong SMS rác tiếng Việt.

Hạn chế: Hai con số 97,77% và 95,56% trùng với Bảng 1 của bài ISJ 2023 cùng nhóm (vu-2023-bien-the-tieng-viet, tr. 35). Rất có thể hai bài báo cùng một kết quả. Chưa đọc toàn văn nên chưa biết số lớp, nguồn dữ liệu, có công khai không. Chỉ báo accuracy.

Dùng cho mục nào của thuyết minh: Mục 8.3, nếu cần nguồn quốc tế cho hướng "dấu thanh". Nên trích bài ISJ (đã đọc toàn văn) là chính. Chỉ trích bài RIVF khi đã đọc toàn văn và biết hai bài khác nhau ở đâu. Chưa dùng làm bằng chứng cho câu "chỉ 2 lớp".

## Trích dẫn IEEE

```
[n] M. T. Vu, T. D. Do, and Q. A. Tran, "Proposing appropriate SMS spam detection approaches for variations of the Vietnamese language," in Proc. 2023 RIVF Int. Conf. Comput. Commun. Technol. (RIVF), 2023, pp. 1–5, doi: 10.1109/RIVF60135.2023.10471859.
```
