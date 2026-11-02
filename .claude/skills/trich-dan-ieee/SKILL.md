---
name: trich-dan-ieee
description: Quản lý trích dẫn IEEE cho thuyết minh, gồm thêm tài liệu, đánh số lại theo thứ tự xuất hiện, đồng bộ danh mục tài liệu tham khảo và rà định dạng. Dùng khi thêm hoặc bỏ một nguồn, khi số [n] bị lệch, hoặc trước khi nộp.
argument-hint: "[thêm <mã bài> | đánh số lại | rà]"
---

# Trích dẫn IEEE

## Quy tắc

- Trong câu: `[1]`, nhiều nguồn `[1], [3]`, dãy liền `[2]-[4]`. Số đặt trước dấu chấm câu.
- Danh mục `thuyet-minh/99-tai-lieu-tham-khao.md` xếp theo thứ tự xuất hiện đầu tiên khi đọc các file `thuyet-minh/` theo tên (00, 01-07, 08... 16). Một nguồn trích nhiều lần giữ một số.
- Mọi `[n]` trong bài có đúng một dòng trong danh mục, và ngược lại.
- Chỉ thêm nguồn đã có phiếu trong `tong-quan/phieu-doc/`.

## Định dạng

| Loại | Mẫu |
| --- | --- |
| Bài tạp chí | `[n] A. B. Nguyen, C. Tran, and D. Le, "Title of article," Journal Name (viết tắt IEEE nếu có), vol. 12, no. 3, pp. 45-60, Mar. 2021, doi: 10.xxxx/xxxxx.` |
| Bài hội nghị | `[n] A. Author and B. Author, "Title of paper," in Proc. Conference Name (ACRONYM), City, Country, 2020, pp. 1-10, doi: ...` |
| Sách | `[n] A. Author, Title of Book, 2nd ed. City, Country: Publisher, 2016.` |
| Preprint | `[n] A. Author, "Title," arXiv:2001.00000, 2020.` |
| Bộ dữ liệu | `[n] A. Author, "Dataset name," Repository, Year. [Online]. Available: URL` |
| Trang web, báo cáo cơ quan | `[n] Tên cơ quan, "Tên trang hoặc báo cáo." Tên website. URL (truy cập dd/mm/yyyy).` |
| Tài liệu tiếng Việt | Giữ nguyên tiếng Việt có dấu, họ tên tác giả viết đủ theo thứ tự tiếng Việt: `[n] Vũ Cao Đàm, Giáo trình phương pháp luận nghiên cứu khoa học. Hà Nội: NXB Giáo dục Việt Nam, 2016.` |

Tới sáu tác giả thì ghi đủ, tên viết tắt trước họ, nối tác giả cuối bằng "and". Từ bảy tác giả trở lên ghi tác giả đầu và "et al.".

## Các bước

Thêm một nguồn:
1. Lấy dòng IEEE từ phiếu đọc. Đối chiếu lại tên bài, tác giả, năm, DOI với trang gốc.
2. Chèn `[?]` vào câu trích, rồi đánh số lại.

Đánh số lại:
1. Đọc các file `thuyet-minh/` có tên bắt đầu bằng số, theo thứ tự tên, bỏ qua khối `<!-- -->`.
2. Lập bảng số cũ sang số mới theo thứ tự xuất hiện đầu tiên.
3. Thay toàn bộ số trong bài và sắp lại danh mục. Báo người dùng bảng đổi số.

Rà:
1. Liệt kê `[n]` không có trong danh mục, dòng danh mục không được trích, số nhảy cóc.
2. Kiểm tra từng dòng theo bảng định dạng.
3. Với lần rà trước khi nộp, gọi agent `kiem-tra-trich-dan` để xác minh nguồn có thật và câu trích đúng ý nguồn.
