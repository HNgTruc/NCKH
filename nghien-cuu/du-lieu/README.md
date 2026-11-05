# Dữ liệu

`raw/` không lên git và Claude Code bị chặn đọc thư mục này (`.claude/settings.json`). Dữ liệu chỉ chuyển sang `processed/` sau khi ẩn danh theo `../huong-dan-gan-nhan.md`.

## Nguồn dữ liệu

Mỗi nguồn một dòng. Điều khoản sử dụng phải đọc trước khi lấy dữ liệu, vì mục 12.5 của thuyết minh cần nêu cơ sở hợp pháp.

| Nguồn | Kênh (SMS, email, mạng xã hội) | Cách lấy | Điều khoản, giấy phép | Số mẫu | Khoảng thời gian | Người phụ trách |
| --- | --- | --- | --- | --- | --- | --- |
| [tran-2026-vi-sms-dataset](../../tong-quan/phieu-doc/tran-2026-vi-sms-dataset.md): Hugging Face `trannguyenthaituan/vietnamese_sms_dataset`, commit `a90e2bd` | SMS | Script `nghien-cuu/src/gan_nhan_so_bo.py` tải file `full_dataset.csv` về `processed/tran-2026/` | CC BY 4.0: được dùng, sửa, chia sẻ nếu ghi nguồn. Tác giả đã ẩn danh bằng thẻ `[PHONE]`, `[MONEY]`...; script quét thêm số điện thoại, số dài | 2.991 dòng, 2.629 sau khi bỏ trùng | 28/05/2026 đến 03/08/2026 | Trúc (vai C) |

## Thẻ dữ liệu (điền khi có dữ liệu)

| Trường | Giá trị |
| --- | --- |
| Tổng số mẫu | |
| Phân bố nhãn | |
| Tỉ lệ tin có dấu, không dấu, teencode | |
| Cách chia train/validation/test | |
| Random seed | |
| Ngày chốt phiên bản | |
| Các bias đã biết | |
