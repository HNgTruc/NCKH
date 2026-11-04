---
name: kiem-tra-truoc-nop
description: Kiểm tra toàn bộ bản thuyết minh trước khi nộp hoặc khi muốn rà bản nháp, theo đề cuối kì, barem Bài tập 2 và mẫu 16 mục, có phản biện độc lập. Dùng ở tuần 5, trước khi xuất PDF, hoặc khi người dùng hỏi bản thảo còn thiếu gì.
---

# Kiểm tra trước khi nộp

## Các bước

1. Đếm dấu hiệu chưa xong trong các file `thuyet-minh/` bắt đầu bằng số: `[TODO`, `[CẦN NGUỒN]`, `[TỰ VIẾT LẠI]`, `[?]`. Liệt kê theo file và dòng.
2. Kiểm tra cấu trúc theo `docs/yeu-cau/mau-thuyet-minh-16-muc.md`: đủ mục 1 đến 16, đúng tên mục, đủ cột các bảng mục 5, 7, 13.2, 14, 16.
3. Kiểm tra theo bảng dưới.

| # | Kiểm tra | Cách làm |
| --- | --- | --- |
| 1 | Tên đề tài 10 đến 15 từ, giống hệt ở bìa | Đếm từ, so `00-bia.md` |
| 2 | Mục 8 có ưu và nhược điểm cho từng nghiên cứu, kết thúc bằng khoảng trống | Đọc 8.4 |
| 3 | Mục 9 có ít nhất 2 số liệu có `[n]` | Đếm |
| 4 | Mục 10 có 1 mục tiêu tổng quát, 3 đến 5 MT, 5 câu hỏi gắn MT | Đếm |
| 5 | Mỗi MT có nội dung ở 13.1 và công việc ở 13.2 | Đối chiếu |
| 6 | Tổng thời gian 13.2 bằng số tháng mục 3 | Tính |
| 7 | Người thực hiện ở 13.2 có trong mục 5 | Đối chiếu |
| 8 | Mục 12 có nguồn dữ liệu, cách thu thập, gán nhãn, chỉ số, đạo đức, bias | Đọc |
| 9 | Mục 16 cộng đúng tổng, có số tiền bằng chữ | Tính |
| 10 | Trích dẫn IEEE khớp danh mục | Skill `trich-dan-ieee`, chế độ rà |
| 11 | Có Kết luận và kiến nghị (Bài tập 2) | Đọc 15.3 |
| 12 | Văn xuôi không có "Trong thời đại", "—", in đậm trong thân bài | Tìm chuỗi |

4. Gọi song song hai agent, mỗi agent chỉ nhận đường dẫn file, không nhận nhận xét của bước 1 đến 3, để chúng đọc với con mắt mới:
   - `phan-bien-thuyet-minh`: chấm theo barem.
   - `kiem-tra-trich-dan`: xác minh từng tài liệu tham khảo.
5. Kiểm tra file nộp nếu đã có: tên dạng `PPNCKH_MSSV1_MSSV2_MSSV3.pdf`, có trang bìa theo PhuLuc_3_Bia.

## Đầu ra

Ghi báo cáo vào `docs/ke-hoach/bao-cao-kiem-tra-<yyyy-mm-dd>.md`: bảng kết quả 12 dòng, kết quả hai agent, danh sách việc cần sửa xếp theo mức ảnh hưởng tới điểm, mỗi việc ghi mục và người phụ trách (theo `docs/ke-hoach/phan-cong.md`). Trả lời người dùng bằng 3 việc quan trọng nhất và đường dẫn báo cáo.

Không tự sửa thuyết minh trong skill này.
