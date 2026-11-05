# tran-2026-vi-sms-dataset: Vietnamese SMS Dataset with Quality Assurance (bộ dữ liệu trên Hugging Face)

Đây là bộ dữ liệu, không phải bài báo. Claude đọc trang bộ dữ liệu (README, QUICKSTART_GUIDE.md) và tải ba file CSV về kiểm tra ngày 06/11/2026, phiên bản commit `a90e2bd` (sửa lần cuối 07/08/2026). Các con số ở cột "Claude tự đếm" là do Claude chạy script đếm trên file đã tải, không lấy từ README.

README ghi bài báo đi kèm đăng ở IEEE Access năm 2026, nhưng phần tiếng Việt và tiếng Anh ghi hai tên bài khác nhau ("Vietnamese SMS Dataset with Quality Assurance" và "Quality-Assured Vietnamese SMS Phishing Dataset: Closed-Loop Human Adjudication Framework and Leakage-Controlled Transformer Benchmarking"). Tìm trên web ngày 06/11/2026 không thấy bài nào khớp. Vì vậy chỉ trích dẫn như một bộ dữ liệu, không trích như bài báo đã bình duyệt.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Trần Nguyễn Thái Tuấn, Lê Hoàng Khang, Nguyễn Minh Tài, Nguyễn Văn Thắng; cố vấn Mai Hoàng Đỉnh (theo README). README không nêu đơn vị |
| Năm | 2026 (tạo trên Hugging Face 03/08/2026) |
| Tên tạp chí hoặc hội nghị | Không có. Bộ dữ liệu đăng trên Hugging Face. Bài báo README nhắc tới: chưa tìm thấy |
| DOI hoặc link chính thức | [huggingface.co/datasets/trannguyenthaituan/vietnamese_sms_dataset](https://huggingface.co/datasets/trannguyenthaituan/vietnamese_sms_dataset) |
| Chỉ mục (Scopus/WoS), bằng chứng | Không áp dụng |
| Hạng Q hoặc CiteScore, IF | Không áp dụng |
| Lĩnh vực theo SCImago | Không áp dụng |
| Giấy phép | CC BY 4.0: được dùng, sửa, chia sẻ nếu ghi nguồn |
| Người đọc, ngày đọc | Claude, 06/11/2026. Trúc: [TODO: mở trang, đọc README, ghi ngày] |

## Nội dung

| Câu hỏi | README ghi | Claude tự đếm |
| --- | --- | --- |
| Bối cảnh và vấn đề | Phục vụ nghiên cứu phát hiện SMS rác và lừa đảo | |
| Khoảng trống tác giả muốn giải quyết | README không nêu | |
| Mục tiêu | Công bố bộ SMS tiếng Việt có kiểm soát chất lượng nhãn và kiểm soát rò rỉ giữa tập train và test | |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tin SMS thật, cộng đồng đóng góp có đồng ý, "không do AI sinh, không dịch". Dùng danh sách 50.000 URL độc hại của nhóm Chống Lừa Đảo làm tiêu chí đánh giá nhãn. 2.991 tin, 2 nhãn: `0` hợp lệ, `1` rác/lừa đảo. Train 2.394, test 597 | 2.991 dòng: 2.193 nhãn 0, 798 nhãn 1. Sau khi bỏ tin trùng nguyên văn còn 2.629 tin (1.918 nhãn 0, 711 nhãn 1). Ngày trong cột `date`: 28/05/2026 đến 03/08/2026 |
| Ẩn danh | Số điện thoại, số tài khoản, số tiền, con số, giờ, ngày thay bằng `[PHONE]`, `[BANK_ACC]`, `[MONEY]`, `[NUMBER]`, `[TIME]`, `[DATE]`. Kiểm tra tay mẫu ngẫu nhiên không thấy thông tin cá nhân sót | Trong 12 tin nhãn 1 xem ngẫu nhiên có 1 tin còn họ tên đầy đủ của một người |
| Tin quảng cáo nằm ở nhãn nào | README không nói | 351 tin hợp lệ (nhãn 0) có thẻ `[QC]` hoặc `(QC)` của nhà mạng. Chỉ 1 tin nhãn 1 có thẻ này. Nhãn 1 trong mẫu xem được phần lớn là lừa đảo: việc nhẹ lương cao, cờ bạc, giả ngân hàng, thuê tài khoản ngân hàng, đầu tư lãi cao |
| Đặc điểm văn bản | "Unaccented/accented" (bộ mẫu 300 tin) | 1.568 trong 2.991 tin không có chữ có dấu nào. Có tin bị chèn ký tự để né bộ lọc, ví dụ "NhHậẬnNLLuUôôn" |
| Phương pháp, mô hình | PhoBERT-base, SVM n-gram ký tự 3-5, SVM RBF, SVM tuyến tính, MLP, Logistic Regression, Multinomial Naive Bayes | |
| Chỉ số đánh giá | Accuracy, precision, recall, F1, khoảng tin cậy bootstrap 95%. 5-fold cross-validation sau khi lọc tin gần trùng (Jaccard ≥ 0,85) | |
| Kết quả chính | F1: PhoBERT-base 96,63% ± 1,05; SVM ký tự 93,40%; Logistic Regression 88,28%; Naive Bayes 78,32% (bảng benchmark trong README) | Không chạy lại |
| Rò rỉ train/test | README ghi tập test "được thiết kế nhằm hạn chế rò rỉ" | 47 tin trong `test.csv` trùng nguyên văn với tin trong `train.csv` |
| Đạo đức | Hội đồng đạo đức xác nhận miễn thẩm định, mã `IRB-2026-NLP-0428`, người đóng góp đồng ý tự nguyện | Không kiểm tra được mã này |

## Nhận xét của nhóm

Ưu điểm: bộ SMS tiếng Việt công khai đầu tiên tìm được có giấy phép rõ (CC BY 4.0), dữ liệu năm 2026, đã ẩn danh bằng thẻ thay thế, có nhiều tin không dấu và tin bị viết biến dạng. Có sẵn kết quả của 7 mô hình để so sánh.

Hạn chế: chỉ 2 nhãn, và cách xếp tin quảng cáo ngược với pham-2016-vi-sms-spam. Bộ này xếp tin quảng cáo nhà mạng vào "hợp lệ", trong khi ở pham-2016 khoảng 70% tin rác là quảng cáo nhà mạng. Chưa có bài báo bình duyệt đi kèm. Tên bài trong README không thống nhất. Cách thu thập và người đóng góp không được mô tả cụ thể. Dữ liệu chỉ trong khoảng 2 tháng. Có 362 dòng trùng nguyên văn, 47 tin test trùng train, nên kết quả benchmark trên `train.csv` và `test.csv` gốc có thể cao hơn thực tế. Ẩn danh chưa sạch hoàn toàn.

Dùng cho mục nào của thuyết minh:

- Mục 8: nghiên cứu trong nước gần nhất, bằng chứng cho khoảng trống "chỉ 2 nhãn". Việc hai bộ dữ liệu xếp tin quảng cáo vào hai lớp trái nhau là lý do cho bộ 3 nhãn.
- Mục 12: nguồn dữ liệu của thử nghiệm sơ bộ và của đề tài. Phải tự bỏ tin trùng trước khi chia tập, và kiểm tra lại ẩn danh.
- Mục 12.5: bias về nguồn (không rõ người đóng góp là ai, chỉ 2 tháng).

## Trích dẫn IEEE

Mẫu IEEE cho bộ dữ liệu trực tuyến. Số [n] đánh khi chạy skill `trich-dan-ieee`.

```
[n] N. T. T. Tran, H. K. Le, M. T. Nguyen, V. T. Nguyen, and H. D. Mai, "Vietnamese SMS Dataset with Quality Assurance," Hugging Face, 2026. [Online]. Available: https://huggingface.co/datasets/trannguyenthaituan/vietnamese_sms_dataset (accessed Nov. 6, 2026).
```
