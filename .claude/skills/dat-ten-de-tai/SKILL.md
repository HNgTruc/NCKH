---
name: dat-ten-de-tai
description: Đề xuất, chấm và sửa tên đề tài NCKH theo công thức trong slide PPNCKH và bộ tiêu chí FINER. Dùng khi nhóm cần chốt hoặc sửa tên đề tài, hoặc khi mục 1 thuyết minh còn TODO.
argument-hint: "[tên đề tài hiện tại, nếu có]"
---

# Đặt tên đề tài

## Đầu vào

Đọc trước: `thuyet-minh/01-07-thong-tin-chung.md` (mục 1 hiện tại), `thuyet-minh/10-muc-tieu.md`, `thuyet-minh/11-doi-tuong-pham-vi.md`, phần "Mục 1" trong `docs/yeu-cau/kien-thuc-slide.md`. Nếu người dùng đưa tên đề tài trong lệnh thì chấm tên đó trước.

## Các bước

1. Tách tên hiện tại (nếu có) theo công thức [Động từ] + [Đối tượng] + [Bối cảnh/Phạm vi] + [Phương pháp]. Chỉ ra thành phần nào thiếu.
2. Đề xuất 3 đến 5 tên mới bằng tiếng Việt, mỗi tên kèm bản tiếng Anh. Mỗi tên dài 10 đến 15 từ tiếng Việt, đếm và ghi số từ. Các tên phải khác nhau thật về trọng tâm (ví dụ một tên nhấn bộ dữ liệu, một tên nhấn so sánh mô hình), không chỉ đổi chữ.
3. Chấm từng tên bằng checklist 8 câu của Chương 3 (đạt/không đạt).
4. Chấm FINER cho hướng đề tài, mỗi tiêu chí 1 đến 5, kèm một câu lý do gắn với tình hình nhóm (kỹ năng ghi trong `CLAUDE.md`). Feasibility phải tính tới việc nhóm chưa biết Python.
5. Chỉ ra ý tưởng yếu theo slide nếu có: quá rộng, quá hẹp, phụ thuộc dữ liệu độc quyền, nhạy cảm, vượt khả năng.
6. Khuyến nghị một tên và lý do. Hỏi người dùng chốt. Chỉ ghi vào mục 1 và `thuyet-minh/00-bia.md` sau khi người dùng đồng ý.

## Đầu ra

Bảng so sánh các tên (tên, số từ, thành phần còn thiếu, điểm checklist), bảng FINER, khuyến nghị. Khi tên đổi, nhắc kiểm tra lại mục 10 và 11 có còn khớp không.

## Không làm

- Không dùng từ mơ hồ ("ứng dụng công nghệ", "giải pháp thông minh").
- Không hứa kết quả trong tên ("chính xác cao").
- Không thêm "Nghiên cứu" ở đầu nếu đã có động từ khác.
