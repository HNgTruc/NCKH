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

## Quy trình

1. Hai người gán độc lập trên cùng một mẫu thử 100 tin.
2. Tính độ đồng thuận bằng Cohen's kappa. Kappa đo mức hai người đồng ý sau khi trừ phần trùng do ngẫu nhiên. Nhóm tự đặt ngưỡng chấp nhận và ghi lý do vào mục 12.
3. Họp xử lý các tin bất đồng, sửa hướng dẫn này.
4. Gán phần còn lại. Một người thứ ba kiểm tra ngẫu nhiên một phần mẫu.

## Ẩn danh hóa trước khi gán

| Thông tin | Thay bằng |
| --- | --- |
| Số điện thoại | `<SDT>` |
| Số tài khoản, số thẻ | `<STK>` |
| Họ tên người thật | `<TEN>` |
| Mã OTP, mật khẩu | `<MA>` |
| Đường link | `<URL>` và lưu tên miền ở cột riêng, vì tên miền là đặc trưng quan trọng |
| Email người nhận | `<EMAIL>` |
