# nguyen-2020-phobert: PhoBERT: Pre-trained Language Models for Vietnamese

Claude điền từ toàn văn PDF trên ACL Anthology (tr. 1037-1042) ngày 04/11/2026. Thông tin giấy phép lấy từ README trên GitHub vì bài không nêu. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Dat Quoc Nguyen (VinAI Research), Anh Tuan Nguyen (NVIDIA, làm khi thực tập ở VinAI) (tr. 1037) |
| Năm | 2020 |
| Tên tạp chí hoặc hội nghị | Findings of the Association for Computational Linguistics: EMNLP 2020, tr. 1037-1042, ACL |
| DOI hoặc link chính thức | [10.18653/v1/2020.findings-emnlp.92](https://doi.org/10.18653/v1/2020.findings-emnlp.92). [ACL Anthology](https://aclanthology.org/2020.findings-emnlp.92/). Mã và mô hình: [github.com/VinAIResearch/PhoBERT](https://github.com/VinAIResearch/PhoBERT) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra CORE portal. Lưu ý Findings là tuyển tập đi kèm, có thể không mang hạng của EMNLP chính] |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Mô hình BERT thành công chủ yếu với tiếng Anh. Với tiếng Việt có hai vấn đề: dữ liệu tiền huấn luyện chỉ có Wikipedia tiếng Việt, nhỏ (khoảng 1GB) và không đại diện cho cách dùng ngôn ngữ chung; các mô hình có sẵn không phân biệt âm tiết với từ, vì tiếng Việt dùng dấu cách để tách âm tiết. Ví dụ "Tôi là một nghiên cứu viên" có 6 âm tiết nhưng 4 từ (tr. 1037) |
| Khoảng trống tác giả muốn giải quyết | Chưa có mô hình ngôn ngữ đơn ngữ quy mô lớn công khai cho tiếng Việt học trên dữ liệu đã tách từ (tr. 1037-1038) |
| Mục tiêu | Huấn luyện và công bố PhoBERT bản base và large, đánh giá trên 4 tác vụ tiếng Việt (tr. 1037-1038) |
| Câu hỏi hoặc giả thuyết | Mô hình đơn ngữ học trên dữ liệu mức từ sẽ tốt hơn mô hình đa ngữ XLM-R với các tác vụ tiếng Việt (tr. 1037-1038, 1040) |
| Đối tượng | Văn bản tiếng Việt chuẩn. Tác vụ: gán nhãn từ loại (POS), phân tích cú pháp phụ thuộc, nhận dạng thực thể (NER), suy luận ngôn ngữ (NLI) (tr. 1038). Không có tác vụ phân loại tin nhắn hay phát hiện rác |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Dữ liệu tiền huấn luyện: 20GB văn bản chưa nén, gồm Wikipedia tiếng Việt (khoảng 1GB) và khoảng 19GB tin tức, lọc trùng từ một kho tin tức 50GB (tr. 1038). Sau tách từ: khoảng 145 triệu câu, khoảng 3 tỉ từ (tr. 1038). Dữ liệu đánh giá: VLSP 2013 (POS), VnDT v1.1 (cú pháp), VLSP 2016 (NER), XNLI v1.0 phần tiếng Việt (NLI). Số mẫu ở Bảng 1 (tr. 1038) |
| Đặc trưng, đầu vào | Cần tách từ (word segmentation) trước. Tác giả dùng RDRSegmenter của VnCoreNLP để tách từ và tách câu cho dữ liệu tiền huấn luyện, rồi dùng fastBPE với bộ từ vựng 64.000 đơn vị con (subword) (tr. 1038). Với NLI, văn bản cũng được tách từ bằng RDRSegmenter trước khi đưa vào (tr. 1039). README trên GitHub ghi đầu vào "must be already word-segmented". Độ dài tối đa: 256 đơn vị con (tr. 1038). Trung bình 24,4 đơn vị con mỗi câu (tr. 1038) |
| Phương pháp, mô hình | Kiến trúc giống BERT-base và BERT-large, cách tiền huấn luyện theo RoBERTa (tr. 1038). Base 135 triệu tham số, large 370 triệu (tr. 1040). Huấn luyện 40 epoch trên 4 GPU V100: base khoảng 540.000 bước trong 3 tuần, large 1,08 triệu bước trong 5 tuần (tr. 1038). Tinh chỉnh (fine-tuning) bằng AdamW, learning rate 1e-5, batch 32, tối đa 30 epoch, dừng sớm sau 5 epoch không cải thiện, mỗi kết quả là trung bình 5 lần chạy (tr. 1039) |
| Chỉ số đánh giá | Accuracy (POS, NLI), LAS/UAS (cú pháp), F1 (NER) (Bảng 2, 3, tr. 1039-1040) |
| Kết quả chính (số liệu kèm trang, bảng) | POS: PhoBERT-large 96,8%, base 96,7%, XLM-R large 96,3% (Bảng 2, tr. 1039). Cú pháp: PhoBERT-base LAS/UAS 78,77/85,22, cao hơn XLM-R base 76,46/83,10 (Bảng 2). NER: PhoBERT-large F1 94,7, base 93,6, XLM-R large 92,8 (Bảng 3, tr. 1040). NLI: PhoBERT-large 80,0%, base 78,5%, XLM-R large 79,7% (Bảng 3). PhoBERT học trên 20GB tiếng Việt, ít hơn khoảng 7 lần so với 137GB tiếng Việt của XLM-R, vẫn tốt hơn (tr. 1040) |

Giấy phép mô hình: bài không nêu. Theo README GitHub (Claude xem ngày 04/11/2026): `vinai/phobert-base` và `vinai/phobert-large` dùng giấy phép MIT, `vinai/phobert-base-v2` dùng GNU AGPL-3.0. Bản base-v2 học thêm 120GB văn bản OSCAR-2301 ngoài 20GB ban đầu. Cả ba bản có độ dài tối đa 256. [TODO: Trúc mở README kiểm tra lại trước khi ghi vào mục 12]

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là mô hình tiếng Việt được dùng nhiều nhất và là mô hình chính của đề tài. Bài giải thích rõ vì sao cần tách từ, kèm ví dụ dễ hiểu. Công bố mô hình kèm giấy phép mở (MIT cho bản base, large), dùng được ngay với thư viện transformers. Giới hạn 256 đơn vị con đủ cho SMS, vì một tin SMS thường ngắn.

Hạn chế: Bài không thử tác vụ phân loại văn bản nào, nên không có bằng chứng trực tiếp PhoBERT tốt cho tin nhắn. Dữ liệu tiền huấn luyện là Wikipedia và tin tức, viết chuẩn, có dấu. Tin rác và lừa đảo tiếng Việt thường không dấu, viết tắt, chèn ký tự (vu-2023-nhung-tu tr. 13, Bảng 1; vu-2023-bien-the-tieng-viet tr. 32). Bài nguyen-2023-visobert cho thấy PhoBERT giảm mạnh hơn ViSoBERT khi bỏ hết dấu (Bảng 8, tr. 5204), và tokenizer của PhoBERT biến biểu tượng cảm xúc thành <unk> (Bảng 1, tr. 5195). Bước tách từ thêm một công cụ (RDRSegmenter trong VnCoreNLP) vào quy trình, nhóm cần học thêm cách cài và chạy.

Dùng cho mục nào của thuyết minh: Mục 8.2, giới thiệu mô hình chính. Mục 12, mô tả tiền xử lý (tách từ bằng RDRSegmenter), độ dài tối đa 256, giấy phép MIT của bản base. Mục 9, kết hợp với nguyen-2023-visobert để nêu câu hỏi "PhoBERT có hợp với tin nhắn không dấu không".

## Trích dẫn IEEE

```
[n] D. Q. Nguyen and A. T. Nguyen, "PhoBERT: Pre-trained language models for Vietnamese," in Findings Assoc. Comput. Linguistics: EMNLP 2020, 2020, pp. 1037–1042, doi: 10.18653/v1/2020.findings-emnlp.92.
```
