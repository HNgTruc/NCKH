# Tổng quan tài liệu

Thư mục này là đầu vào của mục 8 và mục 9. Quy trình cho mỗi bài: tìm, kiểm tra nguồn, đọc, điền phiếu, thêm dòng vào ma trận, xuất Zotero sang `references.bib`. Skill `/doc-bai-bao` làm các bước này cho một bài. Agent `tong-quan-tai-lieu` làm cho nhiều bài.

## Cơ sở dữ liệu

| Nơi tìm | Dùng để | Ghi chú |
| --- | --- | --- |
| [Google Scholar](https://scholar.google.com) | Tìm rộng, xem số trích dẫn | Không dùng làm bằng chứng uy tín |
| [IEEE Xplore](https://ieeexplore.ieee.org) | Bài hội nghị, tạp chí IEEE | Nhiều bài về phishing, spam |
| [ACL Anthology](https://aclanthology.org) | Bài NLP, mô hình tiếng Việt | Miễn phí toàn văn |
| [arXiv](https://arxiv.org) | Bản preprint | Ưu tiên bản đã đăng chính thức nếu có |
| [SCImago](https://www.scimagojr.com) | Tra hạng Q, kiểm tra Scopus | Bắt buộc với mỗi tạp chí trích dẫn |
| [CORE portal](https://portal.core.edu.au/conf-ranks) | Hạng hội nghị | |
| Tạp chí trong nước | Nghiên cứu Việt Nam | Danh sách trong `docs/yeu-cau/kien-thuc-slide.md` |

## Từ khóa

Tiếng Anh: SMS phishing detection, smishing, scam message classification, phishing email detection, spam SMS dataset, Vietnamese text classification, PhoBERT fine-tuning, low-resource language phishing.

Tiếng Việt: phát hiện tin nhắn lừa đảo, phân loại tin nhắn rác, lừa đảo trực tuyến, phát hiện email lừa đảo, phân loại văn bản tiếng Việt.

## Tiêu chí chọn bài

| Nhận | Loại |
| --- | --- |
| Bài từ 2016 trở lại đây, trừ bài kinh điển như bộ dữ liệu gốc | Bài không rõ nơi đăng, không có tác giả |
| Đăng ở tạp chí Scopus/WoS, hội nghị có phản biện, hoặc tạp chí trong danh mục HĐGSNN | Tạp chí nằm trong danh sách săn mồi (predatory) |
| Có mô tả dữ liệu và chỉ số đánh giá | Bài chỉ mô tả sản phẩm, không có thực nghiệm |

## Nhật ký tìm kiếm

Ghi mỗi lần tìm để mục 12 và buổi trình bày có thể nói rõ cách nhóm tìm tài liệu.

| Ngày | Người | Nơi tìm | Từ khóa | Số kết quả | Số bài giữ lại |
| --- | --- | --- | --- | --- | --- |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | SMS spam detection BERT comparison Naive Bayes SVM TF-IDF journal | 10 | 0 (toàn preprint hoặc tạp chí không rõ chỉ mục) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | smishing detection dataset machine learning journal 2023 | 10 | 0 trực tiếp, dẫn tới Mishra và Soni |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | SMS spam detection low-resource language BERT fine-tuning dataset Indonesian OR Bangla OR Arabic OR Urdu journal | 10 | 0 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | phishing email detection transformer BERT survey OR systematic review | 10 | 1 (Kyaw 2024) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | SMS spam detection survey review 2023 2024 journal datasets challenges deep learning transformers | 10 | 1 (Al Saidat 2024) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Tra theo tên bài để lấy trang gốc: Almeida 2011, Roy 2020, Salman 2024, DSmishSMS, Spam Transformer, ViSoBERT, SMTCE, ViSpamReviews, ViLexNorm, ViHSD | 10 mỗi lần | 9 (ViHSD bị loại) |
| 04/11/2026 | Huỳnh Ngọc Trúc | ACL Anthology (mở trực tiếp) | PhoBERT, ViSoBERT, SMTCE, ViLexNorm | 4 trang bài | 4 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese SMS spam detection dataset | 9 | 1 (Pham và Le-Hong 2016) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | phân loại tin nhắn rác tiếng Việt học máy tạp chí | 10 | 1 (Vũ Duy Hiến 2024) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | phát hiện tin nhắn lừa đảo tiếng Việt PhoBERT | 10 | 0 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | VNSED Vietnamese spam email detection Journal of Computer Science and Cybernetics | 10 | 1 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | "Vietnamese" SMS scam OR smishing OR "fraudulent message" detection transformer 2024 OR 2025 | 9 | 2 (RIVF 2023, IDEAL 2024) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | "tin nhắn rác" OR "tin nhắn lừa đảo" phát hiện học sâu bài báo tạp chí khoa học 2023 2024 2025 | 10 | 0 mới, dẫn tới bài trên Tạp chí An toàn thông tin |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese spam SMS classification deep learning conference KSE OR RIVF OR SoICT OR NICS OR MAPR | 10 | 0 mới |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | huggingface dataset Vietnamese SMS scam spam labeled | 10 | 0 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | "Vietnamese SMS Scam Dataset" quality-assured | 10 | 0 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese phishing OR scam text detection dataset benchmark ACL OR Springer OR IEEE 2025 | 9 | 0 (PhishVN là dữ liệu URL, loại) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | site:aclanthology.org Vietnamese spam OR scam OR phishing detection | 10 | 0 |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese spam SMS detection "PhoBERT" "99.53"; Vu Minh Tuan Tran Quang Anh Vietnamese spam SMS PhoBERT DNN | 10 mỗi lần | 0 mới |
| 04/11/2026 | Huỳnh Ngọc Trúc | Trang Tạp chí KH-CN trong lĩnh vực An toàn thông tin (isj.vn) | tin nhắn rác | 1 | 1 |
| 04/11/2026 | Huỳnh Ngọc Trúc | VJOL (vjol.info.vn) | tin nhắn rác | 2 | 0 mới (1 bài đã có, 1 bài luật học) |
| 04/11/2026 | Huỳnh Ngọc Trúc | VJOL (vjol.info.vn) | SMS spam | 4 | 2 mới (2 bài trên Tạp chí KH-CN TT&TT) |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese teencode OR "without diacritics" text classification PhoBERT robustness social media | 10 | 0 mới |
| 04/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese diacritic restoration deep learning transformer paper | 10 | 0 (không sát đề tài) |
| 04/11/2026 | Huỳnh Ngọc Trúc | dblp, SCImago, CORE portal | Vietnamese spam; tra hạng nơi đăng | Bị chặn truy cập tự động (lỗi 403) | Cần tra tay |
| 06/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | Vietnamese smishing detection SMS dataset; Vietnamese SMS scam detection multi-class spam advertising fraud; phân loại tin nhắn lừa đảo tiếng Việt học máy | 10 mỗi lần | 0 |
| 06/11/2026 | Huỳnh Ngọc Trúc | Google Scholar (Claude) | Vietnamese smishing; Vietnamese SMS scam detection | 10 mỗi lần (khoảng 61 và 202) | 1 (VIESpam 2025), thêm ứng viên MLTEA 2026 |
| 06/11/2026 | Huỳnh Ngọc Trúc | Google Scholar (Claude) | "tin nhắn lừa đảo" phân loại; "phân lớp đa nhãn" "tin nhắn SMS" | 8; 1 | 1 (Hoàng Thị Hà 2022) |
| 06/11/2026 | Huỳnh Ngọc Trúc | Google Scholar (Claude) | Vietnamese SMS phishing OR smishing dataset PhoBERT (từ 2023); "multi-class" OR "three classes" Vietnamese SMS spam advertising fraud | 20; 10 | 0 bài báo, 1 tổng quan preprint (Pritom 2026) vào ứng viên |
| 06/11/2026 | Huỳnh Ngọc Trúc | Semantic Scholar, OpenAlex, Crossref, SpringerLink (Claude) | Tra DOI RIVF 2023, IDEAL 2024, VIESpam; OpenAlex "Vietnamese SMS spam", "Vietnamese smishing OR SMS phishing OR scam OR fraud" | 25 mỗi lần OpenAlex | 3 phiếu chỉ đọc tóm tắt (RIVF 2023, IDEAL 2024, VIESpam) |
| 06/11/2026 | Huỳnh Ngọc Trúc | Tạp chí Phát triển KHCN ĐHQG TP.HCM, VJOL (Claude) | SMS spam; tin nhắn; lừa đảo tin nhắn; SMS | 0; 0; 0; 25 (45) | 0 bài phân loại. 1 bài ngành luật vào ứng viên mục 9 |
| 06/11/2026 | Huỳnh Ngọc Trúc | Công cụ tìm web (Claude) | FAIR, SoICT, KSE, NICS kèm SMS spam/scam tiếng Việt | 10-15 mỗi lần | 0. dblp, IEEE Xplore, CORE chặn truy cập tự động nên chưa duyệt từng kỷ yếu. Chi tiết ở cuối `ma-tran-tong-quan.md` |
