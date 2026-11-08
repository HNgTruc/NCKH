<!-- HƯỚNG DẪN
Mẫu: Khả năng ứng dụng và phát triển của đề tài (không có chỉ dẫn thêm).
Slide Chương 4: tiêu chí khả áp dụng gồm khả thi công nghệ, kinh tế, xã hội, khả năng mở rộng, bền vững. Lĩnh vực áp dụng: giáo dục, công nghiệp và công nghệ, chính sách công.
Bài tập 2 có thêm "Kết luận và kiến nghị" mà mẫu không có. Tạm để ở 15.3, chờ Trúc quyết (docs/ke-hoach/gia-dinh.md, dòng 3).

Checklist:
- Ứng dụng nêu người dùng cụ thể (ai dùng, dùng thế nào)
- Hướng phát triển nêu điều đề tài cố ý chưa làm ở phạm vi mục 11
- Không hứa triển khai thương mại
-->

## 15. Khả năng ứng dụng và phát triển của đề tài

### 15.1. Khả năng ứng dụng

| Người dùng | Dùng thế nào |
| --- | --- |
| Nhóm nghiên cứu xử lý ngôn ngữ tiếng Việt | Dùng hướng dẫn gán nhãn và bộ nhãn ba lớp (mã tin kèm nhãn) để gán thêm dữ liệu hoặc so sánh mô hình trên cùng bộ nhãn |
| Đơn vị phát triển ứng dụng lọc tin nhắn | Tham khảo kết quả so sánh ba mô hình và mức giảm F1 khi tin bị viết biến dạng khi chọn mô hình cho bộ lọc |
| Giảng viên, sinh viên Khoa Công nghệ Thông tin | Dùng notebook làm ví dụ thực hành phân loại văn bản tiếng Việt từ khâu gán nhãn đến đánh giá |

Đề tài không triển khai sản phẩm thương mại và không tích hợp vào hệ thống của nhà mạng.

### 15.2. Hướng phát triển

Các việc dưới đây nằm ngoài phạm vi 2 tháng ở mục 11, nhóm dự kiến làm sau khi kết thúc học phần:

- Gán nhãn toàn bộ 2.629 tin của bộ dữ liệu công khai, với hai người gán mù và người thứ ba phân xử.
- Thu thập thêm tin nhắn từ người tình nguyện có phiếu đồng ý, để giảm sai lệch do chỉ có một nguồn và để có tập kiểm tra theo thời gian.
- Gom các tin gần trùng trước khi chia tập, dùng một tập kiểm tra cố định và kiểm định bootstrap cho H1, H2.
- Xây bản demo phân loại một tin nhắn, chạy cục bộ, có giới hạn số lần gọi để hạn chế việc dùng ngược.

### 15.3. Kết luận và kiến nghị

Phần này báo kết quả thử nghiệm sơ bộ của học phần, chạy ngày 08/11/2026. Các mục khác của thuyết minh là kế hoạch. Các số dưới đây là kết quả sơ bộ trên 597 tin có nhãn rõ (600 tin, bỏ 3 tin `KHONG_RO`), chạy ngày 08/11/2026 với random seed 42, kiểm định chéo 5 phần. Mỗi phần kiểm tra có khoảng 120 tin, trong đó khoảng 39 tin lừa đảo. Bảng ghi F1 lớp lừa đảo theo dạng trung bình ± độ lệch chuẩn qua 5 phần.

| Mô hình | Tin gốc | Bỏ dấu thanh | Chèn ký tự | Xóa thẻ QC/TB |
| --- | --- | --- | --- | --- |
| TF-IDF + Logistic Regression | 91,9 ± 3,4 | 88,5 ± 3,9 | 91,7 ± 3,0 | 91,7 ± 3,0 |
| PhoBERT-base | 90,8 ± 2,9 | 82,2 ± 5,3 | 84,9 ± 3,1 | 89,1 ± 3,5 |
| ViSoBERT | 92,7 ± 4,0 | 86,5 ± 8,3 | 89,2 ± 2,7 | 90,2 ± 3,4 |

MT1 đạt một phần. Nhóm đã gán lại ba nhãn cho 600 tin theo hướng dẫn viết sẵn, nhưng kappa vòng đầu giữa người gán thứ hai và nhãn sơ bộ là 0,569, thấp hơn ngưỡng 0,60. Hai người bất đồng nhiều nhất ở tin mời mua, mời vay hoặc trúng thưởng của nhà mạng (17 trong 29 tin) và ở tin mã OTP (7 tin). Nhóm đã họp, bổ sung hai quy tắc vào hướng dẫn và chưa đo lại kappa. Khi chuyển nhãn gốc sang ba nhãn mới (CH2, ước lượng có trọng số), khoảng 95,9% tin gốc "rác hoặc lừa đảo" thành lừa đảo và 4,1% thành quảng cáo. Trong tin gốc "hợp lệ", 53,3% là quảng cáo và 45,9% là bình thường. Điều này cho thấy nhãn "hợp lệ" của bộ gốc gộp nhiều tin quảng cáo.

MT2 đã thực hiện đủ ba mô hình. Ở tin gốc, F1 lớp lừa đảo của ba mô hình chênh nhau trong khoảng 2 điểm, nhỏ hơn độ lệch chuẩn giữa các phần, nên chưa thể nói mô hình nào tốt hơn. Về nhầm lẫn giữa lừa đảo và quảng cáo (CH4), mô hình cơ sở nhầm ít nhất (0,5% tin lừa đảo bị đoán là quảng cáo, 1,2% chiều ngược lại), PhoBERT nhầm 2,1% và 2,1%, ViSoBERT 1,5% và 1,7%.

H1 không được ủng hộ. F1 lớp lừa đảo của PhoBERT cao hơn mô hình cơ sở ở 1 trong 5 phần, bằng nhau ở 1 phần và thấp hơn ở 3 phần, chênh lệch trung bình là -1,1 điểm. Nhóm chưa rõ vì sao. Có hai khả năng, và dữ liệu hiện tại chưa phân biệt được. Một là 600 tin là quá ít (khoảng 478 tin huấn luyện mỗi phần) và hai mô hình transformer dùng chung cấu hình, không dò siêu tham số. Hai là nhiều tin trong mẫu là các mẫu tin lặp lại, nên TF-IDF nhận ra chúng dễ dàng.

H2 được ủng hộ ở mức sơ bộ. Khi bỏ dấu, F1 lớp lừa đảo của PhoBERT giảm 8,6 điểm và của ViSoBERT giảm 6,2 điểm. Mức giảm của PhoBERT lớn hơn ở 4 trong 5 phần, chênh lệch trung bình 2,4 điểm. ViSoBERT có độ lệch chuẩn 8,3 sau khi bỏ dấu, nên kết quả này chưa chắc chắn. Mô hình cơ sở giảm ít nhất (3,4 điểm).

MT3 đã thực hiện. Khi chèn ký tự, F1 lớp lừa đảo giảm 5,9 điểm ở PhoBERT, 3,5 điểm ở ViSoBERT và 0,2 điểm ở mô hình cơ sở. Với phép thử xóa thẻ QC/TB, thẻ xuất hiện ở 78,8% tin quảng cáo, 13,5% tin bình thường và 0% tin lừa đảo. Sau khi xóa thẻ, F1 lớp lừa đảo giảm 1,7 điểm ở PhoBERT, 2,5 điểm ở ViSoBERT và 0,2 điểm ở mô hình cơ sở. F1 lớp quảng cáo của ViSoBERT giảm từ 91,9 xuống 86,8 và F1 lớp bình thường từ 84,5 xuống 77,0. Hai mô hình transformer có học một phần từ thẻ, nhưng ở lớp lừa đảo ảnh hưởng nhỏ vì tin lừa đảo không mang thẻ.

Các kết quả trên có bốn hạn chế. Mẫu chỉ 600 tin từ một bộ dữ liệu. Nhãn là nhãn sơ bộ do mô hình ngôn ngữ gán rồi người xem lại, kappa dưới ngưỡng. Tin gần trùng chưa được gom nhóm, nên kết quả có thể cao hơn thực tế. Chênh lệch giữa các mô hình nhỏ so với độ lệch chuẩn nên chỉ là bằng chứng sơ bộ.

Nhóm kiến nghị làm tiếp bốn việc. Gán nhãn toàn bộ 2.629 tin với hai người gán mù và đo lại kappa. Gom các tin gần trùng trước khi chia tập. Dùng tập kiểm tra cố định và kiểm định bootstrap cho H1, H2. Thử dò siêu tham số cho PhoBERT và ViSoBERT trên bộ dữ liệu lớn hơn trước khi kết luận về hai mô hình này so với mô hình cơ sở.
