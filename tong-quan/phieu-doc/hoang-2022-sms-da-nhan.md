# hoang-2022-sms-da-nhan: Một số phương pháp phân lớp đa nhãn và ứng dụng phân loại tin nhắn SMS tiếng Việt

Claude điền từ tóm tắt ngày 06/11/2026. Trúc mở toàn văn ngày 10/11/2026 và xác nhận các điểm bên dưới (tên tác giả đầu là Hoàng Thị Hà, năm 2022, bộ SMSVN có 11 nhãn gồm Scam và Ads). Trang bài trên vie.vjas.vn trả lỗi 403 với truy cập tự động (cả trang bài và link PDF). Tóm tắt, từ khóa, đơn vị tác giả và danh mục tài liệu tham khảo lấy từ bản lưu (cache) trang bài của Google Scholar. Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu, không phải toàn văn không nêu. Trúc cần mở toàn văn trước khi trích, nhất là để biết bộ nhãn của SMSVN.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Hoàng Thị Hà (tác giả liên hệ, Trúc xác nhận tên ngày 10/11/2026), Đào Xuân Dương, Lê Thị Nhung. Đơn vị: Khoa CNTT, Học viện Nông nghiệp Việt Nam; Công ty Cổ phần Tin học Viễn thông Bưu điện (trang bài) |
| Năm | 2022 (Tập 20, Số 12), Trúc xác nhận ngày 10/11/2026. Nhận bài 24/02/2022, chấp nhận 20/12/2022 |
| Tên tạp chí hoặc hội nghị | Tạp chí Khoa học Nông nghiệp Việt Nam, Tập 20, Số 12, tr. 1672-1683 |
| DOI hoặc link chính thức | Trang bài không có DOI (ô DOI để trống). [Trang bài](https://vie.vjas.vn/index.php/vjasvn/article/view/1083) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra danh mục HĐGSNN 2025, xem tạp chí có được tính điểm ngành CNTT không] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 06/11/2026. Trúc: đã mở toàn văn và đọc phần dữ liệu (Bảng 4, 7, 8) và kết quả (Bảng 9 đến 13) ngày 10/11/2026 |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: người dùng di động thường xuyên bị làm phiền bởi "một lượng lớn tin nhắn lừa đảo, tin nhắn quảng cáo" ở nhiều lĩnh vực như giải trí, mua sắm, tài chính, bất động sản |
| Khoảng trống tác giả muốn giải quyết | Tóm tắt: một tin nhắn có thể thuộc một hoặc nhiều loại cùng lúc, nên phân lớp đơn nhãn (single-label) là không phù hợp |
| Mục tiêu | Tóm tắt: xem xét các kỹ thuật phân lớp đa nhãn (multi-label classification), thu thập bộ SMS tiếng Việt, cải thiện độ chính xác bằng tiền xử lý (chuẩn hóa, làm sạch) |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS tiếng Việt, gán nhiều nhãn cho một tin |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Bộ SMSVN, 2.000 tin nhắn tiếng Việt (tóm tắt). Toàn văn (Bảng 7, 8): 11 nhãn, tần suất NonSpam 1000, Spam 1000, Ads 962, Entertainment 231, App 534, RealEstate 80, Financial 56, Promotion 656, Harm 353, Scam 428, Virus 15. Một tin có thể mang nhiều nhãn. Tóm tắt chỉ nhắc tin lừa đảo, tin quảng cáo và các lĩnh vực giải trí, mua sắm, tài chính, bất động sản, chưa rõ đây là nhãn hay chỉ là mô tả bối cảnh. Nguồn thu, cách gán nhãn, có công khai không: bài không nêu (trong tóm tắt) |
| Đặc trưng, đầu vào | Tóm tắt: tiền xử lý để chuẩn hóa và làm sạch dữ liệu. Cách biểu diễn văn bản: bài không nêu (trong tóm tắt) |
| Phương pháp, mô hình | Tóm tắt: các thuật toán phân lớp đa nhãn, từ khóa nêu hai nhóm "thích nghi thuật toán" (algorithm adaptation) và "chuyển đổi bài toán" (problem transformation). Kết luận chọn Classifier Chains với Gaussian Naive Bayes (GNB). Danh mục tham khảo có ML-kNN, Classifier Chains xác suất, scikit-learn. Không dùng mô hình tiền huấn luyện (theo tóm tắt và danh mục tham khảo) |
| Chỉ số đánh giá | Tóm tắt nhắc "độ chính xác" và "tỉ lệ nhãn bị phân lớp sai" (có thể là Hamming loss). Tên chỉ số cụ thể: bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: sau tiền xử lý, hầu hết kỹ thuật đa nhãn có độ chính xác cao hơn và tỉ lệ nhãn sai thấp hơn. Classifier Chains với GNB phù hợp nhất. Toàn văn (Bảng 10, 12): Classifier Chains kết hợp GNB đạt Hamming-Loss 0,027 và accuracy 0,868, thời gian 54 giây |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài SMS tiếng Việt đầu tiên tìm được không phân loại hai lớp spam/ham. Tóm tắt nêu thẳng cả tin lừa đảo lẫn tin quảng cáo. Có bộ dữ liệu riêng (SMSVN). Ví dụ: một tin "Vay tiêu dùng lãi 0%, bấm link..." có thể vừa thuộc "tài chính" vừa thuộc "lừa đảo", nên tác giả chọn đa nhãn.

Hạn chế: Bộ SMSVN có nhãn Scam (428 tin) và Ads (962 tin) nhưng gán đa nhãn, nên một tin có thể vừa thuộc Scam vừa thuộc Ads hay Financial, lừa đảo và quảng cáo không loại trừ nhau. Bộ nhỏ (2.000 tin, 11 nhãn). Dùng mô hình học máy truyền thống, không có PhoBERT. Tạp chí ngành nông nghiệp, cần kiểm tra danh mục.

Dùng cho mục nào của thuyết minh: Mục 8.3, như hướng đa nhãn trong nghiên cứu SMS tiếng Việt, và mục 8.4, nơi điểm mới của đề tài được viết lại: không nằm ở việc có nhãn lừa đảo, mà ở ba lớp loại trừ nhau, hướng dẫn gán nhãn có đo đồng thuận, so sánh ba mô hình và đo độ bền khi tin bị biến dạng. Mục 9 cũng nhắc bài này.

## Trích dẫn IEEE

```
[n] T. H. Hoang, X. D. Dao, and T. N. Le, "Một số phương pháp phân lớp đa nhãn và ứng dụng phân loại tin nhắn SMS tiếng Việt," Tạp chí Khoa học Nông nghiệp Việt Nam, vol. 20, no. 12, pp. 1672–1683, 2022.
```
