---
name: viet-muc-thuyet-minh
description: Viết nháp hoặc sửa một mục của thuyết minh đề tài NCKH sinh viên (mục 1 đến 16), đối chiếu chỉ dẫn mẫu, barem Bài tập 2 và các mục liên quan. Dùng khi người dùng muốn viết, sửa, rút gọn hay góp ý một mục, ví dụ "/viet-muc-thuyet-minh 10".
argument-hint: "<số mục: 1-16> [viết | sửa | góp ý]"
---

# Viết một mục thuyết minh

## Đầu vào

Số mục và kiểu việc: viết nháp mới, sửa bản đang có, hoặc chỉ góp ý. Không nói kiểu việc thì: mục còn toàn TODO là viết nháp, mục đã có chữ là góp ý trước rồi hỏi có sửa không.

## Đọc trước khi viết

1. File của mục trong `thuyet-minh/` (bảng tra trong `thuyet-minh/README.md`), nhất là khối `<!-- HƯỚNG DẪN -->` ở đầu.
2. Dòng tương ứng trong `docs/yeu-cau/barem-bai-tap-2.md` và phần liên quan trong `docs/yeu-cau/kien-thuc-slide.md`.
3. Các mục phải khớp với mục đang viết:

| Mục đang viết | Phải khớp với |
| --- | --- |
| 1 | 10, 11, `00-bia.md` |
| 8 | `tong-quan/ma-tran-tong-quan.md`, phiếu đọc, mục 9 |
| 9 | 8 (khoảng trống), 10 |
| 10 | 1, 9, 13.1 |
| 11 | 1, 10, 12 |
| 12 | 10, 11, `nghien-cuu/huong-dan-gan-nhan.md`, `nghien-cuu/du-lieu/README.md` |
| 13 | 3, 5, 10, 16 |
| 14 | 10, 12 |
| 16 | 2, 13.2 |

4. Với mục 12, gọi agent `thiet-ke-phuong-phap` trước nếu mục còn trống.

## Khi viết

- Viết tiếng Việt, theo skill `viet-van-khong-rap-khuon` nếu có trong máy. Không mở bài bằng bối cảnh chung chung, không từ nối sáo đầu câu, không gạch ngang dài giữa câu, không in đậm trong thân bài.
- Dùng khái niệm của slide (khoảng trống nghiên cứu, FINER, mục tiêu đo được, đối tượng và khách thể, bias) vì người chấm là giảng viên soạn slide.
- Nội dung lấy từ người dùng, từ phiếu đọc và từ các mục khác. Câu cần nguồn mà phiếu đọc chưa có thì ghi `[CẦN NGUỒN]`. Không bịa số liệu, tên bộ dữ liệu, kết quả.
- Trích dẫn bằng `[n]`. Tài liệu mới chưa có trong `99-tai-lieu-tham-khao.md` thì dùng skill `trich-dan-ieee` để thêm và đánh số lại.
- Đoạn văn dài hơn một đoạn do Claude viết thì đặt `[TỰ VIẾT LẠI]` ở cuối, để người phụ trách diễn đạt lại bằng lời mình và giải thích được khi trình bày.
- Giữ nguyên khối hướng dẫn và tiêu đề mục theo mẫu. Chỉ sửa mục được yêu cầu.

## Sau khi viết

1. Chạy checklist trong khối hướng dẫn của mục, báo từng dòng đạt hay chưa.
2. Liệt kê chỗ không khớp với mục liên quan (bảng trên) và đề xuất sửa, không tự sửa mục khác.
3. Đếm `[TODO`, `[CẦN NGUỒN]`, `[TỰ VIẾT LẠI]` còn lại trong mục.
4. Gợi ý commit: `[muc-XX] <việc vừa làm>`.
