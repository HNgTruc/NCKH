# CLAUDE.md

Repo này là đồ án cuối kì môn Phương pháp nghiên cứu khoa học trong CNTT (mã 841324, Khoa CNTT, Trường Đại học Sài Gòn, giảng viên TS. Vũ Ngọc Thanh Sang). Sản phẩm nộp là bản thuyết minh đề tài NCKH sinh viên cấp trường theo mẫu 16 mục, đề tài "Phân loại tin nhắn SMS lừa đảo và quảng cáo tiếng Việt bằng PhoBERT" (chốt 04/11/2026, phạm vi chỉ SMS, đã bỏ email; điểm mới là tách tin lừa đảo khỏi tin rác quảng cáo, vì các bài trong nước chỉ phân loại spam/ham). Nhóm muốn làm thật đề tài sau khi môn kết thúc, nên `nghien-cuu/` dành cho dữ liệu và mô hình.

## Bối cảnh nhóm

| Thông tin | Giá trị |
| --- | --- |
| Thành viên | Huỳnh Ngọc Trúc (3123411312), [Thành viên 2], [Thành viên 3]. Trúc sẽ điền tên hai bạn khi viết báo cáo |
| Giới hạn | Tối đa 3 người mỗi nhóm (theo đề cuối kì) |
| Cách làm hiện tại | Trúc làm toàn bộ đồ án, không chia việc. Trong thuyết minh vẫn giữ cấu trúc nhóm 3 người và vai trò A, B, C; khi làm việc thì coi mọi vai là Trúc |
| Kỹ năng hiện có | Python và xử lý dữ liệu: chưa biết. Học máy, NLP: mới biết lý thuyết. Đọc bài báo tiếng Anh, trích dẫn IEEE: chưa biết |
| Ngôn ngữ làm việc | Tiếng Việt. Thuật ngữ chuyên ngành giữ tiếng Anh trong ngoặc ở lần đầu xuất hiện |

Vì nhóm mới học, khi giải thích một khái niệm (precision, recall, PhoBERT, Cohen's kappa...) hãy nói ngắn bằng ví dụ gắn với đề tài lừa đảo, không giảng lý thuyết dài.

## Bản đồ repo

| Thư mục | Nội dung | Ai sửa |
| --- | --- | --- |
| `docs/yeu-cau/` | Đề cuối kì, barem Bài tập 2, mẫu 16 mục, kiến thức slide. Đây là nguồn sự thật về yêu cầu | Chỉ sửa khi thầy đổi yêu cầu |
| `docs/ke-hoach/` | Lịch trình 6 tuần, phân công, giả định nhóm tự quyết, báo cáo kiểm tra | Cả nhóm |
| `docs/bien-ban-hop/` | Biên bản họp Chủ nhật hằng tuần | Người chủ trì họp |
| `thuyet-minh/` | Bản thảo thuyết minh, mỗi mục một file, đánh số theo mẫu | Người phụ trách mục đó |
| `tong-quan/` | Chiến lược tìm bài, ma trận tổng quan, phiếu đọc từng bài, `references.bib` | Vai trò B |
| `nghien-cuu/` | Dữ liệu, hướng dẫn gán nhãn, code sau này | Vai trò C |
| `trinh-bay/` | Dàn ý slide trình bày 10 phút | Cả nhóm |
| `scripts/` | `build.ps1` ghép các mục thành file .docx để duyệt | Vai trò A |
| `xuat-ban/` | File xuất ra, không đưa lên git | Tự sinh |

## Quy tắc bắt buộc

1. Không bịa nguồn, số liệu, tên bộ dữ liệu, kết quả mô hình. Câu nào cần nguồn mà chưa có thì ghi `[CẦN NGUỒN]` tại chỗ. Một tài liệu chỉ được đưa vào `thuyet-minh/99-tai-lieu-tham-khao.md` sau khi đã mở trang gốc và có phiếu đọc trong `tong-quan/phieu-doc/`.
2. Trích dẫn theo IEEE: số trong ngoặc vuông `[1]`, đánh theo thứ tự xuất hiện đầu tiên khi đọc từ mục 1 đến mục 16. Dùng skill `trich-dan-ieee` để đánh số lại.
3. Văn xuôi tiếng Việt viết theo skill `viet-van-khong-rap-khuon` nếu có trong máy: không mở bài "Trong thời đại 4.0", không từ nối sáo, không dấu gạch ngang dài giữa câu, không in đậm trong thân bài. Mẫu của trường yêu cầu bảng và tiêu đề thì giữ theo mẫu.
4. Thành viên phải giải thích được mọi câu trong phần mình phụ trách (đề giữa kì yêu cầu điều này, buổi trình bày cũng hỏi). Khi viết nháp hộ, đánh dấu chỗ người viết cần tự diễn đạt lại bằng `[TỰ VIẾT LẠI]` nếu đoạn đó dài hơn một đoạn văn.
5. Sửa đúng phần được yêu cầu. Không viết lại mục của người khác khi không ai nhờ.
6. Dữ liệu thô (tin nhắn, email có số điện thoại, tên, số tài khoản) chỉ nằm trong `nghien-cuu/du-lieu/raw/`, thư mục này bị chặn đọc trong `.claude/settings.json` và không đưa lên git. Chỉ làm việc với dữ liệu đã ẩn danh trong `processed/`.
7. Mỗi chỗ còn thiếu ghi `[TODO: ...]`. Trước khi nộp, `[TODO`, `[CẦN NGUỒN]`, `[TỰ VIẾT LẠI]` phải còn 0 lần xuất hiện.

## Quy trình theo tuần

Lịch chi tiết ở `docs/ke-hoach/lich-trinh.md`. Tóm tắt thứ tự công việc:

1. Chốt tên đề tài (skill `dat-ten-de-tai`) và đăng ký buổi trình bày sớm nhất có thể. Lịch học kỳ trước: hai tuần đầu tối đa 10 điểm, tuần thứ năm tối đa 8.5.
2. Tìm và đọc bài (skill `doc-bai-bao`, agent `tong-quan-tai-lieu`), điền ma trận tổng quan.
3. Viết mục 8, 9, 10, 11 (skill `viet-muc-thuyet-minh`).
4. Thiết kế phương pháp mục 12 (agent `thiet-ke-phuong-phap`), viết mục 2 đến 7 và 13 đến 16.
5. Kiểm tra trước khi nộp (skill `kiem-tra-truoc-nop`, gọi agent `phan-bien-thuyet-minh` và `kiem-tra-trich-dan`).
6. Trình bày, sửa theo góp ý, in nộp Văn phòng Khoa.

## Skills và agents

| Tên | Loại | Dùng khi |
| --- | --- | --- |
| `dat-ten-de-tai` | Skill | Đặt hoặc sửa tên đề tài, chấm FINER |
| `doc-bai-bao` | Skill | Có một bài báo mới cần đọc và đưa vào tổng quan |
| `viet-muc-thuyet-minh` | Skill | Viết hoặc sửa một mục thuyết minh, ví dụ `/viet-muc-thuyet-minh 10` |
| `trich-dan-ieee` | Skill | Thêm tài liệu, đánh số lại, rà định dạng IEEE |
| `kiem-tra-truoc-nop` | Skill | Tuần 5, hoặc bất cứ lúc nào muốn biết bản thảo còn thiếu gì |
| `cap-nhat-tien-do` | Skill | Họp Chủ nhật: cập nhật trạng thái, ghi biên bản |
| `tong-quan-tai-lieu` | Agent | Tìm và đọc nhiều bài cùng lúc mà không làm đầy ngữ cảnh chính |
| `thiet-ke-phuong-phap` | Agent | Thiết kế dữ liệu, gán nhãn, mô hình, chỉ số, đạo đức cho mục 11 và 12 |
| `phan-bien-thuyet-minh` | Agent | Chấm bản thảo theo barem như một người phản biện chưa từng thấy bài |
| `kiem-tra-trich-dan` | Agent | Xác minh từng tài liệu tham khảo có thật và khớp với câu trích |

## Lệnh

```powershell
# Ghép các mục thuyết minh thành file Word để đọc duyệt (cần pandoc)
./scripts/build.ps1

# Tìm chỗ còn thiếu
git grep -n -E "\[TODO|\[CẦN NGUỒN\]|\[TỰ VIẾT LẠI\]" -- thuyet-minh
```

## Quy ước git

Commit nhỏ, mỗi commit một mục. Tiêu đề commit dạng `[muc-08] them 3 bai vao tong quan` hoặc `[tong-quan] phieu doc PhoBERT`. Kéo về (`git pull`) trước khi sửa, vì ba người cùng viết.

Claude không tự chạy `git add`, `git commit`, `git push`. Trúc tự commit. Xong một việc, Claude đưa danh sách lệnh đã chia theo từng commit (file cần `git add`, tiêu đề commit theo dạng trên) để Trúc tự chạy.
