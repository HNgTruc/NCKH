<!-- HƯỚNG DẪN
Mẫu: Khả năng ứng dụng và phát triển của đề tài (không có chỉ dẫn thêm).
Slide Chương 4: tiêu chí khả áp dụng gồm khả thi công nghệ, kinh tế, xã hội, khả năng mở rộng, bền vững. Lĩnh vực áp dụng: giáo dục, công nghiệp và công nghệ, chính sách công.
Bài tập 2 có thêm "Kết luận và kiến nghị" mà mẫu không có. Tạm để ở 15.3, chờ Trúc quyết (docs/ke-hoach/gia-dinh.md, dòng 3).

Checklist:
- Ứng dụng nêu người dùng cụ thể (ai dùng, dùng thế nào)
- Hướng phát triển nêu điều đề tài cố ý chưa làm ở phạm vi mục 11
- Không hứa triển khai thương mại
-->

## 15. Khả năng ứng dụng và phát triển của đề tài

### 15.1. Khả năng ứng dụng

| Người dùng | Dùng thế nào |
| --- | --- |
| Nhóm nghiên cứu xử lý ngôn ngữ tiếng Việt | Dùng hướng dẫn gán nhãn và bộ nhãn ba lớp (mã tin kèm nhãn) để gán thêm dữ liệu hoặc so sánh mô hình trên cùng bộ nhãn |
| Đơn vị phát triển ứng dụng lọc tin nhắn | Tham khảo kết quả so sánh ba mô hình và mức giảm F1 khi tin bị viết biến dạng khi chọn mô hình cho bộ lọc |
| Giảng viên, sinh viên Khoa Công nghệ Thông tin | Dùng notebook làm ví dụ thực hành phân loại văn bản tiếng Việt từ khâu gán nhãn đến đánh giá |

Đề tài không triển khai sản phẩm thương mại và không tích hợp vào hệ thống của nhà mạng.

### 15.2. Hướng phát triển

Các việc dưới đây nằm ngoài phạm vi 3 tháng ở mục 11, nhóm dự kiến làm sau khi kết thúc học phần:

- Gán nhãn toàn bộ 2.629 tin của bộ dữ liệu công khai, với hai người gán mù và người thứ ba phân xử.
- Thu thập thêm tin nhắn từ người tình nguyện có phiếu đồng ý, để giảm sai lệch do chỉ có một nguồn và để có tập kiểm tra theo thời gian.
- Gom các tin gần trùng trước khi chia tập, dùng một tập kiểm tra cố định và kiểm định bootstrap cho H1, H2.
- Xây bản demo phân loại một tin nhắn, chạy cục bộ, có giới hạn số lần gọi để hạn chế việc dùng ngược.

### 15.3. Kết luận và kiến nghị

[TODO: viết sau khi có kết quả notebook. Tóm kết quả so với MT1 đến MT3, nêu giả thuyết nào được ủng hộ, kiến nghị cho nghiên cứu tiếp theo]
