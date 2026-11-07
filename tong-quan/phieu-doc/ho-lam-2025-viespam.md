# ho-lam-2025-viespam: VIESpam: A Hybrid BiLSTM Approach for Spam Classification in English and Vietnamese SMS

Chỉ đọc tóm tắt. Claude điền ngày 06/11/2026 từ trang chương sách trên SpringerLink (tóm tắt, từ khóa, đơn vị, danh mục tham khảo) và Crossref. Toàn văn cần trả phí. Google Books không có bản xem trước chương này. Mọi ô "Bài không nêu" dưới đây nghĩa là tóm tắt không nêu. Trúc cần đọc toàn văn trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Ngoc-Bao Ho-Lam, Anh-Bao Nguyen, My-An Tran, Minh-Triet Tran, Viet-Tham Huynh. Đơn vị: Trường ĐH Khoa học Tự nhiên, ĐHQG TP.HCM (SpringerLink) |
| Năm | Đăng trực tuyến 22/11/2025. Crossref ghi năm in 2026 |
| Tên tạp chí hoặc hội nghị | Future Data and Security Engineering (FDSE 2025), Communications in Computer and Information Science (CCIS), vol. 2709, tr. 315-329, Springer |
| DOI hoặc link chính thức | [10.1007/978-981-95-4724-1_22](https://doi.org/10.1007/978-981-95-4724-1_22) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra hạng FDSE trên CORE và CCIS trên SCImago] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc tóm tắt ngày 06/11/2026. Trúc: [TODO: đọc toàn văn, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tóm tắt: ở Việt Nam, SMS rác xuất hiện cả bằng tiếng Việt và tiếng Anh |
| Khoảng trống tác giả muốn giải quyết | Tóm tắt: cần cách phân loại rác cho hai ngôn ngữ |
| Mục tiêu | Tóm tắt: đề xuất mô hình lai VIESpam, nhẹ, cho tin tiếng Việt và tiếng Anh |
| Câu hỏi hoặc giả thuyết | Bài không nêu (trong tóm tắt) |
| Đối tượng | SMS tiếng Việt và tiếng Anh. Từ khóa ghi "Spam and ham classification", tức 2 lớp |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Tóm tắt: bộ song ngữ 24.086 tin. Tên bộ, nguồn, tỉ lệ tiếng Việt, có công khai không: bài không nêu (trong tóm tắt). Danh mục tham khảo có SMS Spam Collection (tiếng Anh) và dự án SpamHunter trên GitHub, không thấy nguồn bộ SMS tiếng Việt rõ ràng |
| Đặc trưng, đầu vào | Thư viện langdetect nhận diện ngôn ngữ, rồi lấy nhúng từ mô hình tiền huấn luyện: DistilBERT cho tin tiếng Anh, PhoBERT rút gọn số lớp cho tin tiếng Việt (tóm tắt) |
| Phương pháp, mô hình | Nhúng đưa vào mạng BiLSTM để phân loại. So với các mô hình học sâu truyền thống, tên cụ thể: bài không nêu (trong tóm tắt) |
| Chỉ số đánh giá | Accuracy (tóm tắt). Chỉ số khác: bài không nêu (trong tóm tắt) |
| Kết quả chính (số liệu kèm trang, bảng) | Tóm tắt: accuracy 96,75%, kiến trúc gọn nhẹ |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Bài mới nhất tìm được (2025) về SMS rác có tiếng Việt, cùng ĐHQG TP.HCM. Chỉ ra tin rác ở Việt Nam có cả tiếng Anh, điều đề tài cần tính khi thu dữ liệu. Dùng PhoBERT rút gọn, gợi ý cách giảm chi phí tính toán.

Hạn chế: Từ khóa cho thấy chỉ 2 lớp spam/ham, không tách lừa đảo khỏi quảng cáo. Chưa đọc toàn văn nên chưa biết phần tiếng Việt lấy từ đâu và lớn bao nhiêu. Chỉ báo accuracy.

Dùng cho mục nào của thuyết minh: Mục 8.3, nhóm bài dùng PhoBERT cho SMS rác tiếng Việt. Bằng chứng phụ cho khoảng trống "2 lớp" (dựa trên từ khóa của bài, cần đọc toàn văn để chắc). Mục 15 (hướng mở rộng): tin nhắn song ngữ.

## Trích dẫn IEEE

```
[n] N.-B. Ho-Lam, A.-B. Nguyen, M.-A. Tran, M.-T. Tran, and V.-T. Huynh, "VIESpam: A hybrid BiLSTM approach for spam classification in English and Vietnamese SMS," in Future Data and Security Engineering – FDSE 2025 (Communications in Computer and Information Science, vol. 2709). Singapore: Springer, 2025, pp. 315–329, doi: 10.1007/978-981-95-4724-1_22.
```
