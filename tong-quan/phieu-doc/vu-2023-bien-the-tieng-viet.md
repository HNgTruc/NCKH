# vu-2023-bien-the-tieng-viet: Evaluating the Efficiency of Vietnamese SMS Spam Detection Techniques

Claude điền từ toàn văn PDF (tr. 30-37) ngày 04/11/2026. Trang isj.vn không hiện nút tải, PDF lấy theo link OpenAlex chỉ tới: isj.vn/index.php/journal_STIS/article/download/932/303. Bài RIVF 2023 cùng nhóm không mở được toàn văn (IEEE, không truy cập mở), chỉ đối chiếu tóm tắt qua OpenAlex. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Vu Minh Tuan, Nguyen Xuan Thang (Trường Đại học Hà Nội), Tran Quang Anh (Học viện Công nghệ Bưu chính Viễn thông) (tr. 30, 37) |
| Năm | 2023 (nhận bài 08/03/2023, phản biện 1 chấp nhận 07/06/2023, phản biện 2 chấp nhận 05/06/2023, tr. 30) |
| Tên tạp chí hoặc hội nghị | Journal of Science and Technology on Information Security (Tạp chí Khoa học và Công nghệ trong lĩnh vực An toàn thông tin), ISSN 2615-9570, No. 1.CS (18) 2023, tr. 30-37 |
| DOI hoặc link chính thức | [10.54654/isj.v1i18.932](https://doi.org/10.54654/isj.v1i18.932). [Trang bài](https://isj.vn/index.php/journal_STIS/article/view/932). [PDF](https://isj.vn/index.php/journal_STIS/article/download/932/303) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra danh mục tạp chí HĐGSNN 2025 và SCImago] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | SMS phổ biến vì rẻ và hiệu quả, kéo theo tin rác. Bài dẫn số liệu của Cục An toàn thông tin (Bộ TT&TT): nhà mạng được yêu cầu chặn khoảng 9,6 triệu tin rác chỉ trong một tuần Tết 2022 (tr. 30). Câu này không có số tài liệu tham khảo |
| Khoảng trống tác giả muốn giải quyết | Hiệu quả của các phương pháp phụ thuộc ngôn ngữ dữ liệu. Với ngôn ngữ có nhiều biến thể như tiếng Việt (có dấu, không dấu), chưa rõ các kỹ thuật hoạt động ra sao trên từng biến thể (tr. 30-31). Ít công trình về SMS rác tiếng Việt (tr. 31) |
| Mục tiêu | Đánh giá SVM, NB, RF, CNN, LSTM trên ba dạng dữ liệu tiếng Việt: bản gốc, bản không dấu, bản có dấu đầy đủ (tr. 31) |
| Câu hỏi hoặc giả thuyết | Bài không nêu tường minh |
| Đối tượng | SMS tiếng Việt, 2 lớp spam và ham (lớp đầu ra có 2 nơ-ron "spam" và "ham", tr. 34) |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Bộ gốc (dataset 1): khoảng 10.000 tin rác do VNCERT cung cấp và 6.000 tin hợp lệ từ tác giả và tình nguyện viên. Phần lớn tin rác không dấu, toàn bộ tin hợp lệ có dấu đầy đủ (tr. 34). Dataset 2: bỏ dấu toàn bộ bằng thư viện unidecode. Dataset 3: tình nguyện viên thêm dấu bằng tay cho tin không dấu, có hai lớp kiểm soát (tr. 32, 34). Chia 70% huấn luyện, 15% kiểm định, 15% kiểm tra, đồng thời ghi dùng kiểm định chéo 10 lần (tr. 35). Bài không nêu thời gian thu, cách gán nhãn, có công khai dữ liệu hay không |
| Đặc trưng, đầu vào | Làm sạch, đưa về dạng chung (ví dụ [Q.C], [QC], (QC), quảng cáo, quang cao thành QC), bỏ 1.942 từ dừng, tách từ (tr. 32-33). TF-IDF cho học máy truyền thống, PhoBERT làm lớp nhúng cho CNN và LSTM (tr. 33). Tr. 33 lại ghi mô hình truyền thống dùng TF để chọn đặc trưng, không thống nhất với TF-IDF |
| Phương pháp, mô hình | SVM, Naive Bayes, Random Forest (TF-IDF). CNN và LSTM có lớp nhúng PhoBERT (tr. 33-34, Hình 1, 2) |
| Chỉ số đánh giá | Accuracy, precision, recall (tr. 34). Không có F1 |
| Kết quả chính (số liệu kèm trang, bảng) | Accuracy trên dataset 1 / 2 / 3: LSTM 95,66 / 94,89 / 97,77. CNN 95,03 / 95,56 / 96,04. RF 87,58 / 88,32 / 88,55. SVM 85,43 / 87,43 / 87,9. NB 79,77 / 81,15 / 81,23 (Bảng 1, tr. 35). Tác giả kết luận PhoBERT hiệu quả hơn với dữ liệu có dấu (tr. 35) |

Đối chiếu với bài RIVF 2023 (Vu Minh Tuan, Do Thuy Duong, Tran Quang Anh, "Proposing Appropriate SMS Spam Detection Approaches for Variations of the Vietnamese Language", DOI 10.1109/RIVF60135.2023.10471859): tóm tắt trên OpenAlex dùng cùng 5 thuật toán, 3 bộ dữ liệu và cùng hai con số 97,77% (LSTM, bản có dấu) và 95,56% (CNN + PhoBERT, bản không dấu). Đồng tác giả thứ hai khác nhau. Chưa đọc toàn văn bài RIVF nên chưa biết hai bài khác nhau ở đâu. [TODO: Trúc tìm toàn văn RIVF qua thư viện trường rồi so sánh]

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài duy nhất đã đọc thử có hệ thống ảnh hưởng của dấu thanh lên mô hình SMS rác tiếng Việt. Có số liệu VNCERT cung cấp tin rác. Ghi nhận tin rác thường không dấu để tiết kiệm ký tự (tr. 32), đúng đặc điểm tin lừa đảo đề tài sẽ gặp. Cách đưa các biến thể "[QC]", "quang cao" về một dạng (tr. 32) dùng lại được.

Hạn chế: Chỉ 2 lớp, không tách lừa đảo khỏi quảng cáo. Dữ liệu bị lệch nguồn rõ: tin rác phần lớn không dấu, tin hợp lệ có dấu toàn bộ (tr. 34). Ví dụ: ở dataset 1, mô hình chỉ cần học "không dấu thì là rác" cũng đạt điểm cao, nên con số trên dataset 1 không cho biết mô hình hiểu nội dung. Dataset 3 do tình nguyện viên thêm dấu, không phải tin thật. Mô tả chia tập mâu thuẫn (70/15/15 và kiểm định chéo 10 lần). Không báo F1, không báo theo từng lớp. Nhóm truyền thống và nhóm học sâu khác cả biểu diễn lẫn bộ phân loại, nên không tách được tác dụng của PhoBERT. Dữ liệu không công khai. Bài RIVF cùng nhóm có số liệu trùng, cần làm rõ trước khi trích cả hai.

Dùng cho mục nào của thuyết minh: Mục 8.3. Mục 9, thêm một bằng chứng cho khoảng trống "chỉ 2 lớp" và "dữ liệu không công khai". Mục 12, ví dụ cụ thể về bias do nguồn dữ liệu (dấu thanh trùng với nhãn), từ đó đề tài cần kiểm tra tỉ lệ không dấu theo từng nhãn. Số 9,6 triệu tin rác trong tuần Tết 2022 cần lần về thông cáo gốc của Cục An toàn thông tin, chưa dùng thẳng cho mục 9.

## Trích dẫn IEEE

```
[n] M. T. Vu, X. T. Nguyen, and Q. A. Tran, "Evaluating the efficiency of Vietnamese SMS spam detection techniques," J. Sci. Technol. Inf. Secur., vol. 1, no. 18, pp. 30–37, 2023, doi: 10.54654/isj.v1i18.932.
```
