# Hướng dẫn gán nhãn (bản đề xuất)

Bản này là đề xuất để nhóm bàn, chưa chốt. Phần gán nhãn có trong mục 12.3 của thuyết minh, nên khi nhóm chốt bộ nhãn thì cập nhật cả hai nơi.

## Bộ nhãn

Ranh giới giữa tin rác quảng cáo và tin lừa đảo dễ gây gán nhãn không thống nhất (labeling bias), nên đề xuất ba nhãn thay vì hai.

| Nhãn | Định nghĩa | Dấu hiệu thường gặp |
| --- | --- | --- |
| `LUA_DAO` | Tin cố ý lừa người nhận đưa tiền, mật khẩu, mã OTP, thông tin cá nhân, hoặc bấm link giả | Giả danh ngân hàng, cơ quan nhà nước, người quen; tạo gấp gáp; link tên miền lạ; đòi chuyển khoản |
| `QUANG_CAO` | Tin quảng cáo, khuyến mãi không giả danh và không đòi thông tin nhạy cảm | Tên doanh nghiệp rõ, cách hủy nhận tin |
| `BINH_THUONG` | Tin cá nhân, thông báo dịch vụ thật | |

Nếu cuối cùng chỉ cần phân loại hai lớp, gộp `QUANG_CAO` và `BINH_THUONG` thành `KHONG_LUA_DAO` khi huấn luyện. Giữ ba nhãn lúc gán giúp không mất thông tin.

## Quy tắc khi khó quyết định

1. Tin giả danh một tổ chức thật mà đòi bấm link hoặc cung cấp thông tin: `LUA_DAO`, kể cả khi lời lẽ lịch sự.
2. Tin chỉ có link rút gọn, không rõ nội dung: đánh dấu `KHONG_RO`, đưa ra họp nhóm, không tự đoán.
3. Ghi lý do ngắn cho mọi tin gán `LUA_DAO`, dùng để phân tích lỗi sau này.
4. Tin cờ bạc trực tuyến (nhà cái, nổ hũ, tài xỉu, "nạp đầu tặng"): `LUA_DAO`, vì tin dụ người nhận nạp tiền vào dịch vụ bất hợp pháp và thường kèm link rút gọn. Trúc chốt ngày 06/11/2026.
5. Tin hẹn hò, "sugar baby", hứa trả "trợ cấp" rồi mời sang Telegram hoặc Zalo: `LUA_DAO`, vì hứa trả tiền phi thực tế và dẫn sang kênh chat riêng. Trúc chốt ngày 06/11/2026.
6. Tin của nhà mạng hoặc doanh nghiệp gán theo nội dung, không theo thẻ (QC) hay (TB) ở đầu tin. Tin mời mua gói, khuyến mãi là `QUANG_CAO`, kể cả khi gắn thẻ (TB). Tin báo về gói hay tài khoản đang dùng (đăng ký thành công, hết data, gia hạn lỗi, OTP, biến động số dư) là `BINH_THUONG`. Trúc chốt ngày 06/11/2026.

## Quy trình

1. Hai người gán độc lập trên cùng một mẫu thử 100 tin.
2. Tính độ đồng thuận bằng Cohen's kappa. Kappa đo mức hai người đồng ý sau khi trừ phần trùng do ngẫu nhiên. Nhóm tự đặt ngưỡng chấp nhận và ghi lý do vào mục 12.
3. Họp xử lý các tin bất đồng, sửa hướng dẫn này.
4. Gán phần còn lại. Một người thứ ba kiểm tra ngẫu nhiên một phần mẫu.

## Cách duyệt file gán nhãn sơ bộ (bộ tran-2026)

1. Chạy `python nghien-cuu/src/gan_nhan_so_bo.py` từ thư mục gốc repo. Script tạo `nghien-cuu/du-lieu/processed/tran-2026/gan-nhan-so-bo.csv`.
2. Mở file bằng Excel, lọc cột `dot = 1` (600 tin cho thử nghiệm sơ bộ).
3. Đọc tin ở cột `message`, xem nhãn gợi ý ở cột `nhan_goi_y` và lý do ở cột `ly_do`. Gợi ý chỉ do quy tắc từ khóa đưa ra, có thể sai.
4. Điền nhãn cuối vào cột `nhan_chot`: `LUA_DAO`, `QUANG_CAO`, `BINH_THUONG` hoặc `KHONG_RO`. Đồng ý với gợi ý thì chép lại nhãn đó, không để trống.
5. Ghi lý do vào cột `ghi_chu` cho tin `LUA_DAO` (quy tắc 3) và cho mọi tin đổi khác gợi ý. Tin còn sót họ tên, địa chỉ thì ghi "còn tên" để xóa sau.
6. Không sửa các cột khác. Lưu lại đúng định dạng CSV UTF-8.

Bộ tran-2026 đã được tác giả ẩn danh bằng thẻ tiếng Anh (`[PHONE]`, `[BANK_ACC]`, `[MONEY]`, `[NUMBER]`, `[TIME]`, `[DATE]`). Giữ nguyên các thẻ này, không đổi sang thẻ tiếng Việt ở bảng dưới.

## Ẩn danh hóa trước khi gán

| Thông tin | Thay bằng |
| --- | --- |
| Số điện thoại | `<SDT>` |
| Số tài khoản, số thẻ | `<STK>` |
| Họ tên người thật | `<TEN>` |
| Mã OTP, mật khẩu | `<MA>` |
| Đường link | `<URL>` và lưu tên miền ở cột riêng, vì tên miền là đặc trưng quan trọng |
| Email người nhận | `<EMAIL>` |
