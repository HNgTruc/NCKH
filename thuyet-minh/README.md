# Bản thảo thuyết minh

Mỗi mục của mẫu là một file, đánh số để `scripts/build.ps1` ghép đúng thứ tự. File `README.md` này và các file không bắt đầu bằng số không được ghép.

| File | Mục mẫu | Phụ trách |
| --- | --- | --- |
| `00-bia.md` | Trang bìa (PhuLuc_3_Bia) | A |
| `01-07-thong-tin-chung.md` | 1 đến 7 | A |
| `08-tinh-hinh-nghien-cuu.md` | 8 | B |
| `09-tinh-cap-thiet.md` | 9 | A |
| `10-muc-tieu.md` | 10 | C |
| `11-doi-tuong-pham-vi.md` | 11 | C |
| `12-phuong-phap.md` | 12 | C |
| `13-noi-dung-tien-do.md` | 13.1, 13.2 | A |
| `14-san-pham.md` | 14 | A |
| `15-kha-nang-ung-dung.md` | 15 | A |
| `16-kinh-phi.md` | 16 | A |
| `99-tai-lieu-tham-khao.md` | Tài liệu tham khảo | B |

## Cách viết

1. Đọc khối `<!-- HƯỚNG DẪN ... -->` ở đầu file: chỉ dẫn gốc của mẫu, dòng barem tương ứng, checklist. Khối này không xuất ra Word.
2. Viết bên dưới khối hướng dẫn. Giữ tiêu đề mục đúng như mẫu.
3. Chỗ chưa có thông tin ghi `[TODO: ...]`. Câu cần nguồn mà chưa có ghi `[CẦN NGUỒN]`.
4. Trích dẫn bằng `[n]` theo `99-tai-lieu-tham-khao.md`. Thêm tài liệu mới bằng `/trich-dan-ieee`.
5. Muốn Claude viết nháp hoặc sửa: `/viet-muc-thuyet-minh <số mục>`.

## Từ bản thảo đến file nộp

`scripts/build.ps1` tạo `xuat-ban/thuyet-minh-nhap.docx` để cả nhóm đọc duyệt. Bản nộp cuối chép nội dung vào file mẫu .docx của trường để giữ đúng bảng, khung chữ ký, rồi xuất PDF tên `PPNCKH_MSSV1_MSSV2_MSSV3.pdf`.
