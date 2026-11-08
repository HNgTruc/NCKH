<!-- HƯỚNG DẪN
Mẫu: Trình bày cụ thể cách tiếp cận, các nguồn dữ liệu và cách thu thập dữ liệu; mô tả chi tiết phương pháp, quy trình chọn mẫu và cách thức thu thập và phân tích số liệu; lý giải việc lựa chọn của tác giả.
Barem BT2: cách tiếp cận chung (định lượng/định tính/kết hợp); nguồn dữ liệu; cách thu thập; phương pháp phân tích.
Slide Chương 3: sáu thành phần: thiết kế, thu thập, chọn mẫu, công cụ, phân tích, đạo đức.
Slide 2.6: quy trình 5 giai đoạn: thu thập, làm sạch, đặc trưng, mô hình, trực quan.
Slide 2.1: bias khi thu thập (bảng trong docs/yeu-cau/kien-thuc-slide.md).
Nên gọi agent thiet-ke-phuong-phap trước khi viết. Hướng dẫn gán nhãn: nghien-cuu/huong-dan-gan-nhan.md.

Checklist:
- Nói rõ đây là nghiên cứu định lượng, ứng dụng, thực nghiệm có đối chứng (so sánh mô hình)
- Mỗi nguồn dữ liệu có tên, cách lấy, giấy phép hoặc điều khoản sử dụng
- Có cỡ mẫu dự kiến và cách chia train/validation/test, lý do chọn
- Có quy trình gán nhãn và cách đo độ đồng thuận
- Có ít nhất một mô hình cơ sở và một mô hình chính, có lý do chọn
- Chỉ số đánh giá phù hợp dữ liệu lệch lớp (không chỉ dùng accuracy)
- Có mục đạo đức: ẩn danh, lưu trữ, không công bố dữ liệu cá nhân
- Có mục bias và cách giảm
- Mỗi lựa chọn có câu "vì sao"
-->

## 12. Phương pháp nghiên cứu

### 12.1. Cách tiếp cận

Đề tài là nghiên cứu định lượng, ứng dụng, theo thiết kế thực nghiệm có đối chứng. Biến độc lập là mô hình phân loại (TF-IDF kết hợp Logistic Regression, PhoBERT, ViSoBERT) và dạng văn bản của tập kiểm tra (nguyên gốc, bỏ dấu thanh, chèn ký tự, xóa thẻ quảng cáo). Biến phụ thuộc là precision, recall, F1 của từng lớp, F1 trung bình macro và tỉ lệ nhầm giữa tin lừa đảo và tin quảng cáo. Mô hình TF-IDF kết hợp Logistic Regression là nhóm đối chứng. Dữ liệu, cách chia tập và random seed được giữ như nhau cho mọi mô hình, hai mô hình transformer dùng cùng cấu hình huấn luyện, để chênh lệch kết quả chỉ đến từ mô hình. CH1 và CH2 được trả lời bằng thống kê mô tả.

Quy trình đi theo năm giai đoạn xử lý thông tin: thu thập (tải bộ dữ liệu công khai), làm sạch (bỏ tin trùng, kiểm tra ẩn danh), gán nhãn, biểu diễn đặc trưng (TF-IDF hoặc tách từ cho PhoBERT), mô hình hóa, rồi đánh giá và trình bày kết quả bằng bảng và ma trận nhầm lẫn.

### 12.2. Nguồn dữ liệu và cách thu thập

| Nguồn | Loại tin | Cách lấy | Điều khoản sử dụng | Số mẫu dự kiến |
| --- | --- | --- | --- | --- |
| Bộ "Vietnamese SMS Dataset with Quality Assurance" trên Hugging Face [15], phiên bản commit `a90e2bd` | SMS tiếng Việt thật do cộng đồng đóng góp, 2 nhãn gốc: hợp lệ, rác hoặc lừa đảo. Đã được tác giả ẩn danh bằng thẻ `[PHONE]`, `[MONEY]`, `[NUMBER]` | Script `nghien-cuu/src/gan_nhan_so_bo.py` tải đúng phiên bản, bỏ tin trùng nguyên văn | CC BY 4.0: được dùng, sửa, chia sẻ nếu ghi nguồn | 2.991 dòng, còn 2.629 tin sau khi bỏ trùng; dùng 600 tin |

Nhóm chọn bộ dữ liệu này vì đây là bộ SMS tiếng Việt công khai duy nhất tìm được có giấy phép rõ và dữ liệu năm 2026. Các bộ trong nước khác hoặc không công khai, hoặc chỉ công khai vài tin mẫu [9], [7]. Trong thời gian học kỳ, nhóm không tự thu thập thêm tin nhắn, vì việc này cần phiếu đồng ý của người đóng góp và quy trình ẩn danh riêng.

### 12.3. Gán nhãn và chọn mẫu

Bộ nhãn gồm `LUA_DAO` (tin cố ý lừa người nhận đưa tiền, mật khẩu, mã OTP, thông tin cá nhân hoặc bấm link giả), `QUANG_CAO` (tin quảng cáo, khuyến mãi không giả danh và không đòi thông tin nhạy cảm) và `BINH_THUONG` (tin cá nhân, thông báo dịch vụ thật). Tin không đủ căn cứ được gán `KHONG_RO` và loại khỏi huấn luyện. Hướng dẫn gán nhãn có sáu quy tắc cho các trường hợp khó: tin cờ bạc trực tuyến và tin hẹn hò hứa trả "trợ cấp" là `LUA_DAO`, vì các tin này dụ người nhận nạp tiền hoặc chuyển sang kênh chat riêng (dự thảo nghị định có một loại riêng cho tin vi phạm nội dung bị cấm [19]; nhóm không tách loại này, đây là quyết định của nhóm và là một hạn chế khi đối chiếu với dự thảo); tin của nhà mạng gán theo nội dung, không theo thẻ (QC) hay (TB) ở đầu tin. Nhãn chỉ dựa vào nội dung, không xét người nhận đã đồng ý nhận quảng cáo hay chưa.

Chọn mẫu theo ba bước:

1. Script gợi ý một nhãn cho mỗi tin bằng quy tắc từ khóa (thẻ QC, từ "khuyến mãi", "soạn ... gửi", mã OTP) và ghi lý do.
2. Script chọn ngẫu nhiên 200 tin cho mỗi nhãn gợi ý, random seed 42, được 600 tin. Chọn đều ba nhóm để lớp nào cũng đủ mẫu đánh giá. Vì cách chọn này làm tỉ lệ lớp trong mẫu khác tỉ lệ trong cả bộ, CH2 được ước lượng có trọng số: mỗi tin nhân với số tin của nhóm gợi ý trong cả bộ chia cho số tin của nhóm đó trong mẫu.
3. Nhãn của cả 600 tin được gán sơ bộ bằng mô hình ngôn ngữ Claude (Anthropic) theo hướng dẫn gán nhãn, có xem nhãn gợi ý của script và ghi lý do cho tin lừa đảo. Người gán thứ nhất (Huỳnh Ngọc Trúc) xem lại [TODO: Trúc ghi đã xem lại bao nhiêu tin và sửa bao nhiêu tin] rồi chốt. Người gán thứ hai (Khang) gán độc lập 100 tin trong số đó (34, 34 và 32 tin theo ba nhãn gợi ý), không được xem nhãn gợi ý lẫn nhãn của người thứ nhất.

Độ đồng thuận đo bằng Cohen's kappa trên 100 tin, tính cả nhãn `KHONG_RO`. Kappa đo mức hai người đồng ý sau khi trừ phần trùng do may mắn. Ngưỡng chấp nhận là κ ≥ 0,60. Nghiên cứu ViSpamReviews đặt ngưỡng trên 0,5 và đạt 0,72 sau một vòng huấn luyện lại người gán [6]. Đề tài đặt ngưỡng chặt hơn, vì ranh giới giữa tin lừa đảo và tin quảng cáo chính là điểm mới cần chứng minh. Hai người xem lại các tin bất đồng, ghi lý do và bổ sung quy tắc vào hướng dẫn. Nếu kappa dưới 0,60, nhóm sửa hướng dẫn và báo đúng con số đạt được.

Kết quả vòng gán đầu: hai bên giống nhau ở 71 trong 100 tin, κ = 0,569, thấp hơn ngưỡng 0,60. Trong 29 tin bất đồng, 17 tin ở ranh giới giữa quảng cáo và lừa đảo hoặc bình thường (tin mời gói, cho vay, trúng thưởng của nhà mạng), 7 tin là mã OTP mà người gán thứ hai xếp vào lừa đảo, 3 tin giả danh ngân hàng hoặc nhà mạng mà người gán thứ hai xếp vào bình thường, 2 tin còn lại lệch giữa bình thường và quảng cáo. Hướng dẫn gán nhãn lúc đó chưa có quy tắc cho tin OTP thật. Trúc và Khang đã xem lại 29 tin này ngày 08/11/2026. Hai người giữ nhãn sơ bộ ở 28 tin và đổi 1 tin sang lừa đảo theo người gán thứ hai, rồi bổ sung hai quy tắc (tin OTP thật, tin mời của nhà mạng) vào hướng dẫn. Kappa không được tính lại sau cuộc họp, vì sau khi thống nhất hai bên đã trùng nhau trên cả 29 tin. Con số báo cáo vẫn là κ = 0,569 của vòng đầu. Vì nhãn của người gán thứ nhất là nhãn sơ bộ do mô hình ngôn ngữ gán, con số này đo mức người gán thứ hai đồng ý với nhãn sơ bộ đó.

Chia tập: 600 tin được chia làm 5 phần, phân tầng theo nhãn, random seed 42. Mỗi lần lấy một phần làm tập kiểm tra, bốn phần còn lại để huấn luyện, lặp 5 lần rồi lấy trung bình và độ lệch chuẩn. Nhóm chọn kiểm định chéo 5 phần thay cho một tập kiểm tra cố định, vì một tập kiểm tra 120 tin cho kết quả dao động mạnh. Tin trùng nguyên văn đã được bỏ trước khi chia, nên không có tin nào vừa ở tập huấn luyện vừa ở tập kiểm tra. Tin gần trùng (cùng một mẫu tin, khác vài chữ) chưa được gom nhóm, nên kết quả có thể cao hơn thực tế; đây là hạn chế của đề tài.

### 12.4. Phương pháp phân tích

| Thành phần | TF-IDF + Logistic Regression | PhoBERT-base | ViSoBERT |
| --- | --- | --- | --- |
| Tiền xử lý | Chuyển chữ thường, cụm 1 và 2 từ, giữ thẻ ẩn danh và đường link | Tách từ bằng RDRSegmenter của VnCoreNLP như bài gốc [4]; dùng underthesea nếu VnCoreNLP lỗi và ghi lại | Đưa văn bản thô, không tách từ [5] |
| Cấu hình | `class_weight="balanced"`, tối đa 2.000 vòng lặp | Tinh chỉnh (fine-tune) 4 epoch, learning rate 2e-5, batch 16, độ dài tối đa 128 token, AdamW, warmup 10% | Giống PhoBERT |
| Vai trò | Mô hình cơ sở | Mô hình chính | Mô hình so sánh |

Hai mô hình transformer dùng cùng cấu hình và không dò siêu tham số, vì với 600 tin không còn đủ dữ liệu cho một tập kiểm định riêng, và dò cho một mô hình kỹ hơn mô hình kia sẽ làm phép so sánh H2 không công bằng.

Công cụ: Python trên Google Colab với GPU T4 miễn phí; thư viện pandas, scikit-learn, PyTorch, Hugging Face Transformers, py_vncorenlp, underthesea. Toàn bộ các bước nằm trong một notebook (`nghien-cuu/notebooks/thu-nghiem-so-bo.ipynb`). Notebook ghi lại cấu hình, phiên bản thư viện và kết quả từng phần vào một file JSON, để người khác chạy lại ra cùng kết quả.

Chỉ số đánh giá là precision, recall và F1 của từng lớp, F1 trung bình macro và ma trận nhầm lẫn, báo dạng trung bình ± độ lệch chuẩn qua 5 phần. Accuracy chỉ là chỉ số phụ: một mô hình đoán mọi tin là "bình thường" vẫn có accuracy cao khi tin bình thường chiếm đa số, trong khi không bắt được tin lừa đảo nào. Precision lớp lừa đảo cho biết trong các tin mô hình báo là lừa đảo, bao nhiêu tin đúng là lừa đảo. Recall lớp lừa đảo cho biết trong các tin lừa đảo thật, mô hình bắt được bao nhiêu. CH4 lấy từ ma trận nhầm lẫn: số tin lừa đảo bị đoán thành quảng cáo chia cho tổng số tin lừa đảo, và ngược lại.

Với MT3, tập kiểm tra của mỗi phần được biến đổi theo ba cách, còn mô hình vẫn huấn luyện trên tin gốc:

- Bỏ dấu thanh: chuyển toàn bộ chữ có dấu thành không dấu, ví dụ "Ngân hàng" thành "Ngan hang".
- Chèn ký tự: biến dạng ngẫu nhiên khoảng 20% số từ theo một trong ba cách kẻ gửi rác hay dùng, gồm xen dấu chấm ("n.g.â.n"), lặp ký tự xen chữ hoa ("nHhậận"), thay chữ bằng số giống hình ("ng4n h4ng"). Thẻ ẩn danh và đường link không bị biến đổi. Random seed cố định, nên mọi mô hình nhận đúng một bản biến đổi.
- Xóa thẻ: xóa các thẻ (QC), [QC], (TB), [TB] ở đầu tin. Bước này kiểm tra mô hình có chỉ học thẻ thay vì nội dung hay không, vì tin quảng cáo của nhà mạng thường mang thẻ (QC) và script gợi ý nhãn cũng dựa vào thẻ này.

Mức giảm F1 lớp lừa đảo bằng F1 trên tập gốc trừ F1 trên tập đã biến đổi. Để đánh giá H1 và H2, nhóm so ghép cặp theo từng phần: H1 được ủng hộ khi F1 lớp lừa đảo của PhoBERT cao hơn của mô hình cơ sở ở đa số trong 5 phần và chênh lệch trung bình lớn hơn 0. H2 đánh giá tương tự với mức giảm khi bỏ dấu của PhoBERT so với ViSoBERT. Chỉ có 5 phần nên đây là bằng chứng sơ bộ, chưa phải kiểm định thống kê. Kiểm định bootstrap trên tập kiểm tra lớn hơn để ở hướng phát triển.

### 12.5. Đạo đức nghiên cứu và kiểm soát sai lệch

Dữ liệu là bộ công khai theo giấy phép CC BY 4.0, đã được tác giả ẩn danh. Nhóm ghi nguồn đầy đủ và kiểm tra ẩn danh thêm hai lượt: script quét lại số điện thoại và dãy số dài còn sót (thay thêm 110 chỗ), và người gán đánh dấu tin còn sót họ tên để xóa. Khi kiểm tra ngẫu nhiên 12 tin, nhóm thấy 1 tin còn họ tên đầy đủ, nên các file dữ liệu chưa được đưa lên kho mã nguồn công khai. Đề tài không công bố nguyên văn tin nhắn, chỉ công bố mã tin kèm nhãn ba lớp. Người gán không bấm link và không gọi lại số điện thoại trong tin. Tác giả PhoBERT phát hành bản base theo giấy phép MIT [20]. Bài gốc của ViSoBERT ghi mô hình chỉ dùng cho mục đích nghiên cứu [5], nên đề tài chỉ dùng ViSoBERT để nghiên cứu. Kết quả đánh giá trên tin chèn ký tự có thể bị dùng ngược để soạn tin né bộ lọc (tính lưỡng dụng), nên nhóm chỉ báo số liệu tổng hợp và không phát hành công cụ chèn ký tự riêng.

| Sai lệch (bias) | Biểu hiện trong đề tài | Cách giảm hoặc cách báo |
| --- | --- | --- |
| Chọn nguồn (sampling) | Một bộ dữ liệu duy nhất, không rõ người đóng góp là ai, ở đâu | Báo là hạn chế. Thu thêm tin từ nhiều nguồn ở hướng phát triển |
| Chọn mẫu (selection) | Mẫu 600 tin chọn đều 200 tin mỗi nhãn gợi ý, khác tỉ lệ thật | Dùng F1 trung bình macro; ước lượng CH2 có trọng số |
| Gán nhãn (labeling) | Ranh giới lừa đảo và quảng cáo không rõ | Hướng dẫn có quy tắc và ví dụ, hai người gán, đo kappa |
| Neo (anchoring) | Nhãn sơ bộ do mô hình ngôn ngữ gán có xem nhãn gợi ý của script, rồi người gán thứ nhất xem lại | Người thứ hai gán mù; báo chênh lệch tỉ lệ trùng nhãn gợi ý giữa hai người; ghi rõ nhãn sơ bộ không phải do người gán từ đầu |
| Nhãn gốc hai lớp | Nhãn "rác" của bộ gốc gộp tin lừa đảo với tin rác khác | Gán lại từng tin, báo bảng chuyển nhãn (CH2) |
| Đo lường (measurement) | Mỗi lần chạy tiền xử lý một kiểu | Một notebook chung, cố định random seed, ghi phiên bản thư viện |
| Lịch sử (historical) | Tin chỉ trong khoảng 2 tháng năm 2026, ngày ghi trong bộ có thể là ngày đóng góp | Chỉ kết luận cho khoảng thời gian này |
| Thẻ trùng nhãn | Tin quảng cáo nhà mạng thường có thẻ (QC); script cũng dùng thẻ này để gợi ý nhãn, nên mô hình có thể chỉ học thẻ | Báo tỉ lệ tin quảng cáo có thẻ; đo lại F1 trên tập kiểm tra đã xóa thẻ |
| Văn hóa, cách viết (cultural) | Tin không dấu, teencode, chèn ký tự | Giữ nguyên trong dữ liệu; đo riêng ở MT3 |
| Dấu thanh trùng nhãn | Ở nghiên cứu trước, tin rác phần lớn không dấu còn tin hợp lệ có dấu, nên mô hình có thể học dấu thay vì nội dung [10] | Báo tỉ lệ tin không dấu theo từng nhãn; đo F1 trên bản bỏ dấu |
