---
name: doc-bai-bao
description: Đọc một bài báo khoa học và đưa vào tổng quan của nhóm, gồm kiểm tra chỉ mục Scopus/WoS, điền phiếu đọc, thêm dòng ma trận tổng quan và soạn trích dẫn IEEE. Dùng khi người dùng đưa DOI, link, tên bài hoặc file PDF bài báo.
argument-hint: "<DOI | link | đường dẫn PDF | tên bài>"
---

# Đọc một bài báo

## Đầu vào

Một bài, qua DOI, link, tên, hoặc file PDF trong repo. Nhiều bài cùng lúc thì giao cho agent `tong-quan-tai-lieu`.

## Các bước

1. Lấy siêu dữ liệu từ nguồn chính thức: trang DOI (`https://doi.org/...`), trang nhà xuất bản, ACL Anthology, IEEE Xplore, hoặc Crossref (`https://api.crossref.org/works/<DOI>`). Không lấy từ đoạn trích của kết quả tìm kiếm. Không mở được trang gốc thì dừng và báo người dùng.
2. Kiểm tra nơi đăng: tra tên tạp chí trên SCImago để lấy Scopus, hạng Q, lĩnh vực. Hội nghị thì tra CORE. Ghi link làm bằng chứng. Preprint arXiv chưa đăng chính thức thì ghi rõ "preprint".
3. Kiểm tra trùng: tìm trong `tong-quan/phieu-doc/` và `tong-quan/ma-tran-tong-quan.md`. Đã có thì chỉ bổ sung.
4. Tạo phiếu `tong-quan/phieu-doc/<tacgia-nam-tukhoa>.md` theo `_mau.md`. Mỗi ô nội dung ghi số trang hoặc số bảng. Ô nào bài không nêu thì ghi "Bài không nêu". Phần "Nhận xét của nhóm" là đề xuất của Claude, ghi rõ để thành viên sửa lại theo ý mình.
5. Thêm một dòng vào bảng chính của `tong-quan/ma-tran-tong-quan.md`. Nếu bài nằm trong bảng "Ứng viên cần kiểm tra" thì chuyển trạng thái thành "Đã có phiếu".
6. Soạn trích dẫn IEEE trong phiếu (định dạng ở skill `trich-dan-ieee`). Chưa thêm vào `thuyet-minh/99-tai-lieu-tham-khao.md` cho tới khi bài được trích trong một mục thuyết minh.
7. Nhắc người dùng thêm bài vào Zotero để `references.bib` cập nhật.

## Đầu ra cho người dùng

Ba đến năm câu: bài làm gì, trên dữ liệu gì, kết quả chính kèm số, hạn chế, dùng được cho mục nào của thuyết minh. Giải thích bằng ví dụ gắn với đề tài lừa đảo nếu bài dùng khái niệm nhóm chưa học.

## Không làm

- Không điền số liệu, kết quả, tên bộ dữ liệu mà bài không ghi.
- Không chép nguyên văn quá một câu. Câu chép nguyên văn để trong ngoặc kép kèm số trang.
