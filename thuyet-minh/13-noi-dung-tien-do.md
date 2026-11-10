<!-- HƯỚNG DẪN
Mẫu 13.1: nêu rõ từng nội dung gắn với các mục tiêu cụ thể.
Mẫu 13.2: bảng STT, công việc chủ yếu, thời gian (bắt đầu-kết thúc), người thực hiện.
Barem BT2: chia đề tài thành phần nhỏ tương ứng mục tiêu cụ thể; bảng tiến độ có ngày bắt đầu, ngày kết thúc, người phụ trách. CLO4: phân bổ thời gian hợp lý.
Bảng dưới là KẾ HOẠCH THỰC HIỆN ĐỀ TÀI (2 tháng, 10/2026 đến 11/2026), khác lịch làm bài môn học ở docs/ke-hoach/lich-trinh.md.
Cột "Mục tiêu" thêm vào để người chấm thấy liên kết với mục 10. Nếu muốn giữ đúng 4 cột của mẫu, đưa MT vào cuối ô "Công việc".

Checklist:
- Mỗi MT ở mục 10 có ít nhất một nội dung ở 13.1
- Tổng thời gian bằng số tháng ở mục 3
- Người thực hiện khớp mục 5
- Có khoảng dự phòng cho gán nhãn (việc hay trễ nhất)
-->

## 13. Nội dung nghiên cứu và tiến độ thực hiện

### 13.1. Nội dung nghiên cứu

- Nội dung 1 (MT1, trả lời CH1 và CH2): xây dựng mẫu dữ liệu ba nhãn. Tải bộ SMS công khai đúng phiên bản, bỏ tin trùng, viết hướng dẫn gán nhãn, gợi ý nhãn bằng quy tắc từ khóa, chọn ngẫu nhiên phân tầng 600 tin. Nhãn sơ bộ của 600 tin do mô hình ngôn ngữ gán, người gán thứ nhất xem lại và chốt, người gán thứ hai gán độc lập 100 tin, tính Cohen's kappa và lập bảng chuyển từ nhãn gốc hai lớp sang ba nhãn.
- Nội dung 2 (MT2, trả lời CH3, CH4 và H1): huấn luyện và đánh giá TF-IDF kết hợp Logistic Regression, PhoBERT và ViSoBERT trên 600 tin bằng kiểm định chéo 5 phần. Tính precision, recall, F1 từng lớp, F1 trung bình macro và ma trận nhầm lẫn.
- Nội dung 3 (MT3, trả lời CH5 và H2): tạo bản bỏ dấu, bản chèn ký tự và bản xóa thẻ quảng cáo của tập kiểm tra trong từng phần, đo mức giảm F1 lớp lừa đảo của ba mô hình.

### 13.2. Tiến độ thực hiện

| STT | Công việc chủ yếu | Thời gian (bắt đầu - kết thúc) | Người thực hiện | Nội dung |
| --- | --- | --- | --- | --- |
| 1 | Xác định vấn đề nghiên cứu, đọc tài liệu sơ bộ, đề xuất câu hỏi nghiên cứu | 10/2026 | Cả nhóm | Chuẩn bị |
| 2 | Tổng quan tài liệu, lập ma trận tổng quan, chốt tên đề tài | 01/11/2026 - 07/11/2026 | Khang, Huỳnh Ngọc Trúc | Chuẩn bị |
| 3 | Chọn bộ dữ liệu, soạn hướng dẫn gán nhãn, viết script gán nhãn sơ bộ | 04/11/2026 - 07/11/2026 | Nhân | 1 |
| 4 | Gán nhãn sơ bộ 600 tin bằng mô hình ngôn ngữ, Trúc xem lại và chốt; Khang gán độc lập 100 tin không xem nhãn; tính kappa | 07/11/2026 - 08/11/2026 | Huỳnh Ngọc Trúc, Khang | 1 |
| 5 | Họp xử lý 29 tin bất đồng, bổ sung hai quy tắc vào hướng dẫn gán nhãn | 08/11/2026 | Huỳnh Ngọc Trúc, Khang | 1 |
| 6 | Huấn luyện và đánh giá ba mô hình bằng kiểm định chéo 5 phần (chạy sơ bộ) | 08/11/2026 | Nhân, Huỳnh Ngọc Trúc | 2 |
| 7 | Đánh giá trên tin bỏ dấu, chèn ký tự và đã xóa thẻ quảng cáo (chạy sơ bộ) | 08/11/2026 | Nhân | 3 |
| 8 | Hoàn thiện thuyết minh, làm slide, tập trình bày, viết thuyết minh và bản thảo | 02/11/2026 - 09/11/2026 | Huỳnh Ngọc Trúc, cả nhóm | |

Dòng 2 đến 7 đã thực hiện ở mức sơ bộ đến ngày 08/11/2026. Dòng 8 là kế hoạch cho ngày 09/11/2026. Kết quả trong thuyết minh là kết quả sơ bộ.
