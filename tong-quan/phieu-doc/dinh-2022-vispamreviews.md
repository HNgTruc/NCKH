# dinh-2022-vispamreviews: Detecting Spam Reviews on Vietnamese E-commerce Websites

Claude điền từ toàn văn bản arXiv (2207.14636v2, ngày 9/12/2022, 13 trang) ngày 04/11/2026. Số trang trong phiếu là số trang của bản arXiv. Bản đăng ở ACIIDS 2022 (LNCS, Springer) nằm ở tr. 595-607, Claude chưa mở được bản này. Trúc cần đọc lại bài gốc trước khi trích.

## Thông tin

| Trường | Giá trị |
| --- | --- |
| Tác giả | Co Van Dinh, Son T. Luu, Anh Gia-Tuan Nguyen. Trường ĐH Công nghệ Thông tin, ĐHQG TP.HCM (tr. 1) |
| Năm | 2022 |
| Tên tạp chí hoặc hội nghị | 14th Asian Conference on Intelligent Information and Database Systems (ACIIDS 2022), Intelligent Information and Database Systems, LNCS, Springer, tr. 595-607. Tên hội nghị lấy từ mục Comments trên trang arXiv, bản PDF arXiv không ghi |
| DOI hoặc link chính thức | [10.1007/978-3-031-21743-2_48](https://doi.org/10.1007/978-3-031-21743-2_48). Bản mở: [arXiv 2207.14636](https://arxiv.org/abs/2207.14636). Dữ liệu: [github.com/sonlam1102/vispamdetection](https://github.com/sonlam1102/vispamdetection) |
| Chỉ mục (Scopus/WoS), bằng chứng | Chưa tra. [TODO: Trúc tra hạng ACIIDS trên CORE portal và kiểm tra LNCS có trong Scopus, ghi link] |
| Hạng Q hoặc CiteScore, IF | Chưa tra |
| Lĩnh vực theo SCImago | Chưa tra |
| Người đọc, ngày đọc | Claude đọc toàn văn bản arXiv ngày 04/11/2026. Trúc: [TODO: đọc lại, ghi ngày] |

## Nội dung (theo khung bài giữa kỳ)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Bối cảnh và vấn đề | Thương mại điện tử Việt Nam tăng nhanh. Người mua dựa vào đánh giá của người mua trước, nên có người viết đánh giá sai sự thật để lừa người mua (spam reviews) (tr. 1) |
| Khoảng trống tác giả muốn giải quyết | Đã có bộ dữ liệu đánh giá sản phẩm tiếng Việt (điện thoại, nhà hàng, phàn nàn) nhưng chưa có bộ nào cho phát hiện đánh giá rác trên sàn thương mại điện tử Việt Nam (tr. 2) |
| Mục tiêu | Xây bộ ViSpamReviews với quy trình gán nhãn chặt chẽ, rồi đánh giá các mô hình phân loại trên bộ này (tr. 1-2) |
| Câu hỏi hoặc giả thuyết | Bài không nêu |
| Đối tượng | Đánh giá sản phẩm tiếng Việt trên sàn thương mại điện tử. Không phải SMS |
| Dữ liệu (nguồn, số mẫu, số lớp, ngôn ngữ) | Thu từ "leading online shopping platforms in Vietnam", không nêu tên sàn. Mỗi loại hàng chọn vài sản phẩm bán gần đây, lấy tối đa 15 đánh giá mỗi sản phẩm, được 19.868 đánh giá kèm số sao và link sản phẩm (tr. 2-3). Bài không nêu thời gian thu thập. Chia 7-1-2: huấn luyện 14.306, kiểm định 1.590, kiểm tra 3.974 (Bảng 6, tr. 7). Hình 1 (tr. 6): tập huấn luyện có NO-SPAM 10.585, SPAM-1 195, SPAM-2 1.087, SPAM-3 2.439; tập kiểm định 1.157 / 26 / 127 / 280; tập kiểm tra 2.867 / 61 / 319 / 727. Cộng ba tập ra 19.870, lệch 2 so với 19.868 ở tr. 2. Bảng 7 (tr. 7) chỉ cộng ra 10.779 đánh giá (10.584 NO-SPAM, 195 SPAM), không khớp tổng, bài không giải thích |
| Đặc trưng, đầu vào | Dùng vector fastText có sẵn cho các mạng sâu (tr. 7). Bài không nêu bước tiền xử lý, có tách từ cho PhoBERT hay không, độ dài tối đa, số epoch, learning rate |
| Phương pháp, mô hình | Text-CNN, LSTM, GRU, PhoBERT, BERT4News (tr. 8) |
| Chỉ số đánh giá | Accuracy và F1 trung bình macro (macro-averaged F1) (tr. 8-9) |
| Kết quả chính (số liệu kèm trang, bảng) | Task 1 (2 lớp): PhoBERT Acc 90,01, F1-macro 86,89; BERT4News 86,39 / 86,16; Text-CNN 84,18 / 77,89 (Bảng 8, tr. 9). Task 2 (4 lớp): PhoBERT Acc 88,93, F1-macro 72,17; LSTM 83,35 / 66,58; BERT4News 86,20 / 62,62 (Bảng 8). Task 2 thấp hơn do lệch lớp và khó hơn (tr. 9). Phân tích lỗi PhoBERT: SPAM-2 bị đoán là NO-SPAM 177 lần, đúng 135 lần (tr. 9, Hình 2 tr. 10). Lỗi chính do mô hình lẫn lời khen thương hiệu với nhận xét chất lượng, và đánh giá quá ngắn (Bảng 9, tr. 10-11) |

## Quy trình gán nhãn (mẫu tham khảo cho mục 12)

| Câu hỏi | Trả lời, có số trang |
| --- | --- |
| Khung quy trình | Dựa theo khung MATTER của Pustejovsky và Stubbs (tr. 3) |
| Số người gán | 3 người, gán độc lập (tr. 3) |
| Giai đoạn 1: huấn luyện người gán | Người gán đọc hướng dẫn (nghĩa từng nhãn, đánh giá mẫu, ví dụ ca đặc biệt), gán 300 mẫu ngẫu nhiên. Tính độ đồng thuận trung bình. Đạt thì sang giai đoạn 2, không đạt thì sửa hướng dẫn và huấn luyện lại (tr. 3) |
| Ngưỡng chấp nhận | Cohen's kappa trên 0,5, dẫn theo Di Eugenio (2000) (tr. 3, tài liệu [4] tr. 12) |
| Giai đoạn 2: gán toàn bộ | Cả 3 người gán toàn bộ dữ liệu, nhãn cuối lấy theo đa số (majority voting) (tr. 3, 6) |
| Bộ nhãn | Task 1: SPAM và NO-SPAM. Task 2: mỗi tin SPAM được gán thêm một trong 3 loại theo Jindal và Liu (2008): SPAM-1 đánh giá giả (khen hoặc chê sai để kéo khách hay hại cửa hàng), SPAM-2 chỉ nói về thương hiệu, nhà sản xuất, người bán, SPAM-3 không phải đánh giá (không liên quan sản phẩm, quảng cáo sản phẩm khác, kiếm hoa hồng) (tr. 3) |
| Hướng dẫn gán nhãn | Có định nghĩa từng nhãn (tr. 3) và bảng ví dụ kèm lý giải cho từng nhãn (Bảng 1, tr. 4). Bài không đăng toàn văn hướng dẫn |
| Độ đồng thuận lần đầu | Cohen's kappa theo từng cặp. Task 1: A1-A2 0,36, A1-A3 0,34, A2-A3 0,61, trung bình 0,43. Task 2: 0,41, 0,37, 0,57, trung bình 0,44. Dưới ngưỡng 0,5 (Bảng 2, tr. 5) |
| Xử lý khi chưa đạt | Bổ sung giải thích và ví dụ vào hướng dẫn, huấn luyện lại người gán (tr. 5). Gắn link sản phẩm cho người gán xem ngữ cảnh (tr. 5) |
| Độ đồng thuận sau huấn luyện lại | Task 1: 0,93, 0,59, 0,65, trung bình 0,72. Task 2: 0,87, 0,57, 0,60, trung bình 0,68. Tác giả xếp vào mức "substantial" theo Landis và Koch (1977) (Bảng 3, tr. 5) |
| Chỗ người gán hay bất đồng | Giữa NO-SPAM và các loại SPAM, nhất là SPAM-2 (khen thương hiệu, người bán) và SPAM-3 (nhận xét quá chung). Ma trận nhầm lẫn trung bình giữa các cặp ở Bảng 4 (tr. 5), ví dụ bất đồng ở Bảng 5 (tr. 6) |
| Giấy phép, cách lấy dữ liệu | Bài không nêu. Trang arXiv ghi dữ liệu ở github.com/sonlam1102/vispamdetection. README (Claude xem ngày 04/11/2026) ghi dữ liệu dùng cho "research purposes", có hai phiên bản trên Hugging Face ở chế độ phải xin quyền (gated), không thấy file giấy phép. Bản PDF arXiv mang giấy phép CC BY-NC-SA 4.0, đó là giấy phép của bài, không phải của dữ liệu. [TODO: Trúc kiểm tra trang Hugging Face của bộ dữ liệu] |

## Nhận xét của nhóm

Phần này là đề xuất của Claude. Trúc sửa lại theo ý mình.

Ưu điểm: Là bộ dữ liệu "rác" tiếng Việt hiếm hoi có mô tả quy trình gán nhãn đầy đủ: ngưỡng kappa đặt trước, đo theo từng cặp người gán, có vòng huấn luyện lại khi chưa đạt, báo cả kappa trước và sau. Có bộ nhãn nhiều lớp tách các loại rác, gần với ý tưởng 3 nhãn của đề tài. Báo F1-macro, phù hợp khi lệch lớp. Ví dụ dễ hiểu về kappa: hai người cùng gán 300 tin, nếu đoán bừa cũng trùng nhau một phần, kappa 0,72 nghĩa là mức đồng ý vượt khá xa mức trùng do ngẫu nhiên.

Hạn chế: Không phải SMS, không có nhãn lừa đảo. Kappa từng cặp chênh lệch nhiều (0,93 so với 0,59), cho thấy một người gán lệch với hai người còn lại, bài không bàn điểm này. Lớp hiếm (SPAM-1 chỉ 61 mẫu trong tập kiểm tra) làm F1-macro Task 2 thấp (72,17). Thiếu thông tin tiền xử lý và siêu tham số nên khó lặp lại. Số liệu tổng không khớp giữa các bảng (19.868, 19.870, Bảng 7 chỉ 10.779).

Dùng cho mục nào của thuyết minh: Mục 12, làm mẫu thiết kế gán nhãn: 2 giai đoạn, ngưỡng Cohen's kappa đặt trước có dẫn nguồn, huấn luyện lại khi chưa đạt, báo kappa từng cặp, nhãn cuối theo đa số. Mục 8.3, nghiên cứu "rác" tiếng Việt nhiều lớp gần nhất với đề tài. Mục 9, cho thấy với tiếng Việt, tách rác thành nhiều loại đã có ở đánh giá sản phẩm nhưng chưa thấy ở SMS. Bài học cho đề tài: lớp LUA_DAO có thể ít mẫu như SPAM-1, nên dự kiến cách xử lý lệch lớp ngay từ mục 12.

## Trích dẫn IEEE

```
[n] C. V. Dinh, S. T. Luu, and A. G.-T. Nguyen, "Detecting spam reviews on Vietnamese e-commerce websites," in Intelligent Information and Database Systems (ACIIDS 2022), Lecture Notes in Computer Science, vol. [TODO: số tập LNCS, nơi xuất bản]. Springer, 2022, pp. 595–607, doi: 10.1007/978-3-031-21743-2_48.
```
