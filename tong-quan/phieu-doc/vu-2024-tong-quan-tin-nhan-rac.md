# vu-2024-tong-quan-tin-nhan-rac: Nghiên cứu bài toán phát hiện tin nhắn rác trên thiết bị di động và một số vấn đề gợi mở

Claude điền từ toàn văn PDF trên VJOL (tr. 65-78) ngày 04/11/2026. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Vũ Duy Hiến, Chu Văn Huy, Bùi Thị Hồng Nhung, Lê Thị Hồng Nhung. Học viện Ngân hàng (tr. 65) |
| Năm | 2024 (nhận bài 06/06/2024, nhận bản sửa 20/06/2024, duyệt đăng 01/07/2024, tr. 65) |
| Tên tạp chí hoặc hội nghị | Tạp chí Kinh tế - Luật và Ngân hàng (Học viện Ngân hàng), ISSN 3030-4199, Số 266, Năm thứ 26 (7), tháng 7/2024, tr. 65-78. Tên tiếng Anh của bài: "A study on the spam sms detection problem and some recommendations" (tr. 65) |
| DOI hoặc link chính thức | [10.59276/JELB.2024.07CD.2763](https://doi.org/10.59276/JELB.2024.07CD.2763) (in ở tr. 65, Claude chưa mở thử link DOI). [Trang bài trên VJOL](https://vjol.info.vn/tckinhteluatvanganhang-hvnh/article/view/100298) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra danh mục tạp chí HĐGSNN 2025, ngành nào tính điểm. Đây là tạp chí ngành kinh tế, không phải CNTT] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Tội phạm công nghệ cao dùng tin nhắn rác để lừa đảo chiếm đoạt tài sản. Đã có nhiều giải pháp phát hiện với độ chính xác cao, nhưng số vụ và thiệt hại tài chính vẫn có dấu hiệu tăng (tóm tắt, tr. 65; tr. 68) |
| Khoảng trống tác giả muốn giải quyết | Khoảng cách giữa độ chính xác rất cao trong các bài báo và thiệt hại không giảm trong thực tế (tr. 73) |
| Mục tiêu | (1) Đánh giá các công trình điển hình về phát hiện tin nhắn rác để xác định tồn tại; (2) đưa ra khuyến nghị (tr. 68) |
| Câu hỏi hoặc giả thuyết | Bài không nêu |
| Đối tượng | Bài tổng quan, không có thực nghiệm. Định nghĩa tin nhắn rác gồm cả tin quảng cáo, tiếp thị, tin không liên quan và tin lừa đảo hoặc chứa mã độc (tr. 67, 69) |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Phương pháp: phân tích, tổng hợp; quan sát và thu thập số liệu thực tế; phương pháp chuyên gia (tr. 68). Bài không nêu cơ sở dữ liệu đã tìm, từ khóa, tiêu chí chọn bài, số bài sàng lọc. Bảng 1 (tr. 70) liệt kê 3 bộ dữ liệu: Almeida 2011 (5.574 tin, 747 rác), NUS SMS Corpus (67.063 tin, không phân loại), SpamHunter (25.889 tin, 947 rác). Bảng 2 (tr. 70-71) tổng hợp 13 công trình học máy truyền thống, Bảng 3 (tr. 71-72) tổng hợp 9 công trình học sâu, chỉ báo độ chính xác (accuracy) |
| Đặc trưng, đầu vào | Không áp dụng (bài tổng quan) |
| Phương pháp, mô hình | Không áp dụng. Các công trình được tổng hợp dùng Naive Bayes, KNN, SVM, cây quyết định, Markov ẩn, CNN, LSTM và kết hợp (Bảng 2, 3) |
| Chỉ số đánh giá | Bảng 2 và 3 chỉ có cột độ chính xác (%) |
| Kết quả chính (số liệu kèm trang, bảng) | Hầu hết công trình đạt trên 90%, nhiều công trình trên 99% (tr. 70-71). Công trình tiếng Việt duy nhất trong bảng là Tuan và cộng sự 2022 (DNN + PhoBERT, 99,53%) (Bảng 3, tr. 72), tức bài vu-2022-phobert-dnn. Ba tồn tại (mục 2.5, tr. 73-74): (1) dữ liệu: các nghiên cứu dùng lặp lại vài bộ công khai, chủ yếu tiếng Anh, ít số lượng, thiếu cập nhật, gần như không có đóng góp dữ liệu mới, trong khi kẻ gửi liên tục đổi mẫu tin; (2) bài toán: công cụ chỉ cảnh báo tin "thường" hay "rác" là chưa đủ (tr. 74); (3) ứng dụng chặn tin rác chủ yếu dựa trên luật, bản tốt phải trả phí, tuyên truyền chưa hiệu quả. Khuyến nghị (mục 3, tr. 74-76): đóng góp bộ dữ liệu công khai, cập nhật, đa dạng biến thể ngôn ngữ, cần sự hỗ trợ của cơ quan nhà nước và nhà mạng, tuân thủ pháp luật và quyền riêng tư (tr. 75); phát triển mô hình cảnh báo nhiều cấp độ, nhận diện được tin rủi ro cao về tài chính-ngân hàng hoặc lừa đảo (mục 3.2, tr. 75); ứng dụng miễn phí và tuyên truyền (mục 3.3, tr. 76). Kết luận đề xuất mở rộng sang tiếng Việt (tr. 76) |

## Số liệu thống kê bài dẫn (cho mục 9, phải lần về nguồn gốc)

Cột "Nguồn bài ghi" chép đúng cách bài trích. Cột "Ghi chú" là nhận xét của Claude khi đối chiếu với danh mục tài liệu tham khảo (tr. 76-78).

| Số liệu | Trang | Nguồn bài ghi | Ghi chú |
| --- | --- | --- | --- |
| Việt Nam: BKAV cho biết 75% người dùng từng nhận tin nhắn/cuộc gọi rác lừa đảo | tr. 73 | (XM, 2023) | "XM, 2023" không có trong danh mục tài liệu tham khảo. Năm khảo sát của BKAV không ghi. Phải tự tìm báo cáo gốc của BKAV |
| Việt Nam: dùng trạm BTS giả, tội phạm có thể phát tán tới 100.000 tin nhắn rác/lừa đảo mỗi ngày | tr. 73 | "theo báo cáo của Bộ Thông tin và Truyền thông năm 2023 (An, 2024)" | An (2024) là bài báo Tuổi Trẻ, URL có ngày 17/01/2024 (tr. 76). Đây là nguồn thứ cấp, báo cáo gốc của Bộ chưa được trích |
| Việt Nam: năm 2022 một khách hàng nữ mất 3 tỷ đồng vài phút sau khi làm theo tin nhắn mạo danh ngân hàng | tr. 73 | (Xuân, 2022) | "Xuân, 2022" không có trong danh mục tài liệu tham khảo. Là một vụ việc, không phải thống kê |
| Việt Nam: một khách hàng mất 38 triệu đồng sau khi đăng nhập "xác minh tài khoản" theo yêu cầu kẻ mạo danh | tr. 73 | (Thuần & Hồng, 2021) | Không có trong danh mục tài liệu tham khảo. Là một vụ việc |
| Việt Nam đứng thứ 9 thế giới về số tin nhắn rác "trực tiếp" (tin tin tặc đang tương tác trực tiếp để lừa đảo) năm 2021. Hình 4 ghi giá trị 284 cho Việt Nam, không ghi đơn vị | tr. 68 | Lời văn: báo cáo năm 2021 (Gajić, 2022). Chú thích Hình 4: Maqsood và cộng sự, 2023 | Gajić (2022) là blog 99firms.com (tr. 77). Lời văn và chú thích hình ghi hai nguồn khác nhau |
| Việt Nam nằm trong 20 nước gửi nhiều thư/tin nhắn rác nhất năm 2022 (Hình 3) | tr. 67 | Lời văn: Statista. Chú thích Hình 3: Maqsood và cộng sự, 2023 | Bài không ghi con số cho Việt Nam trong lời văn, chỉ có cột trên hình. Không nên đọc số từ hình |
| Thế giới: hơn 6 tỷ người dùng di động năm 2022 | tr. 66 | Statista (Degenhar, 2024; Maqsood và cộng sự, 2023) | Không phải số liệu lừa đảo |
| Năm 2022, mỗi tháng một người ở Cameroon nhận 16 tin rác, ở Nam Phi khoảng 6 tin | tr. 67 | Truecaller và (Maqsood và cộng sự, 2023) | Nước ngoài |
| Năm 2022, Nga phát tán 23,5% thư/tin nhắn rác, Đức 11%, Mỹ 10,85% | tr. 67 | Statista | Danh mục tài liệu không có mục Statista riêng cho số này |
| 75% người dùng di động có cài ứng dụng tài chính, nên có nguy cơ thất thoát vì tin rác lừa đảo | tr. 68 | (Fact.MR, 2021) | Báo cáo thị trường ứng dụng tài chính, không đo trực tiếp lừa đảo |
| Mỹ: 225 tỷ tin rác năm 2023 (tăng 157%), 19,2 tỷ tin trong tháng 3/2024 | tr. 72 | (Robokiller, 2022) | Nguồn ghi năm 2022 nhưng số liệu là của 2023 và 2024, không khớp |
| Mỹ: 21% vụ lừa đảo liên quan tin nhắn rác | tr. 72 | Techreport (Laborde, 2024) | Nước ngoài |
| Mỹ: 68,4 triệu người là nạn nhân lừa đảo qua điện thoại, thiệt hại hơn 330 triệu USD năm 2022 | tr. 72-73 | Truecaller và FTC (Truecaller, 2022), (Khristopher, 2023) | Khristopher (2023) là bài CBS News |
| Mỹ: mất 330 triệu USD vì tin nhắn lừa đảo năm 2022, 131 triệu năm 2021, 86 triệu năm 2020. 35% người Mỹ vẫn tò mò về tin rác từ số lạ | tr. 74 | (Truecaller, 2022) cho con số 35%. Dãy số 330/131/86 không có trích dẫn riêng | Nước ngoài |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bài tổng quan trong nước mới (2024), chỉ ra đúng vấn đề đề tài nhắm tới: cảnh báo hai lớp "thường/rác" là chưa đủ (tr. 74), cần mô hình nhận diện riêng tin lừa đảo, rủi ro tài chính (tr. 75). Có ảnh tin lừa đảo mạo danh Vietcombank viết không dấu (Hình 6, tr. 73) và ví dụ thủ đoạn né bộ lọc (Hình 7, tr. 73), dùng được để minh họa trong thuyết minh. Định nghĩa "tin nhắn rác" của bài gộp cả quảng cáo lẫn lừa đảo (tr. 67, 69), là bằng chứng rằng khái niệm "rác" đang dùng chưa tách hai loại này.

Hạn chế: Không phải tổng quan hệ thống: không nêu cơ sở dữ liệu, từ khóa, tiêu chí chọn bài. Chỉ so độ chính xác, không bàn precision, recall, F1. Có lỗi tổng hợp: Bảng 3 ghi bài Liu 2021 là "LSTM kết hợp CNN" (tr. 71) trong khi tóm tắt bài gốc nói là Transformer (liu-2021-spam-transformer). Không nhắc vu-2023-nhung-tu (2023, nằm trong khung 5 năm của bài). pham-2016-vi-sms-spam (2016) nằm ngoài khung 5 năm nên vắng mặt là hợp lý. Nhiều số liệu lấy từ báo chí, blog, báo cáo doanh nghiệp. Một số trích dẫn không có trong danh mục tài liệu (XM 2023, Xuân 2022, Thuần & Hồng 2021). Nguồn của hình và lời văn không khớp (Hình 3, Hình 4). Đăng ở tạp chí ngành kinh tế.

Dùng cho mục nào của thuyết minh: Mục 8.3, nghiên cứu tổng quan trong nước. Mục 9, trích khuyến nghị "cảnh báo nhiều cấp độ, nhận diện tin lừa đảo" (tr. 75) làm bằng chứng một nhóm khác cũng thấy khoảng trống này. Không dùng thẳng số liệu thống kê của bài cho mục 9. Với số 75% của BKAV và số 100.000 tin/ngày của Bộ TT&TT, phải tìm báo cáo gốc và ghi `[CẦN NGUỒN]` cho tới khi tìm được.

## Trích dẫn IEEE

```
[n] D. H. Vu, V. H. Chu, T. H. N. Bui, and T. H. N. Le, "Nghiên cứu bài toán phát hiện tin nhắn rác trên thiết bị di động và một số vấn đề gợi mở," Tạp chí Kinh tế - Luật và Ngân hàng, vol. 26, no. 7 (266), pp. 65–78, Jul. 2024, doi: 10.59276/JELB.2024.07CD.2763.
```
