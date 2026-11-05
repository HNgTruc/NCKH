# liu-2021-spam-transformer: A Spam Transformer Model for SMS Spam Detection

Chỉ đọc tóm tắt. Claude điền ngày 04/11/2026 từ tóm tắt (lấy qua OpenAlex) và siêu dữ liệu Crossref. Bài là truy cập mở, nhưng IEEE Xplore chặn truy cập tự động (lỗi 420, trang HTML trả về rỗng), nên chưa đọc được toàn văn. Trường Đại học Ottawa có luận văn thạc sĩ cùng tên của tác giả đầu (Xiaoxu Liu, 2021, [handle 10393/42057](http://hdl.handle.net/10393/42057)). Đó là tài liệu khác, Claude chưa đọc và không dùng để điền phiếu này. Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Xiaoxu Liu, Haoye Lu, Amiya Nayak (School of Electrical Engineering and Computer Science, University of Ottawa, Canada). Đơn vị lấy từ OpenAlex |
| Năm | 2021 |
| Tên tạp chí hoặc hội nghị | IEEE Access, vol. 9, tr. 80253-80263 |
| DOI hoặc link chính thức | [10.1109/ACCESS.2021.3081479](https://doi.org/10.1109/ACCESS.2021.3081479). IEEE Xplore: [document 9433507](https://ieeexplore.ieee.org/document/9433507). Giấy phép bài: CC BY-NC-ND 4.0 (Crossref) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra IEEE Access trên SCImago, ghi link và hạng Q của năm 2021] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 04/11/2026. Trúc: [TODO: tải PDF từ IEEE Xplore bằng trình duyệt, đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: SMS rác tăng theo mức dùng SMS, cần phương pháp phát hiện tốt hơn |
| Khoảng trống tác giả muốn giải quyết | Bài không nêu (trong tóm tắt) |
| Mục tiêu | Tóm tắt: đề xuất một mô hình Transformer có sửa đổi (modified Transformer) để phát hiện SMS rác |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS tiếng Anh, 2 lớp spam và ham. Thử thêm trên tweet rác |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tóm tắt: SMS Spam Collection v.1 (bộ của almeida-2011-sms-spam-collection) và bộ Twitter Spam Detection Competition của UtkMl. Số mẫu, cách chia tập: bài không nêu (trong tóm tắt) |
| Đặc trưng, đầu vào | Bài không nêu (trong tóm tắt) |
| Phương pháp, mô hình | Tóm tắt: Transformer có sửa đổi, so với "a series of established machine learning classifiers and state-of-the-art SMS spam detection approaches". Tên từng mô hình so sánh: bài không nêu trong tóm tắt |
| Chỉ số đánh giá | Tóm tắt nêu accuracy, recall, F1-score |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: trên SMS Spam Collection v.1, mô hình đề xuất đạt accuracy 98,92%, recall 0,9451, F1 0,9613, tốt nhất trong các mô hình so sánh. Trên bộ Twitter cũng cho kết quả tốt. [TODO: Trúc ghi số bảng và số trang khi đọc toàn văn] |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài sớm dùng kiến trúc Transformer cho SMS rác, đăng ở tạp chí truy cập mở. Báo cả recall và F1, không chỉ accuracy. Ví dụ dễ hiểu: recall 0,9451 nghĩa là cứ 100 tin rác thật thì mô hình bắt được khoảng 94 tin, bỏ sót khoảng 6.

Hạn chế: Chỉ 2 lớp trên bộ tiếng Anh nhỏ và cũ. Accuracy cao (98,92%) một phần do bộ dữ liệu lệch lớp (khoảng 87% là tin hợp lệ theo trang UCI), nên một mô hình đoán toàn "hợp lệ" cũng đạt khoảng 87%. Chưa đọc toàn văn nên chưa biết cách chia tập và có kiểm tra trùng lặp hay không. Lưu ý: bài tổng quan vu-2024-tong-quan-tin-nhan-rac ghi bài này là "LSTM kết hợp CNN" (Bảng 3, tr. 71), không khớp với tóm tắt (Transformer). Khi trích, lấy theo bài gốc.

Dùng cho mục nào của thuyết minh: Mục 8.1, đại diện hướng Transformer cho SMS rác tiếng Anh. Mục 12, dẫn chứng vì sao đề tài báo F1 từng lớp thay vì chỉ accuracy. Chỉ dùng con số trong tóm tắt, ghi rõ nguồn là tóm tắt, cho tới khi đọc toàn văn.

## Trích dẫn IEEE

```
[n] X. Liu, H. Lu, and A. Nayak, "A spam transformer model for SMS spam detection," IEEE Access, vol. 9, pp. 80253–80263, 2021, doi: 10.1109/ACCESS.2021.3081479.
```
