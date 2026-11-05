# Lộ trình nộp thuyết minh (bản dồn)

Ngày 06/11/2026 Trúc báo nhóm 5 nộp PDF và trình bày cùng ngày thứ Ba 10/11/2026, và muốn có kết quả chạy thật trước khi nộp. Lịch 6 tuần cũ (hạn 06/12) không còn dùng được, xem lại trong lịch sử git nếu cần. Bản trên Claude Docs ([Lịch trình đồ án PPNCKH](https://claude.ai/artifact/5dLNj8WykNyfFiK7Rh71MT)) vẫn là lịch 6 tuần cũ, chưa cập nhật.

Thuyết minh xong trong ba ngày 06/11 đến 08/11, thứ Hai 09/11 dành cho sửa, xuất PDF, làm slide và tập. Như vậy nếu một ngày bị trễ vẫn còn thứ Hai làm đệm.

Trạng thái dùng một trong ba giá trị: Chưa làm, Đang làm, Xong. Trúc làm toàn bộ, nên không có cột phụ trách.

## Nguyên tắc ưu tiên

1. Thuyết minh đủ 16 mục là phần bắt buộc, thiếu mục nào mất điểm mục đó. Kết quả chạy thật là phần cộng thêm: thuyết minh là bản đề xuất, mẫu không đòi kết quả.
2. Vì vậy kết quả thật làm dưới dạng thử nghiệm sơ bộ (pilot) cỡ nhỏ, chạy song song, và là thứ bị cắt đầu tiên khi trễ. Các mốc cắt ghi ở mục "Điểm dừng".
3. Mọi đoạn Claude viết nháp, Trúc phải tự giải thích được trước buổi trình bày. Thời gian tự viết lại các chỗ `[TỰ VIẾT LẠI]` đã xếp riêng vào tối Chủ nhật, không được bỏ.

## Đã xong đến 06/11

| Việc | Bằng chứng |
| --- | --- |
| Chốt tên đề tài, phạm vi chỉ SMS, 3 nhãn | Commit `e298af9`, `thuyet-minh/01-07-thong-tin-chung.md` |
| Danh sách 20 bài, đã xác minh metadata | `tong-quan/ma-tran-tong-quan.md`, phần "Ứng viên cần kiểm tra" |
| 11 phiếu đọc, 11 dòng ma trận tổng quan | `tong-quan/phieu-doc/` (8 file chưa commit) |
| Câu khoảng trống có bằng chứng từng ý | Cuối `tong-quan/ma-tran-tong-quan.md` |
| 5 số liệu chính thống và 2 văn bản pháp luật | `tong-quan/so-lieu.md` (chưa commit) |
| Bản đề xuất hướng dẫn gán nhãn 3 nhãn | `nghien-cuu/huong-dan-gan-nhan.md` |

## Lộ trình theo ngày

Hai luồng chạy song song. Luồng T là thuyết minh, luồng P là thử nghiệm sơ bộ. Cột "Công cụ" là skill hoặc agent dùng cho việc đó.

### Thứ Sáu 06/11 (tối)

| Luồng | Việc | Công cụ | Sản phẩm | Trạng thái |
| --- | --- | --- | --- | --- |
| T | Commit các file đang dở (lệnh ở cuối file này) | | 3 commit | Chưa làm |
| T | Hỏi lớp kênh nộp và giới hạn trang. Ghi vào `gia-dinh.md` dòng 2, 6. Ngày nộp đã biết: thứ Ba 10/11 | | Kênh nộp | Chưa làm |
| T | Xin Khang và Nhân họ tên đầy đủ, MSSV, lớp (cần cho bìa, mục 5 và tên file PDF). Đã ghi vai: Khang B, Nhân C | | Đủ thông tin mục 4, 5 | Đang làm |
| P | Nhắn bạn bè, người thân xin tin SMS lừa đảo và quảng cáo họ nhận được (chụp màn hình hoặc chép nội dung), nói rõ sẽ xóa số điện thoại, tên trước khi dùng. Làm sớm vì phải chờ người khác trả lời | | Tin nhắn gửi về | Chưa làm |
| P | Xuất SMS trong điện thoại Trúc ra file, lưu vào `nghien-cuu/du-lieu/raw/` | | File thô trong `raw/` | Chưa làm |
| P | Claude viết script ẩn danh (thay số điện thoại, số tài khoản, số thẻ, OTP, email bằng thẻ như `<SDT>`) và notebook Colab chạy mô hình, có chú thích tiếng Việt từng bước | | `nghien-cuu/src/`, `nghien-cuu/notebooks/` | Chưa làm |
| T | Viết mục 10: 1 mục tiêu tổng quát, 4 mục tiêu cụ thể, 5 câu hỏi nghiên cứu. Mục này làm trước vì mục 11 đến 14 bám theo nó | `viet-muc-thuyet-minh 10` | Mục 10 | Chưa làm |

### Thứ Bảy 07/11

| Buổi | Luồng | Việc | Công cụ | Sản phẩm | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| Sáng | T | Tìm bổ sung tối đa 1 giờ: Google Scholar với "Vietnamese smishing", "Vietnamese SMS scam", "SMS lừa đảo tiếng Việt"; mở bài RIVF 2023 và IDEAL 2024 xem có tách lừa đảo không. Hết giờ thì dừng, câu khoảng trống ghi "trong phạm vi đã tìm" | `tong-quan-tai-lieu` | Nhật ký tìm kiếm, câu khoảng trống đã kiểm | Chưa làm |
| Sáng | T | Viết mục 11 và mục 8 từ ma trận tổng quan | `viet-muc-thuyet-minh 11`, `viet-muc-thuyet-minh 8` | Mục 8, 11 | Chưa làm |
| Sáng | P | Chạy script ẩn danh trên `raw/`, tự đọc lại từng tin xem còn sót tên, địa chỉ không, rồi lưu vào `processed/`. Claude không đọc `raw/` | Script ẩn danh | File trong `processed/` | Chưa làm |
| Chiều | T | Viết mục 9 từ `tong-quan/so-lieu.md` | `viet-muc-thuyet-minh 9` | Mục 9 | Chưa làm |
| Chiều | T | Thiết kế và viết mục 12 (dữ liệu, gán nhãn, mô hình, chỉ số, đạo đức, bias) | `thiet-ke-phuong-phap`, `viet-muc-thuyet-minh 12` | Mục 12 | Chưa làm |
| Chiều | P | Gán nhãn toàn bộ tin trong `processed/` theo 3 nhãn. Nhờ một người gán độc lập 100 tin để tính Cohen's kappa | `huong-dan-gan-nhan.md` | Bảng đã gán nhãn | Chưa làm |
| Tối | P | Chạy mô hình cơ sở TF-IDF + Logistic Regression trên Colab, ghi số liệu | Notebook | Bảng kết quả mô hình cơ sở | Chưa làm |

### Chủ nhật 08/11

| Buổi | Luồng | Việc | Công cụ | Sản phẩm | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| Sáng | P | Chạy PhoBERT-base trên Colab (GPU miễn phí). Để máy chạy, làm luồng T trong lúc chờ | Notebook | Bảng so sánh 2 mô hình | Chưa làm |
| Sáng | T | Viết mục 13, 14, 15, 16 và mục 1 đến 7, bìa | `viet-muc-thuyet-minh` | Đủ 16 mục | Chưa làm |
| 12:00 | P | Điểm dừng 1 (xem dưới) | | | Chưa làm |
| Chiều | T | Đưa kết quả thử nghiệm sơ bộ vào thuyết minh (chỗ đặt: Trúc chốt) | | Đoạn kết quả sơ bộ | Chưa làm |
| Chiều | T | Lập danh sách tài liệu tham khảo, đánh số IEEE theo thứ tự xuất hiện | `trich-dan-ieee` | Mục 99 | Chưa làm |
| Chiều | T | Ghép file, chạy phản biện và kiểm tra trích dẫn | `./scripts/build.ps1`, `phan-bien-thuyet-minh`, `kiem-tra-trich-dan` | Danh sách lỗi cần sửa | Chưa làm |
| Tối | T | Tự viết lại mọi đoạn `[TỰ VIẾT LẠI]` bằng lời của mình. Đây là phần Trúc sẽ bị hỏi khi trình bày | | 0 chỗ `[TỰ VIẾT LẠI]` | Chưa làm |

### Thứ Hai 09/11

| Buổi | Luồng | Việc | Công cụ | Sản phẩm | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| Sáng | T | Sửa theo phản biện. Điền nốt họ tên, MSSV, lớp của Khang và Nhân | | Bản sửa | Chưa làm |
| Sáng | T | Chạy kiểm tra cuối, xuất PDF tên `PPNCKH_MSSV1_MSSV2_MSSV3.pdf`, bìa theo PhuLuc_3 | `kiem-tra-truoc-nop` | PDF nộp được | Chưa làm |
| Chiều | T | Làm slide từ `trinh-bay/dan-y-slide.md`, thêm 1 slide kết quả sơ bộ nếu có. Điền tên Khang, Nhân vào cột "Người nói" | | Slide | Chưa làm |
| Tối | T | Tập nói 2 lần, bấm giờ 10 phút. Tập trả lời các câu hỏi cuối `dan-y-slide.md`, nhất là câu về dữ liệu và câu "chưa biết Python" | | Đã tập 2 lần | Chưa làm |
| Tối | T | In bản giấy | | Bản in | Chưa làm |

### Thứ Ba 10/11 (nộp và trình bày)

| Buổi | Việc | Sản phẩm | Trạng thái |
| --- | --- | --- | --- |
| Trước giờ nộp | Đọc lại slide một lượt, nộp PDF qua kênh lớp quy định | Đã nộp | Chưa làm |
| Theo lịch lớp | Trình bày, ghi lại câu hỏi và góp ý của thầy | Ghi chú góp ý | Chưa làm |
| Sau buổi | Nộp bản giấy Văn phòng Khoa | Đã nộp bản giấy | Chưa làm |

## Điểm dừng cho luồng P

| Mốc | Nếu chưa đạt | Thì |
| --- | --- | --- |
| 12:00 Chủ nhật 08/11: có bảng đã gán nhãn trong `processed/` | Chưa có | Bỏ PhoBERT. Chỉ báo thống kê mô tả (số tin mỗi nhãn, tỉ lệ không dấu) |
| Tối Chủ nhật 08/11: có ít nhất số liệu mô hình cơ sở | Chưa có | Bỏ hẳn luồng P. Thuyết minh chỉ mô tả kế hoạch. Sáng thứ Hai không được dùng để chạy mô hình, vì phải xuất PDF |
| Lớp `LUA_DAO` có dưới khoảng 30 tin | | Vẫn báo số, nhưng ghi rõ là cỡ mẫu quá nhỏ để kết luận, chỉ chứng minh quy trình chạy được |

## Thử nghiệm sơ bộ (đề xuất, Trúc chốt trước khi chạy)

| Thành phần | Đề xuất | Vì sao |
| --- | --- | --- |
| Dữ liệu | Khoảng 300 tin từ điện thoại Trúc và người đồng ý chia sẻ, đã ẩn danh | Thu được trong 1 ngày, đủ để thử quy trình |
| Gán nhãn | Trúc gán hết, một người khác gán lại 100 tin, tính Cohen's kappa | Kappa cho biết hai người hiểu nhãn giống nhau tới đâu. Ví dụ hai người cùng gọi tin "Vietcombank: tài khoản bị khóa, bấm link" là lừa đảo thì đồng thuận |
| Mô hình cơ sở | TF-IDF + Logistic Regression | Chạy vài giây, là mốc để so. vu-2023-nhung-tu cũng dùng TF-IDF làm cơ sở |
| Mô hình chính | PhoBERT-base | Mô hình chính của đề tài |
| Chia dữ liệu | Chia 5 phần, lần lượt lấy 1 phần làm kiểm tra (5-fold, phân tầng theo nhãn), cố định random seed | Với 300 tin, một tập kiểm tra 60 tin cho kết quả dao động mạnh. Chia 5 lần rồi lấy trung bình ổn hơn |
| Chỉ số | F1 lớp `LUA_DAO`, F1 trung bình macro, ma trận nhầm lẫn | Tin lừa đảo ít hơn tin thường. Mô hình đoán "bình thường" cho mọi tin vẫn đạt accuracy cao mà không bắt được tin lừa đảo nào |

## Quyết định Trúc cần chốt

| Quyết định | Hạn chốt | Ghi vào |
| --- | --- | --- |
| Kênh nộp, giới hạn trang | Tối 06/11 | `gia-dinh.md` dòng 2, 6 |
| Họ tên đầy đủ, MSSV, lớp của Khang và Nhân | Sáng 09/11 | Bìa, mục 5, `phan-cong.md` |
| Các thông số thử nghiệm sơ bộ ở bảng trên | Tối 06/11 | Notebook, mục 12 |
| Mục tiêu cụ thể và câu hỏi nghiên cứu | Tối 06/11 | Mục 10 |
| Chỗ đặt kết quả sơ bộ trong thuyết minh (mẫu không có mục riêng) | Chiều 08/11 | Mục 12 hoặc mục khác |
| Loại đề tài, thời gian thực hiện, kinh phí | Sáng 08/11 | Mục 2, 3, 16 |
| Chỗ đặt "Kết luận và kiến nghị" | Sáng 08/11 | `gia-dinh.md` dòng 3 |
| Năng lực từng người cho mục 6 | Sáng 08/11 | `phan-cong.md`, mục 6 |
| Bản giấy có cần đóng bìa, ký tên | Trước ngày nộp | `gia-dinh.md` dòng 7 |

## Sau khi nộp

Thử nghiệm sơ bộ là bước đầu của việc làm thật đề tài. Sau buổi trình bày, các bước tiếp theo theo `nghien-cuu/README.md`: mở rộng nguồn dữ liệu và ghi điều khoản vào `nghien-cuu/du-lieu/README.md`, gán nhãn với đủ người, chạy thêm ViSoBERT, kiểm tra mô hình trên tin không dấu. Lịch chi tiết lập lại sau khi nộp, theo bảng tiến độ ở mục 13.2.

## Lệnh commit cho phần đang dở

Trúc tự chạy:

```powershell
git add tong-quan/phieu-doc/ tong-quan/ma-tran-tong-quan.md
git commit -m "[tong-quan] phieu doc 8 bai, cap nhat ma tran tong quan"

git add tong-quan/so-lieu.md
git commit -m "[tong-quan] so lieu lua dao truc tuyen va van ban phap luat"

git add docs/ke-hoach/gia-dinh.md docs/ke-hoach/lich-trinh.md docs/ke-hoach/phan-cong.md CLAUDE.md
git commit -m "[ke-hoach] don lich nop 10/11, vai tro Khang Nhan"

git add thuyet-minh/00-bia.md thuyet-minh/01-07-thong-tin-chung.md
git commit -m "[muc-05] ten thanh vien, thang nop tren bia"
```
