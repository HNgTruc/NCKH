# Nghiên cứu

Khu này dùng khi nhóm làm thật đề tài sau môn học. Trong 6 tuần làm thuyết minh, chỉ cần `huong-dan-gan-nhan.md` (viết mục 12) và `du-lieu/README.md` (khai báo nguồn dữ liệu dự kiến).

## Cấu trúc dự kiến

| Thư mục | Nội dung | Có lên git không |
| --- | --- | --- |
| `du-lieu/raw/` | Dữ liệu gốc, còn số điện thoại, tên, số tài khoản | Không |
| `du-lieu/processed/` | Dữ liệu đã ẩn danh và gán nhãn | Có, nếu điều khoản nguồn cho phép |
| `notebooks/` | Jupyter notebook thử nghiệm, tạo khi bắt đầu code | Có |
| `src/` | Code tiền xử lý, huấn luyện, đánh giá, tạo khi bắt đầu code | Có |

## Thứ tự làm khi bắt đầu

1. Chốt nguồn dữ liệu và điều khoản trong `du-lieu/README.md`.
2. Gán thử 100 mẫu theo `huong-dan-gan-nhan.md`, đo độ đồng thuận, sửa hướng dẫn.
3. Ẩn danh toàn bộ dữ liệu thô, ghi vào `processed/`.
4. Chạy mô hình cơ sở trước, mô hình tiền huấn luyện sau.
5. Ghi phiên bản Python, thư viện, random seed vào `requirements.txt` và báo cáo, để người khác chạy lại ra cùng kết quả.
