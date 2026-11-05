# nguyen-2023-visobert: ViSoBERT: A Pre-Trained Language Model for Vietnamese Social Media Text Processing

Claude điền từ toàn văn PDF trên ACL Anthology (tr. 5191-5207) ngày 04/11/2026. Điều khoản sử dụng đối chiếu thêm trang mô hình trên Hugging Face. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Quoc-Nam Nguyen, Thang Chau Phan (đóng góp ngang nhau), Duc-Vu Nguyen, Kiet Van Nguyen. Trường ĐH Công nghệ Thông tin, ĐHQG TP.HCM (tr. 5191) |
| Năm | 2023 |
| Tên tạp chí hoặc hội nghị | Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023, hội nghị chính), tr. 5191-5207, ACL |
| DOI hoặc link chính thức | [10.18653/v1/2023.emnlp-main.315](https://doi.org/10.18653/v1/2023.emnlp-main.315). [ACL Anthology](https://aclanthology.org/2023.emnlp-main.315/). Mô hình: [huggingface.co/uitnlp/visobert](https://huggingface.co/uitnlp/visobert) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra hạng EMNLP trên CORE portal, ghi link] |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Các mô hình tiếng Việt có sẵn (PhoBERT, viBERT, vELECTRA) học trên văn bản chuẩn. Văn bản mạng xã hội có teencode, từ không chuẩn, thiếu dấu, biểu tượng cảm xúc (emoji), nên các mô hình này xử lý kém (tr. 5191-5192) |
| Khoảng trống tác giả muốn giải quyết | Chưa có mô hình ngôn ngữ đơn ngữ tiền huấn luyện riêng cho văn bản mạng xã hội tiếng Việt (tr. 5191). Tokenizer của các mô hình có sẵn xử lý kém văn bản mạng xã hội (tr. 5194) |
| Mục tiêu | Xây ViSoBERT cùng tokenizer riêng cho mạng xã hội tiếng Việt, đánh giá trên 5 tác vụ (tr. 5192) |
| Câu hỏi hoặc giả thuyết | Bài không nêu tường minh. Phần 5 phân tích ảnh hưởng của tỉ lệ che (masking rate), emoji, teencode, dấu thanh (tr. 5196-5199) |
| Đối tượng | Bình luận mạng xã hội tiếng Việt. 5 tác vụ: nhận dạng cảm xúc, phát hiện phát ngôn thù ghét, phân tích cảm xúc, phát hiện đánh giá rác (spam reviews, bộ ViSpamReviews), phát hiện đoạn thù ghét (Bảng 2, tr. 5195). Không có tác vụ SMS |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Dữ liệu tiền huấn luyện: bình luận từ trang Facebook đã xác minh (1/2016-12/2022, qua Graph API), kênh TikTok đã xác minh (1/2020-12/2022, qua Research API), kênh YouTube đã xác minh (1/2016-12/2022, qua Data API) (tr. 5193). Đã bỏ bình luận chứa link, tin rác lặp lại, bình luận chỉ có tên người dùng, giữ emoji. Sau làm sạch còn 1GB văn bản chưa nén (tr. 5193). Bài không nêu số câu hoặc số bình luận. Dữ liệu tiền huấn luyện "available only for research purposes" (tr. 5193). Bộ ViSpamReviews dùng để đánh giá: 14.306/1.590/3.974 mẫu, 4 lớp (Bảng 2, tr. 5195) |
| Đặc trưng, đầu vào | Tokenizer riêng xây bằng SentencePiece trên toàn bộ dữ liệu tiền huấn luyện, xử lý văn bản thô (tr. 5194). Từ vựng 15.000 (Bảng 3, tr. 5196), 15.002 (Bảng 6, tr. 5203). Có cần tách từ không: bài không nêu tường minh. Bài không nhắc RDRSegmenter hay VnCoreNLP. Ví dụ trên Hugging Face đưa thẳng văn bản thô vào tokenizer. Độ dài tối đa: Bảng 3 ghi 512 (tr. 5196), Bảng 6 ghi độ dài chuỗi lúc tiền huấn luyện là 128 (tr. 5203), lúc tinh chỉnh dùng 128 (tr. 5194). Khi đánh giá, không tiền xử lý dữ liệu (tr. 5194) |
| Phương pháp, mô hình | Kiến trúc kiểu XLM-R: 768 chiều ẩn, 12 lớp, 12 đầu chú ý, mục tiêu che từ (masked language) (tr. 5193). 97 triệu tham số (Bảng 3, tr. 5196). Tỉ lệ che 30% (tr. 5194, 5197). 1,2 triệu bước, batch 128, khoảng 3 ngày trên 2 GPU RTX 4090 (tr. 5194). Bài mâu thuẫn ở điểm học từ đầu hay học tiếp: tr. 5194 ghi "pretraining from scratch", phần Ethics Statement ghi dựa trên tiền huấn luyện một mô hình có sẵn là XLM-R (tr. 5200). Tinh chỉnh: batch 40, learning rate 2e-5, 10 epoch, AdamW (tr. 5194). So với viBERT, vELECTRA, PhoBERT base và large, mBERT, XLM-R, XLM-T, TwHIN-BERT, Bernice (Bảng 3, tr. 5196) |
| Chỉ số đánh giá | Accuracy, F1 có trọng số (WF1), F1 trung bình macro (MF1) (Bảng 2, tr. 5195). Kiểm định t ghép cặp, p < 0,01 cho kết quả cao nhất (Bảng 4, tr. 5196) |
| Kết quả chính (số liệu kèm trang, bảng) | Tác vụ đánh giá rác (ViSpamReviews, 4 lớp): ViSoBERT Acc 90,99, WF1 90,92, MF1 79,06. PhoBERT-base 89,83 / 89,75 / 76,18. PhoBERT-large 90,12 / 90,03 / 76,88 (Bảng 4, tr. 5196). MF1 của ViSoBERT cao hơn PhoBERT-large 2,18 điểm. Bảng 4 đánh dấu MF1 79,06 có ý nghĩa thống kê (p < 0,01) so với mô hình đứng thứ hai là TwHIN-BERT-large (77,28), không phải so với PhoBERT. Bỏ 100% dấu: MF1 của PhoBERT-large giảm 4,99 điểm xuống 71,89, ViSoBERT giảm 2,94 điểm xuống 76,12 (Bảng 8, tr. 5204). Chuẩn hóa teencode làm ViSoBERT giảm nhẹ trên tác vụ này (MF1 79,06 xuống 78,77, Bảng 7, tr. 5204), tác giả cho là vì tin rác hay lặp ký tự để kéo dài bình luận (tr. 5198). Tokenizer PhoBERT biến emoji thành <unk> (Bảng 1, tr. 5195) |

Điều khoản sử dụng mô hình: bài ghi ViSoBERT "available only for research purposes" (tóm tắt, tr. 5191). Trang Hugging Face (Claude xem ngày 04/11/2026) không có ô giấy phép, không thấy yêu cầu xin quyền truy cập. [TODO: Trúc kiểm tra lại trang Hugging Face và ghi điều khoản vào mục 12]

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Đăng ở EMNLP hội nghị chính. Có thử nghiệm trực tiếp trên dữ liệu thiếu dấu, teencode, emoji, đúng các đặc điểm của tin rác tiếng Việt. Ví dụ: tin "Tai khoan cua ban dang duoc dang nhap tren thiet bi khac..." trong vu-2024-tong-quan-tin-nhan-rac (Hình 6, tr. 73) hoàn toàn không dấu. Có kiểm định thống kê, không chỉ so số. Không cần tách từ nên quy trình đơn giản hơn PhoBERT.

Hạn chế: Không có tác vụ SMS. Mức chênh với PhoBERT trên ViSpamReviews nhỏ ở Accuracy (dưới 1 điểm), lớn hơn ở MF1. Chỉ cho phép dùng để nghiên cứu, đủ cho đề tài sinh viên nhưng không dùng được cho sản phẩm thương mại. Bài có chỗ không nhất quán (học từ đầu hay học tiếp từ XLM-R, độ dài tối đa 512 hay 128, chữ "micro F1" ở tr. 5196 trong khi bảng ghi macro F1). Dữ liệu tiền huấn luyện là bình luận mạng xã hội, chưa chắc giống văn phong SMS.

Dùng cho mục nào của thuyết minh: Mục 8.2, mô hình so sánh với PhoBERT. Mục 9, bằng chứng rằng văn bản không dấu làm PhoBERT giảm mạnh hơn (Bảng 8), nên câu hỏi "mô hình nào hợp với SMS lừa đảo tiếng Việt" còn mở. Mục 12, cân nhắc thêm ViSoBERT làm mô hình so sánh thứ hai và thêm thí nghiệm bỏ dấu.

## Trích dẫn IEEE

```
[n] Q.-N. Nguyen, T. C. Phan, D.-V. Nguyen, and K. V. Nguyen, "ViSoBERT: A pre-trained language model for Vietnamese social media text processing," in Proc. 2023 Conf. Empirical Methods Natural Lang. Process. (EMNLP), 2023, pp. 5191–5207, doi: 10.18653/v1/2023.emnlp-main.315.
```
