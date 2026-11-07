<!-- HƯỚNG DẪN
Mẫu 13.1: nêu rõ từng nội dung gắn với các mục tiêu cụ thể.
Mẫu 13.2: bảng STT, công việc chủ yếu, thời gian (bắt đầu-kết thúc), người thực hiện.
Barem BT2: chia đề tài thành phần nhỏ tương ứng mục tiêu cụ thể; bảng tiến độ có ngày bắt đầu, ngày kết thúc, người phụ trách. CLO4: phân bổ thời gian hợp lý.
Bảng dưới là KẾ HOẠCH THỰC HIỆN ĐỀ TÀI (6 tháng), khác lịch làm bài môn học ở docs/ke-hoach/lich-trinh.md.
Cột "Mục tiêu" thêm vào để người chấm thấy liên kết với mục 10. Nếu muốn giữ đúng 4 cột của mẫu, đưa MT vào cuối ô "Công việc".

Checklist:
- Mỗi MT ở mục 10 có ít nhất một nội dung ở 13.1
- Tổng thời gian bằng số tháng ở mục 3
- Người thực hiện khớp mục 5
- Có khoảng dự phòng cho gán nhãn (việc hay trễ nhất)
-->

## 13. Nội dung nghiên cứu và tiến độ thực hiện

### 13.1. Nội dung nghiên cứu

- Nội dung 1 (MT1, trả lời CH1 và CH2): xây dựng mẫu dữ liệu ba nhãn. Tải bộ SMS công khai đúng phiên bản, bỏ tin trùng, viết hướng dẫn gán nhãn, gợi ý nhãn bằng quy tắc từ khóa, chọn ngẫu nhiên phân tầng 600 tin. Người gán thứ nhất chốt nhãn 600 tin, người gán thứ hai gán độc lập 100 tin, tính Cohen's kappa và lập bảng chuyển từ nhãn gốc hai lớp sang ba nhãn.
- Nội dung 2 (MT2, trả lời CH3, CH4 và H1): huấn luyện và đánh giá TF-IDF kết hợp Logistic Regression, PhoBERT và ViSoBERT trên 600 tin bằng kiểm định chéo 5 phần; tính precision, recall, F1 từng lớp, F1 trung bình macro và ma trận nhầm lẫn.
- Nội dung 3 (MT3, trả lời CH5 và H2): tạo bản bỏ dấu và bản chèn ký tự của tập kiểm tra trong từng phần, đo mức giảm F1 lớp lừa đảo của ba mô hình.

### 13.2. Tiến độ thực hiện

| STT | Công việc chủ yếu | Thời gian (bắt đầu - kết thúc) | Người thực hiện | Mục tiêu |
| --- | --- | --- | --- | --- |
| 1 | Học phương pháp nghiên cứu khoa học, chọn hướng đề tài, làm bài tập giữa kỳ (phân tích 1 bài báo, đề xuất 5 câu hỏi nghiên cứu) | 09/2026 - 10/2026 | Cả nhóm | |
| 2 | Chốt tên đề tài; tìm, đọc tài liệu và lập ma trận tổng quan | 02/11/2026 - 07/11/2026 | B, A | |
| 3 | Chọn bộ dữ liệu, viết hướng dẫn gán nhãn, viết script gán nhãn sơ bộ | 06/11/2026 - 06/11/2026 | C | MT1 |
| 4 | Gán nhãn 600 tin; người thứ hai gán độc lập 100 tin; tính kappa | 07/11/2026 - 08/11/2026 | C, B | MT1 |
| 5 | Huấn luyện và đánh giá ba mô hình; đánh giá trên tin bỏ dấu và chèn ký tự | 08/11/2026 - 09/11/2026 | C, A | MT2, MT3 |
| 6 | Viết, ghép và tự kiểm tra bản thuyết minh | 06/11/2026 - 09/11/2026 | A, cả nhóm | |
| 7 | Trình bày trước lớp, sửa theo góp ý, nộp bản in | 10/11/2026 - 30/11/2026 | Cả nhóm | |
