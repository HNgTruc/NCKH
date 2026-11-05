# salman-2024-evasive-sms: Investigating Evasive Techniques in SMS Spam Filtering: A Comparative Analysis of Machine Learning Models

Chỉ đọc tóm tắt. Claude điền ngày 04/11/2026 từ tóm tắt (lấy qua OpenAlex và Semantic Scholar) và siêu dữ liệu Crossref. Bài là truy cập mở (CC BY-NC-ND 4.0), nhưng IEEE Xplore chặn truy cập tự động (lỗi 420 và 418 với cả link PDF). Không tìm thấy bản arXiv của bài này. Cùng nhóm tác giả có preprint khác, "An Empirical Analysis of SMS Scam Detection Systems" ([arXiv 2210.10451](https://arxiv.org/abs/2210.10451), 2022, bộ 153.551 tin), số liệu khác bài này, Claude chưa đọc và không dùng để điền phiếu. Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Muhammad Salman, Muhammad Ikram, Mohamed Ali Kaafar (School of Computing, Macquarie University, Sydney, Úc). Đơn vị lấy từ Crossref |
| Năm | 2024 (Crossref ghi tạo bản ghi ngày 09/02/2024) |
| Tên tạp chí hoặc hội nghị | IEEE Access, vol. 12, tr. 24306-24324 |
| DOI hoặc link chính thức | [10.1109/ACCESS.2024.3364671](https://doi.org/10.1109/ACCESS.2024.3364671). IEEE Xplore: [document 10431737](https://ieeexplore.ieee.org/document/10431737/). Giấy phép bài: CC BY-NC-ND 4.0 (Crossref) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra IEEE Access trên SCImago, ghi link và hạng Q của năm 2024] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 04/11/2026. Trúc: [TODO: tải PDF từ IEEE Xplore bằng trình duyệt, đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: SMS rác vẫn là vấn đề lớn. Kẻ gửi rác dùng nhiều cách né tránh (evasion) để lọt qua bộ lọc |
| Khoảng trống tác giả muốn giải quyết | Tóm tắt: cần xác định các thách thức của hệ thống phát hiện và lọc SMS rác hiện có, đặc biệt là độ bền trước kỹ thuật né tránh |
| Mục tiêu | Tóm tắt: công bố bộ SMS mới, phân tích spam thay đổi theo thời gian, so sánh mô hình học máy nông (shallow), mạng sâu và dịch vụ chống rác thương mại, kiểm tra khả năng chịu né tránh |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS, nhãn ham và spam. Tóm tắt không có các từ "scam", "smishing", "phishing", "fraud" (Claude kiểm tra từ khóa trong tóm tắt), nên chưa biết bộ dữ liệu có tách tin lừa đảo khỏi tin rác khác hay không. [TODO: Trúc kiểm tra trong toàn văn: bộ nhãn, có nhãn smishing/scam riêng không] |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tóm tắt: hơn 68.000 tin, khoảng 61% hợp lệ và 39% rác. Tác giả gọi đây là bộ SMS rác công khai lớn nhất tới thời điểm đó và công bố cho nghiên cứu. Nguồn thu thập, ngôn ngữ, thời gian thu, cách gán nhãn: bài không nêu (trong tóm tắt). Giấy phép bộ dữ liệu: bài không nêu (trong tóm tắt). [TODO: Trúc tìm link tải và giấy phép dữ liệu trong toàn văn] |
| Đặc trưng, đầu vào | Tóm tắt: đặc trưng ngữ nghĩa (semantic) và cú pháp (syntactic) |
| Phương pháp, mô hình | Tóm tắt: các phương pháp học máy và học sâu phổ biến, cùng các dịch vụ chống rác phổ biến. Tên từng mô hình: bài không nêu (trong tóm tắt) |
| Chỉ số đánh giá | Bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: phần lớn dịch vụ chống rác dựa trên học máy nông phân loại SMS rác kém. Mọi phương pháp học máy được thử đều dễ bị các chiến lược né tránh qua mặt. Tóm tắt không có con số kết quả. [TODO: Trúc lấy số từ bảng kết quả, ghi rõ loại né tránh nào được thử] |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Bộ dữ liệu lớn hơn nhiều so với SMS Spam Collection (hơn 68.000 so với 5.574 tin) và có công bố. Đây là bài hiếm hoi đặt câu hỏi về né tránh, tức là kẻ gửi cố tình viết khác đi để lọt bộ lọc, ví dụ viết "ng4n h4ng" thay cho "ngân hàng". Tin lừa đảo tiếng Việt cũng có kiểu này: bài vu-2024-tong-quan-tin-nhan-rac có ảnh minh họa chèn ký tự, viết không dấu để tránh bộ lọc (Hình 7, tr. 73).

Hạn chế: Chỉ đọc tóm tắt. Theo tóm tắt, bộ dữ liệu có 2 nhãn ham/spam, chưa thấy tách lừa đảo. Ngôn ngữ dữ liệu chưa rõ. Chưa biết giấy phép dữ liệu, nên chưa thể nói nhóm được dùng lại hay không.

Dùng cho mục nào của thuyết minh: Mục 8.1, đại diện hướng nghiên cứu độ bền trước né tránh. Mục 9, làm lý do để đề tài thử mô hình trên tin bị viết biến dạng (không dấu, chèn ký tự). Mục 12, gợi ý thêm một tập kiểm tra nhỏ gồm tin đã biến dạng. Chưa dùng con số nào ngoài tóm tắt.

## Trích dẫn IEEE

```
[n] M. Salman, M. Ikram, and M. A. Kaafar, "Investigating evasive techniques in SMS spam filtering: A comparative analysis of machine learning models," IEEE Access, vol. 12, pp. 24306–24324, 2024, doi: 10.1109/ACCESS.2024.3364671.
```
