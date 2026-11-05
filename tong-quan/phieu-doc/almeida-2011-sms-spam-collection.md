# almeida-2011-sms-spam-collection: Contributions to the Study of SMS Spam Filtering: New Collection and Results

Chỉ đọc tóm tắt. Claude điền ngày 04/11/2026 từ tóm tắt (lấy qua OpenAlex vì trang ACM Digital Library chặn truy cập tự động, lỗi 403) và trang bộ dữ liệu trên UCI. Không tìm được toàn văn mở: trang tác giả (dt.fee.unicamp.br) không truy cập được, OpenAlex ghi bài là "closed". Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu, không phải toàn văn không nêu. Trúc cần đọc lại bài gốc (qua thư viện trường) trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Tiago A. Almeida (UNICAMP, Brazil), José María Gómez Hidalgo (Optenet, Tây Ban Nha), Akebo Yamakami (UNICAMP). Đơn vị lấy từ OpenAlex |
| Năm | 2011 |
| Tên tạp chí hoặc hội nghị | Proceedings of the 11th ACM Symposium on Document Engineering (DocEng '11), tr. 259-262, ACM |
| DOI hoặc link chính thức | [10.1145/2034691.2034742](https://doi.org/10.1145/2034691.2034742). Bộ dữ liệu: [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra hạng DocEng trên CORE portal, ghi link] |
| Hạng Q hoặc CiteScore, IF | Hội nghị, không có hạng Q. Hạng CORE: chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 04/11/2026. Trúc: [TODO: đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: dùng điện thoại di động tăng làm SMS rác tăng mạnh. Khó chống vì cước SMS rẻ, nhiều nhà cung cấp làm ngơ, ít phần mềm chống rác cho điện thoại |
| Khoảng trống tác giả muốn giải quyết | Tóm tắt: giới nghiên cứu thiếu bộ SMS rác công khai để kiểm chứng và so sánh các bộ phân loại. Tin nhắn ngắn nên bộ lọc dựa trên nội dung có thể kém hơn so với email |
| Mục tiêu | Tóm tắt: công bố một bộ SMS rác mới, thật, công khai, không mã hóa, theo tác giả là lớn nhất được biết lúc đó, và chạy thử nhiều phương pháp học máy trên bộ này |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | Tin nhắn SMS tiếng Anh, 2 lớp ham và spam (trang UCI) |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Theo trang UCI: 5.574 tin. Nguồn: 425 tin rác từ diễn đàn Grumbletext (Anh), 3.375 tin hợp lệ lấy ngẫu nhiên từ NUS SMS Corpus (khoảng 10.000 tin), 450 tin hợp lệ từ luận án tiến sĩ của Caroline Tagg, 1.002 tin hợp lệ và 322 tin rác từ SMS Spam Corpus v.0.1 Big. Cộng lại: 4.827 hợp lệ, 747 rác. Giấy phép CC BY 4.0. Gửi lên UCI ngày 21/6/2012. Trang UCI không ghi ngôn ngữ, mẫu tin là tiếng Anh, có một số tin kiểu Singlish |
| Đặc trưng, đầu vào | Bài không nêu (trong tóm tắt) |
| Phương pháp, mô hình | Tóm tắt: so sánh "several established machine learning methods". Tên từng phương pháp: bài không nêu trong tóm tắt, chỉ nêu SVM |
| Chỉ số đánh giá | Bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: SVM tốt hơn các bộ phân loại khác, nên tác giả đề xuất dùng SVM làm mức cơ sở (baseline). Tóm tắt không có con số nào. [TODO: Trúc lấy số liệu từ bảng kết quả trong toàn văn] |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bộ SMS rác công khai được dùng nhiều nhất. Bài tổng quan trong nước vu-2024-tong-quan-tin-nhan-rac cho thấy hầu hết công trình ở Bảng 2 và Bảng 3 (tr. 70-72) đều chạy trên bộ này. Có giấy phép rõ (CC BY 4.0). Mô tả rõ nguồn của từng phần dữ liệu.

Hạn chế: Chỉ 2 lớp, gộp mọi loại tin rác (quảng cáo, lừa đảo) vào một nhãn spam. Tiếng Anh. Nhỏ (747 tin rác) và đã cũ (thu trước 2012). Tin hợp lệ và tin rác đến từ nguồn khác nhau (NUS, luận án Tagg so với Grumbletext), giống vấn đề nguồn dữ liệu đã thấy ở vu-2023-nhung-tu.

Dùng cho mục nào của thuyết minh: Mục 8.1, làm mốc bộ dữ liệu kinh điển. Mục 9, làm ví dụ cho nhận xét "bộ dữ liệu chuẩn quốc tế cũng chỉ có 2 lớp". Mục 12, gợi ý ghi rõ nguồn từng phần dữ liệu và giấy phép giống cách UCI mô tả. Chưa trích số liệu kết quả cho tới khi đọc được toàn văn.

## Trích dẫn IEEE

```
[n] T. A. Almeida, J. M. G. Hidalgo, and A. Yamakami, "Contributions to the study of SMS spam filtering: New collection and results," in Proc. 11th ACM Symp. Document Eng. (DocEng), 2011, pp. 259–262, doi: 10.1145/2034691.2034742.
```
