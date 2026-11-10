# Kịch bản thuyết trình 10 phút

Dành cho ba người nói: Trúc, Khang, Nhân. Mỗi người đọc phần mình, hiểu từng câu rồi nói lại bằng lời của mình, không đọc nguyên văn từ giấy. Thầy sẽ hỏi từng người về phần mình. Số liệu lấy từ thuyết minh và file `nghien-cuu/ket-qua/ket-qua-so-bo.json`, không có số nào khác.

Tổng thời gian khoảng 10 phút. Mỗi đoạn dưới đây dài vừa đủ thời gian ghi ở đầu. Nói hơi chậm, mỗi phút khoảng 130 từ.

## Cách chia phần

| Người | Slide | Thời gian |
| --- | --- | --- |
| Trúc | 1, 2, 8, 9, 10, 12 | khoảng 4:20 |
| Khang | 3, 4, 11 | khoảng 2:15 |
| Nhân | 5, 6, 7 | khoảng 3:15 |

## Slide 1. Tên đề tài (Trúc, 0:20)

"Em chào thầy. Nhóm 5 chúng em gồm Trúc, Khang và Nhân. Đề tài của nhóm là phân loại tin nhắn SMS lừa đảo và quảng cáo tiếng Việt bằng PhoBERT. Hôm nay nhóm trình bày kế hoạch đề tài và kết quả sơ bộ chạy ngày 8 tháng 11."

## Slide 2. Vấn đề (Trúc, 1:00)

"Lừa đảo trực tuyến đang gây thiệt hại lớn. Theo Cục Cảnh sát hình sự, giai đoạn 2020 đến 2025 cả nước có 24.295 vụ lừa đảo chiếm đoạt tài sản trên không gian mạng, thiệt hại gần 40.000 tỷ đồng. Riêng 11 tháng đầu năm 2025, thiệt hại ước tính trên 6.000 tỷ đồng.

Nhóm nói rõ là số liệu chính thức chưa tách riêng kênh SMS, nên đây là thiệt hại của lừa đảo trực tuyến nói chung.

Bên dưới là một tin lừa đảo trong bộ dữ liệu, đã được ẩn danh. Tin báo đơn hàng bị giữ vì thiếu cước và đòi chuyển khoản vào một số tài khoản. Người nhận lo gấp là dễ chuyển tiền."

Chuyển sang Khang: "Vậy các nghiên cứu hiện có đã làm gì? Em xin nhường Khang."

## Slide 3. Các nghiên cứu hiện có (Khang, 1:15)

"Nhóm đọc 20 tài liệu và chọn năm nghiên cứu tiêu biểu để đưa lên bảng. Điểm chung dễ thấy nhất là phần lớn chỉ chia hai lớp.

Bộ SMS tiếng Anh của Almeida năm 2011 có hơn 5.500 tin và chỉ có hai lớp. Hai nghiên cứu tiếng Việt, của Pham và Le-Hong năm 2016 và của Vu năm 2022, cũng chia hai lớp. Bộ năm 2016 xếp quảng cáo nhà mạng vào tin rác. Bộ công khai năm 2026 trên Hugging Face lại xếp quảng cáo nhà mạng vào tin hợp lệ. Hai bộ xếp ngược nhau.

Hệ quả là tin lừa đảo, loại làm người nhận mất tiền, luôn bị gộp với một loại tin ít nguy hiểm hơn. Có một ngoại lệ: bộ SMSVN của Hoàng Thị Hà năm 2022 có 11 nhãn, trong đó có nhãn Scam và Ads, nhưng gán đa nhãn nên một tin có thể mang nhiều nhãn cùng lúc. Nghiên cứu của Dinh năm 2022 có chia nhiều loại, nhưng dữ liệu là đánh giá sản phẩm, không phải SMS.

Nhóm mới đọc tóm tắt bảy tài liệu, và đã ghi rõ ở mục 8.5 của thuyết minh."

## Slide 4. Khoảng trống (Khang, 0:30)

"Từ bảng trên, khoảng trống của đề tài là: trong phạm vi nhóm tìm được, chưa có nghiên cứu nào gán SMS tiếng Việt thành ba lớp loại trừ nhau là lừa đảo, quảng cáo và bình thường.

Nhóm nói là trong phạm vi nhóm tìm được, chứ không khẳng định chắc là chưa ai làm. Bộ SMSVN của Hoàng Thị Hà có nhãn lừa đảo, nhưng một tin có thể mang nhiều nhãn và bài không dùng mô hình tiền huấn luyện. Nên điểm mới của nhóm không nằm ở việc có nhãn lừa đảo, mà ở ba lớp loại trừ nhau, hướng dẫn gán nhãn có đo kappa, so sánh ba mô hình và đo độ bền khi tin bị biến dạng. Bộ lọc hiện nay chỉ báo được tin 'rác' hay 'không rác', trong khi tin lừa đảo mới là loại làm người nhận mất tiền."

Chuyển sang Nhân: "Từ khoảng trống đó, nhóm đặt mục tiêu như sau, xin nhường Nhân."

## Slide 5. Mục tiêu và giả thuyết (Nhân, 0:50)

"Đề tài có ba mục tiêu. Một là gán lại ba nhãn cho 600 tin SMS theo một hướng dẫn viết sẵn và đo độ đồng thuận giữa người gán bằng kappa, với mục tiêu từ 0,60. Hai là so sánh ba mô hình: TF-IDF kết hợp Logistic Regression làm mô hình cơ sở, PhoBERT và ViSoBERT, bằng kiểm định chéo 5 phần. Ba là đo xem F1 của lớp lừa đảo giảm bao nhiêu khi tin bị bỏ dấu, bị chèn ký tự hoặc bị xóa thẻ quảng cáo.

Có hai giả thuyết. H1: PhoBERT đạt F1 lớp lừa đảo cao hơn mô hình cơ sở. H2: khi bỏ dấu, F1 lớp lừa đảo của ViSoBERT giảm ít hơn PhoBERT. Với 600 tin thì cả hai chỉ là bằng chứng sơ bộ."

## Slide 6. Làm gì, không làm gì (Nhân, 0:40)

"Phạm vi được giữ gọn để làm trong hai tháng. Nhóm làm với SMS tiếng Việt lấy từ một bộ dữ liệu công khai, 2.629 tin sau khi bỏ trùng và dùng 600 tin. Nhãn gán theo nội dung tin.

Nhóm không làm ba việc: gán toàn bộ 2.629 tin, thu thêm tin nhắn và làm bản demo. Ba việc này để ở hướng phát triển. Nhóm cũng không xét tin Zalo, email hay cuộc gọi, không mở link trong tin và không dùng số điện thoại hay tên người gửi. Lý do không dùng tên người gửi là để mô hình học nội dung chứ không học đặc điểm người gửi."

## Slide 7. Phương pháp (Nhân, 1:45)

"Phương pháp gồm năm bước.

Bước một, thu thập. Nhóm dùng bộ SMS trên Hugging Face, giấy phép CC BY 4.0. Sau khi bỏ trùng còn 2.629 tin.

Bước hai, ẩn danh. Bộ dữ liệu đã được tác giả thay số điện thoại và số tiền bằng thẻ. Nhóm quét thêm số điện thoại và dãy số dài còn sót. Khi kiểm tra ngẫu nhiên 12 tin vẫn còn 1 tin có họ tên, nên nhóm không công bố nguyên văn tin.

Bước ba, gán nhãn. Script gợi ý nhãn bằng từ khóa rồi chọn ngẫu nhiên 200 tin cho mỗi nhóm gợi ý, tổng 600 tin. Nhãn sơ bộ do mô hình ngôn ngữ Claude gán theo hướng dẫn. Trúc xem lại 300 trong 600 tin. Khang gán độc lập 100 tin, không nhìn nhãn gợi ý, để đo kappa. Nhóm nói rõ điều này ở mục 12 của thuyết minh.

Bước bốn, ba mô hình. Mô hình cơ sở là TF-IDF kết hợp Logistic Regression. Mô hình chính là PhoBERT-base. Mô hình so sánh là ViSoBERT. Hai mô hình sau dùng cùng cấu hình, không dò siêu tham số.

Bước năm, đánh giá bằng kiểm định chéo 5 phần, đo precision, recall và F1 từng lớp. Nhóm không dùng accuracy làm chỉ số chính, vì tin bình thường chiếm đa số, một mô hình đoán toàn 'bình thường' vẫn có accuracy cao mà không bắt được tin lừa đảo nào. Mọi thứ chạy trong một notebook trên Google Colab, seed 42."

Chuyển sang Trúc: "Kết quả chạy ngày 8 tháng 11 như sau, xin nhường Trúc."

## Slide 8. Kết quả sơ bộ (Trúc, 1:30)

"Bảng này là F1 của lớp lừa đảo, tính trung bình và độ lệch chuẩn qua 5 phần, trên 597 tin có nhãn rõ. Ba tin gán 'không rõ' bị loại.

Ba điều nhóm muốn nói thẳng.

Một, kappa vòng đầu là 0,569, thấp hơn ngưỡng 0,60 nhóm tự đặt. Nhóm báo đúng con số. Hai người bất đồng 29 trong 100 tin, chủ yếu ở tin mời mua của nhà mạng và tin mã OTP. Nhóm đã họp, thêm hai quy tắc vào hướng dẫn gán nhãn. Nhóm chưa tính lại kappa, vì sau khi hai bên thống nhất thì số này không còn ý nghĩa.

Hai, giả thuyết H1 không được ủng hộ. PhoBERT chỉ cao hơn mô hình cơ sở ở 1 trong 5 phần. Có hai khả năng, nhóm chưa phân biệt được: mẫu quá nhỏ và không dò siêu tham số, hoặc nhiều tin trong mẫu theo mẫu lặp nên TF-IDF nhận ra dễ.

Ba, giả thuyết H2 đúng chiều nhưng chưa chắc. Khi bỏ dấu, PhoBERT giảm 8,6 điểm, ViSoBERT giảm 6,2 điểm. Nhưng độ lệch chuẩn của ViSoBERT là 8,3 nên nhóm chưa kết luận. Khi xóa thẻ quảng cáo, F1 lớp lừa đảo giảm khoảng 2 điểm ở hai mô hình transformer. Tin lừa đảo không mang thẻ nên ảnh hưởng nhỏ."

## Slide 9. Tiến độ (Trúc, 0:30)

"Về tiến độ, nhóm làm từ tháng 10 đến ngày 9 tháng 11. Tháng 10 xác định vấn đề và đọc tài liệu. Từ 1 đến 7 tháng 11 làm tổng quan và chốt tên đề tài, đồng thời chọn dữ liệu và viết hướng dẫn gán nhãn. Ngày 7 và 8 tháng 11 gán nhãn và đo kappa. Ngày 8 tháng 11 họp xử lý 29 tin bất đồng và chạy ba mô hình. Hôm nay, ngày 9, là hoàn thiện thuyết minh và tập trình bày."

## Slide 10. Sản phẩm và ứng dụng (Trúc, 0:40)

"Đề tài có bốn sản phẩm: mẫu 600 tin gán ba nhãn, chỉ công bố mã tin kèm nhãn chứ không công bố nguyên văn tin; hướng dẫn gán nhãn có tám quy tắc; notebook Google Colab chạy lại được; và báo cáo kết quả sơ bộ.

Người dùng có thể là nhóm nghiên cứu xử lý ngôn ngữ tiếng Việt, đơn vị làm ứng dụng lọc tin nhắn, và giảng viên, sinh viên dùng làm ví dụ thực hành. Đề tài không triển khai sản phẩm thương mại."

## Slide 11. Đạo đức và hạn chế (Khang, 0:30)

"Nhóm nêu thẳng các hạn chế. Về thông tin cá nhân, nhóm không công bố nguyên văn tin vì còn sót họ tên. Nhãn sơ bộ do mô hình ngôn ngữ gán nên nội dung tin đã được gửi tới dịch vụ của Anthropic, và Trúc mới xem lại 300 trong 600 tin. Nhóm cũng lo mô hình chỉ học lại luật từ khóa, nên báo tỉ lệ nhãn trùng với gợi ý là 87,3% và đo lại sau khi xóa thẻ quảng cáo. Mẫu nhỏ, một nguồn, nên kết quả chỉ là sơ bộ. Cuối cùng, nhóm chỉ báo số liệu tổng hợp và không phát hành công cụ chèn ký tự, để tránh bị dùng ngược né bộ lọc."

## Slide 12. Kết (Trúc, 0:20)

"Điều nhóm muốn mang đi là: nhãn ba lớp tách được tin lừa đảo khỏi tin quảng cáo, và trên mẫu 597 tin này, mô hình đơn giản chưa thua mô hình lớn. Nhóm xin cảm ơn thầy và xin nghe câu hỏi."

## Giải thích ngắn các thuật ngữ (để trả lời khi thầy hỏi)

| Thuật ngữ | Nói ngắn, ví dụ trong đề tài |
| --- | --- |
| Precision (độ chính xác của lớp) | Trong các tin mô hình báo là lừa đảo, bao nhiêu tin đúng là lừa đảo. Thấp nghĩa là báo nhầm nhiều |
| Recall (độ bắt được) | Trong các tin lừa đảo thật, mô hình bắt được bao nhiêu. Thấp nghĩa là bỏ sót nhiều |
| F1 | Trung bình điều hòa của precision và recall. Một con số để so sánh mô hình |
| Cohen's kappa | Mức hai người gán nhãn giống nhau sau khi trừ phần trùng do may mắn. 1 là hoàn toàn đồng ý, 0 là như đoán ngẫu nhiên. Nhóm đo được 0,569 trên 100 tin |
| Kiểm định chéo 5 phần | Chia 600 tin thành 5 phần, lần lượt lấy 1 phần làm kiểm tra, 4 phần để huấn luyện, rồi lấy trung bình. Dùng vì một tập kiểm tra nhỏ cho kết quả dao động mạnh |
| TF-IDF + Logistic Regression | Đếm từ nào xuất hiện nhiều trong tin này mà ít ở tin khác (ví dụ "xác minh", "bit.ly") rồi học trọng số cho từng từ để đoán nhãn. Mô hình cơ sở |
| PhoBERT | Mô hình ngôn ngữ đã được huấn luyện sẵn trên văn bản tiếng Việt. Nhóm tinh chỉnh (fine-tune) nó trên 597 tin để phân loại |
| ViSoBERT | Mô hình giống PhoBERT nhưng huấn luyện trên bình luận mạng xã hội, nên có thể chịu tin không dấu và viết tắt tốt hơn |
| Độ lệch chuẩn | Mức dao động của kết quả giữa 5 phần. Chênh lệch giữa hai mô hình nhỏ hơn độ lệch chuẩn thì chưa kết luận được |
| Thẻ QC, TB | Chữ (QC) hoặc (TB) ở đầu tin quảng cáo của nhà mạng. Nhóm xóa thẻ để kiểm tra mô hình có chỉ học thẻ hay không |

## Các câu thầy dễ hỏi

Mười câu hỏi và đáp ngắn nằm ở cuối file `dan-y-slide.md`. Ba câu khó nhất cần cả ba người cùng biết đáp:

1. Kappa dưới ngưỡng tự đặt mà không đo lại, và kappa này đo giữa ai với ai? Đáp: giữa Khang và nhãn sơ bộ do mô hình ngôn ngữ gán. Đã báo đúng con số, đã họp xử lý bất đồng, không đo lại vì sau khi hai bên thống nhất thì số này vô nghĩa. Đo lại trên mẫu mới là hướng phát triển.
2. Nhãn do mô hình ngôn ngữ gán thì có đáng tin không, và có vòng tròn với từ khóa không? Đáp: đã ghi trong thuyết minh như một hạn chế. Trúc xem lại 300 trong 600 tin, Khang gán độc lập 100 tin, và nhóm đo lại F1 sau khi xóa thẻ để xem mô hình có chỉ học luật từ khóa không.
3. PhoBERT không thắng mô hình cơ sở thì tên đề tài còn ý nghĩa gì? Đáp: đây là kết quả thật của mẫu 597 tin. Điểm mới của đề tài nằm ở nhãn ba lớp tách tin lừa đảo khỏi tin quảng cáo, không nằm ở việc PhoBERT thắng.

## Lưu ý khi đứng nói

- Nói thẳng các kết quả không tốt (kappa thấp, H1 không được ủng hộ). Nhóm đã ghi trong thuyết minh nên nói thẳng an toàn hơn né.
- Không nói số nào không có trong file kết quả. Thầy hỏi số khác thì nói "nhóm chưa đo".
- Nếu quá giờ, rút slide 9 và 10, mỗi slide còn khoảng 20 giây.
- Mỗi người đọc thêm phần mình trong thuyết minh: Khang mục 8 và 11, Nhân mục 10 đến 12, Trúc mục 9, 13 đến 16.
