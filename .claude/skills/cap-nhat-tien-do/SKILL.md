---
name: cap-nhat-tien-do
description: Cập nhật tiến độ đồ án trong buổi họp nhóm hằng tuần, gồm sửa cột trạng thái lịch trình, ghi biên bản họp và liệt kê việc tuần tới. Dùng khi nhóm họp, khi người dùng báo đã xong hoặc trễ một việc, hoặc hỏi tuần này làm gì.
argument-hint: "[ghi chú buổi họp]"
---

# Cập nhật tiến độ

## Các bước

1. Lấy ngày hôm nay, xác định đang ở tuần mấy trong `docs/ke-hoach/lich-trinh.md`.
2. Xem bằng chứng tiến độ, không chỉ dựa vào lời kể: `git log --since="8 days ago" --stat`, số TODO còn lại trong `thuyet-minh/`, số dòng trong ma trận tổng quan, số phiếu đọc.
3. Hỏi người dùng những gì git không thể hiện (đã đăng ký lịch trình bày chưa, thầy trả lời gì).
4. Đề xuất trạng thái mới (Chưa làm, Đang làm, Xong) cho từng tuần trong lịch trình, sửa sau khi người dùng đồng ý.
5. Tạo biên bản `docs/bien-ban-hop/<yyyy-mm-dd>.md` theo `_mau.md`, điền việc tuần trước kèm bằng chứng (commit, file), vướng mắc, quyết định, việc tuần này.
6. Câu hỏi mới cho thầy thì thêm vào `docs/ke-hoach/cau-hoi-cho-thay.md`. Câu trả lời mới của thầy thì ghi vào cột cuối và báo những file cần sửa theo.

## Đầu ra

Một bảng ngắn: việc tuần này, người, hạn. Nếu đang trễ hơn một tuần so với lịch, đề xuất cụ thể việc cắt bớt hoặc dồn lại để vẫn có PDF trước ngày 06/12/2026, và nhắc rằng điểm tối đa giảm theo tuần trình bày.
