---
title: Hướng Dẫn Chuẩn Bị và Nhập Liệu Nội Dung Cho Media Team
version: 1.0.0
status: Stable
---

# HƯỚNG DẪN CHUẨN BỊ & NHẬP LIỆU NỘI DUNG (MEDIA & CONTENT TEAM)

Tài liệu này được biên soạn bởi đội ngũ Phát triển phần mềm (Dev) nhằm giúp đội ngũ Truyền thông và Nội dung (Media/Content Team) nắm rõ cấu trúc thông tin, định dạng dữ liệu, và các trường bắt buộc cần chuẩn bị khi cập nhật nội dung cho hệ thống website qua trang Quản trị (Django Admin).

> [!IMPORTANT]
> - Tài liệu này được đối chiếu trực tiếp từ các file định nghĩa cơ sở dữ liệu (`models.py`) của hệ thống.
> - Vui lòng tuân thủ nghiêm ngặt các quy định về độ dài ký tự tối đa, định dạng ảnh, đường dẫn (URL) và biểu tượng (Icons) để tránh gây lỗi giao diện hoặc lỗi hệ thống.
> - **Lưu ý quan trọng:** Ứng dụng **core** (chứa thông tin Hero, Statistic, Title, Timeline của trang chủ) do đội ngũ Dev quản lý kỹ thuật trực tiếp, do đó **không** được đưa vào phạm vi hướng dẫn này.

---

## I. CÁC QUY CHUẨN CHUNG & YÊU CẦU KỸ THUẬT

Để website vận hành trơn tru và đạt điểm SEO/tốc độ tải trang tối ưu nhất, đội ngũ Media cần chú ý các quy chuẩn kỹ thuật sau:

### 1. Định dạng Slug (Đường dẫn tĩnh / URL thân thiện)
- **Định dạng bắt buộc:** Chỉ chứa chữ cái thường không dấu (`a-z`), chữ số (`0-9`) và dấu gạch ngang (`-`). Tuyệt đối không có khoảng trắng, dấu tiếng Việt hoặc ký tự đặc biệt khác.
- *Ví dụ đúng:* `dich-vu-tu-van-doanh-nghiep`, `xay-dung-thuong-hieu-ca-nhan-2026`.
- *Ví dụ sai:* `dịch vụ tư vấn!`, `dich_vu_tu_van`, `Dich-Vu-Tu-Van`.
- **Cách nhập:** Khi nhập tiêu đề, hệ thống Django Admin sẽ tự sinh slug. Tuy nhiên, Media Team cần rà soát lại để đảm bảo slug ngắn gọn, dễ hiểu và tối ưu SEO trước khi lưu.

### 2. Định dạng & Dung lượng Hình ảnh
- **Định dạng tối ưu:** Ưu tiên sử dụng định dạng **WebP** để có dung lượng nhẹ nhất và chất lượng tốt nhất. Nếu không có, hãy dùng **PNG** (cho ảnh nền trong suốt) hoặc **JPG** (cho ảnh chụp).
- **Nén hình ảnh:** Tất cả hình ảnh tải lên phải được nén qua các công cụ như *TinyPNG* hoặc *Squoosh*. Dung lượng của mỗi hình ảnh **không vượt quá 500KB** (lý tưởng là dưới 150KB).
- **Lưu trữ tự động:** Khi bạn tải ảnh lên qua Admin, hệ thống sẽ tự động đồng bộ hóa và tối ưu hóa trên nền tảng đám mây Cloudinary theo đường dẫn thư mục được Dev quy định.

### 3. Trình soạn thảo Rich Text (Vavan bản phong phú - TinyMCE)
- Các trường có ký hiệu **[Rich Text / HTML]** cho phép bạn tùy biến định dạng chữ: In đậm, in nghiêng, căn lề, thêm danh sách (`ul`, `ol`), chèn link liên kết, hoặc chia nhỏ bài viết bằng thẻ tiêu đề H2, H3.
- *Mẹo tránh lỗi hiển thị:* Tránh sao chép và dán trực tiếp từ các file Word hoặc Google Docs vào vì sẽ kéo theo mã định dạng ẩn bị lỗi. Thay vào đó, hãy dùng tổ hợp phím `Ctrl + Shift + V` để dán văn bản thô, sau đó dùng công cụ của hệ quản trị để định dạng lại.

### 4. Quy tắc Thứ tự hiển thị (`display_order`)
- Sử dụng số nguyên không âm (`0`, `1`, `2`, `3`...).
- Hệ thống sẽ sắp xếp các mục từ nhỏ đến lớn (số nhỏ hiển thị trước). Mặc định là `0`. Nếu muốn đẩy một mục lên đầu trang, hãy đặt giá trị là `1`, và các mục tiếp theo tăng dần lên `2`, `3`...

### 5. Biểu tượng Fonts/Mạng xã hội (`icon_class`)
- Hệ thống tích hợp thư viện **FontAwesome**. Media Team cần điền chính xác "class" của biểu tượng.
- *Cách tìm kiếm:* Lên trang chủ FontAwesome (bản Free) chọn icon mong muốn và sao chép mã class.
- *Ví dụ mẫu:* 
  - Icon mã nguồn: `fa-solid fa-code`
  - Icon điện thoại: `fa-solid fa-phone`
  - Icon bộ não/trí tuệ nhân tạo: `fa-solid fa-brain`
  - Icon Facebook: `fa-brands fa-facebook`
  - Icon LinkedIn: `fa-brands fa-linkedin-in`

---

## II. HƯỚNG DẪN CHI TIẾT TỪNG MODULE (MÔ-ĐUN HỆ THỐNG)

Dưới đây là chi tiết tất cả các mục nhập liệu tương ứng với từng ứng dụng trên hệ thống (không bao gồm core).

### 1. MODULE: `common` (Cấu hình chung toàn trang)

Mô-đun này chứa các thông số kỹ thuật, SEO, thông tin liên hệ và chân trang dùng chung cho toàn bộ website.

---

#### 📌 1.1 GeneralSettings (Cấu hình cơ bản của Website)
Dùng để quản lý tên, logo và biểu tượng nhỏ trên trình duyệt của website.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **site_name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên của website (hiển thị trên tiêu đề trình duyệt). Ví dụ: `Nguyễn Văn A - Portfolio Site`. |
| **site_logo** | Ảnh | Upload vào thư mục `site_logo/`. | Logo chính thức của website. Nên dùng ảnh PNG nền trong suốt, căn chỉnh viền khít. |
| **favicon** | Ảnh nhỏ | Upload vào thư mục `favicon/`. | Biểu tượng nhỏ hiển thị trên tab trình duyệt. Nên dùng ảnh hình vuông kích thước `32x32 px` hoặc `48x48 px` định dạng `.ico` hoặc `.png`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Trạng thái hoạt động. Nếu bỏ chọn, cấu hình này sẽ bị ẩn/ngừng áp dụng. |

---

#### 📌 1.2 SEOSettings (Cấu hình SEO chung cho trang Web)
Dùng để khai báo thông tin tối ưu hóa công cụ tìm kiếm giúp website dễ lên top Google.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **meta_title** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tiêu đề SEO hiển thị trên kết quả tìm kiếm Google. Khuyên dùng từ 50-60 ký tự chứa từ khóa chính. |
| **meta_description** | Văn bản dài | Không giới hạn ký tự. Bắt buộc. | Đoạn mô tả ngắn gọn nội dung website hiển thị dưới tiêu đề trên Google. Khuyên dùng từ 150-160 ký tự để không bị cắt ngắn. |
| **meta_keywords** | Văn bản dài | Không giới hạn ký tự. Bắt buộc. | Các từ khóa tìm kiếm liên quan, phân cách nhau bằng dấu phẩy. Ví dụ: `lập trình viên, chuyên gia AI, tư vấn công nghệ`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Cho phép áp dụng cấu hình SEO này hay không. |

---

#### 📌 1.3 ContactInfo (Thông tin liên hệ chính)
Thông tin liên hệ hiển thị ở các khu vực như header, footer và trang Liên hệ.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **email** | Email | Đúng định dạng email. Bắt buộc. | Địa chỉ email tiếp nhận thông tin từ khách hàng. Ví dụ: `contact@nguyenvana.com`. |
| **phone_number** | Chữ ngắn | Tối đa 20 ký tự. Bắt buộc. | Số điện thoại liên hệ chính thức. Ví dụ: `+84 987 654 321`. |
| **address** | Văn bản dài | Bắt buộc. | Địa chỉ văn phòng làm việc hoặc địa chỉ giao dịch chính thức. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Trạng thái hiển thị thông tin liên hệ này trên trang. |

---

#### 📌 1.4 SocialMediaLink (Liên kết Mạng xã hội)
Danh sách các tài khoản mạng xã hội để người dùng nhấn vào kết nối.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **platform_name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên mạng xã hội. Ví dụ: `Facebook`, `LinkedIn`, `GitHub`, `YouTube`. |
| **profile_url** | Đường dẫn | Phải là URL hợp lệ. Bắt buộc. | Đường link dẫn trực tiếp đến trang cá nhân. Ví dụ: `https://linkedin.com/in/nguyenvana`. |
| **icon_class** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Mã class của biểu tượng FontAwesome. Ví dụ: `fa-brands fa-linkedin-in`, `fa-brands fa-facebook`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Hiển thị hoặc ẩn nút liên kết mạng xã hội này. |

---

#### 📌 1.5 Footer (Thông tin chân trang)
Chứa thông tin bản quyền hoặc đoạn giới thiệu ngắn ở cuối trang.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **content** | Văn bản dài | Bắt buộc. | Nội dung chữ hiển thị ở chân trang. Có thể bao gồm thông tin bản quyền. Ví dụ: `© 2026 Nguyễn Văn A. All Rights Reserved.`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Cho phép hiển thị hoặc ẩn footer này. |

---

#### 📌 1.6 AnalyticsSettings (Cấu hình Tracking & Theo dõi)
Dùng để tích hợp mã theo dõi lưu lượng truy cập của bên thứ ba.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **google_analytics_id** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Mã đo lường của Google Analytics 4. Định dạng dạng: `G-XXXXXXXXXX`. |
| **facebook_pixel_id** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | ID của Facebook Pixel để đo lường chuyển đổi từ quảng cáo. Định dạng: Dãy số nguyên. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt các mã theo dõi này trên trang web. |

---

### 2. MODULE: `services` (Quản lý dịch vụ cung cấp)

Mô-đun này lưu trữ thông tin về các gói dịch vụ (Tư vấn, Đào tạo, Phát triển phần mềm...) và phản hồi từ những khách hàng đã sử dụng dịch vụ.

---

#### 📌 2.1 ServiceCategory (Danh mục dịch vụ)
Dùng để phân nhóm các dịch vụ (ví dụ: nhóm dịch vụ "AI & Machine Learning", nhóm "Web Development").

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên danh mục dịch vụ. Ví dụ: `Trí tuệ nhân tạo (AI) & Học máy`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Xem phần quy chuẩn slug. Ví dụ: `tri-tue-nhan-tao-ai-va-hoc-may`. |
| **description** | Văn bản dài | Bắt buộc. | Mô tả ngắn về danh mục này để khách hàng hiểu nhóm này gồm những dịch vụ gì. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Cho hiển thị danh mục này và các dịch vụ thuộc về nó hay ẩn đi. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự ưu tiên hiển thị của danh mục này trên trang dịch vụ. |

---

#### 📌 2.2 Services (Chi tiết dịch vụ)
Nội dung chi tiết của từng dịch vụ cụ thể.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **category** | Chọn từ danh sách | Liên kết khóa ngoại. Bắt buộc. | Chọn Danh mục dịch vụ (ở mục 2.1) mà dịch vụ này thuộc về. |
| **title** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên dịch vụ cụ thể. Ví dụ: `Tích Hợp Trợ Lý Ảo AI Cho Doanh Nghiệp`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của dịch vụ. Ví dụ: `tich-hop-tro-ly-ao-ai-cho-doanh-nghiep`. |
| **icon_class** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Class FontAwesome đại diện cho dịch vụ. Ví dụ: `fa-solid fa-robot`. |
| **short_description** | Văn bản dài | Bắt buộc. | Đoạn tóm tắt ngắn từ 2-3 câu mô tả dịch vụ (sẽ hiển thị ở trang danh sách dịch vụ). |
| **description** | **Rich Text / HTML** | Bắt buộc. Soạn thảo TinyMCE. | Mô tả chi tiết dịch vụ: quy trình làm việc, lợi ích khách hàng nhận được, các công nghệ sử dụng, bảng giá,... |
| **image** | Ảnh | Tải lên thư mục `ai_development/`. | Ảnh bìa/ảnh minh họa chính cho dịch vụ. Kích thước chuẩn khuyến nghị: `800x600 px`. |
| **delivery_mode** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Hình thức làm việc/bàn giao. Ví dụ: `Online & Offline`, `Remote toàn phần`. |
| **timeline** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Thời gian hoàn thành dự kiến. Ví dụ: `2 - 4 tuần`, `Theo từng giai đoạn`. |
| **response_time** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Thời gian phản hồi hỗ trợ. Ví dụ: `Dưới 2 giờ`, `24/7 đối với sự cố khẩn cấp`. |
| **featured** | Checkbox | Mặc định bỏ chọn (False). | Tích chọn nếu muốn đưa dịch vụ này làm "Dịch vụ nổi bật" hiển thị trực tiếp trên trang chủ. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt hiển thị dịch vụ này trên website. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị giữa các dịch vụ trong cùng một trang hoặc danh mục. |

---

#### 📌 2.3 FAQ (Câu hỏi thường gặp về dịch vụ)
Các câu hỏi và câu trả lời giúp giải đáp thắc mắc nhanh cho khách hàng ở trang chi tiết dịch vụ.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **service** | Chọn từ danh sách | Liên kết khóa ngoại. Bắt buộc. | Chọn Dịch vụ cụ thể (ở mục 2.2) mà câu hỏi này giải đáp trực tiếp. |
| **question** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Nội dung câu hỏi của khách hàng. Ví dụ: `Tôi có được hỗ trợ kỹ thuật sau khi bàn giao sản phẩm không?`. |
| **answer** | Văn bản dài | Bắt buộc. | Nội dung câu trả lời/giải đáp chi tiết cho câu hỏi trên. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Cho phép hiển thị hoặc ẩn câu hỏi này. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị từ trên xuống dưới của bộ câu hỏi FAQ thuộc dịch vụ này. |

---

#### 📌 2.4 Testimonial (Ý kiến đánh giá từ khách hàng)
Những lời nhận xét, đánh giá của đối tác và khách hàng cũ để gia tăng độ uy tín.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Họ và tên khách hàng hoặc người đại diện doanh nghiệp. Ví dụ: `Trần Thị B`. |
| **title** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Chức danh nghề nghiệp của khách hàng. Ví dụ: `Giám đốc Marketing`, `Founder & CEO`. |
| **company** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Tên công ty/tổ chức của khách hàng đó. Ví dụ: `Vinamilk`, `FPT Software`. |
| **testimonial** | Văn bản dài | Bắt buộc. | Nội dung lời chứng thực/nhận xét/đánh giá từ khách hàng về chất lượng dịch vụ. |
| **image** | Ảnh | Tải lên thư mục `testimonials/`. | Ảnh chân dung (avatar) của khách hàng. Khuyến nghị ảnh vuông tỷ lệ `1:1` (ví dụ: `400x400 px`), chất lượng rõ nét. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Trạng thái hiển thị lời đánh giá này lên website. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự sắp xếp các đánh giá trên slide/khung hiển thị. |

---

### 3. MODULE: `portfolio` (Quản lý dự án, sản phẩm và kỹ năng)

Mô-đun này quan trọng nhất đối với trang Portfolio cá nhân, dùng để lưu trữ các sản phẩm/dự án đã thực hiện và hiển thị các kỹ năng công nghệ hiện có.

---

#### 📌 3.1 ProjectCategory (Danh mục dự án)
Phân loại các dự án (ví dụ: "Dự án nguồn mở", "Sản phẩm thương mại", "Nghiên cứu khoa học").

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên nhóm dự án. Ví dụ: `Mobile Apps (Ứng dụng di động)`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của danh mục dự án. Ví dụ: `mobile-apps-ung-dung-di-dong`. |
| **description** | Văn bản dài | Bắt buộc. | Mô tả ngắn gọn về đặc điểm của các dự án nằm trong nhóm này. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt hiển thị danh mục dự án này trên bộ lọc tìm kiếm của website. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự sắp xếp danh mục trên thanh điều hướng/bộ lọc dự án. |

---

#### 📌 3.2 Skill (Kỹ năng chuyên môn)
Danh sách các công cụ, ngôn ngữ lập trình, hoặc kỹ năng mềm mà chủ website sở hữu.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên kỹ năng/công cụ. Ví dụ: `Python`, `Docker`, `Machine Learning`. |
| **proficiency** | Số nguyên | **Từ 0 đến 100**. Bắt buộc. | Mức độ thành thạo tính theo đơn vị phần trăm (%). Ví dụ điền: `85` đại diện cho thành thạo 85%. |
| **icon_class** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Mã class icon từ FontAwesome để đại diện trực quan cho công nghệ. Ví dụ: `fa-brands fa-python`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt hiển thị kỹ năng này trên phần tiến trình của trang. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị của kỹ năng trong danh sách kỹ năng chuyên môn. |

---

#### 📌 3.3 Project (Thông tin dự án chi tiết)
Thông tin chi tiết về từng dự án/sản phẩm công nghệ đã thực hiện.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **category** | Chọn từ danh sách | Liên kết khóa ngoại. Bắt buộc. | Chọn nhóm danh mục dự án tương ứng (đã tạo ở mục 3.1). |
| **skills** | Chọn nhiều | Liên kết Many-to-Many. Bắt buộc. | Chọn danh sách các công nghệ/kỹ năng được áp dụng trong dự án này (chọn từ danh sách Skill ở mục 3.2). |
| **title** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên dự án. Ví dụ: `Hệ Thống Phân Tích Hành Vi Người Dùng Bằng AI`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của dự án. Ví dụ: `he-thong-phan-tich-hanh-vi-nguoi-dung-bang-ai`. |
| **short_description** | Văn bản dài | Bắt buộc. | Đoạn tóm tắt rất ngắn hiển thị ở trang danh sách dự án hoặc card dự án. |
| **description** | **Rich Text / HTML** | Bắt buộc. Soạn thảo TinyMCE. | Bài viết giới thiệu chi tiết về dự án: Mục tiêu, kiến trúc hệ thống, quy trình thực hiện, kết quả đạt được, bài học rút ra... |
| **image** | Ảnh | Tải lên thư mục `projects/`. | Ảnh đại diện chính (Cover Image/Thumbnail) của dự án. Kích thước khuyến nghị: `1200x800 px` hoặc tỷ lệ `3:2`. |
| **github_url** | Đường dẫn | URL hợp lệ. Có thể để trống. | Link dẫn đến kho mã nguồn GitHub của dự án (nếu dự án là mã nguồn mở). Ví dụ: `https://github.com/nguyenvana/my-project`. |
| **live_url** | Đường dẫn | URL hợp lệ. Có thể để trống. | Link dẫn đến phiên bản đang chạy thử nghiệm trực tiếp (Live Demo) của sản phẩm. Ví dụ: `https://my-demo-project.com`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Cho phép hiển thị dự án ra ngoài công chúng. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị dự án trên lưới trình diễn (Grid). |

---

#### 📌 3.4 Image (Bộ sưu tập ảnh chi tiết của dự án)
Bảng này dùng để thêm nhiều ảnh chi tiết khác hiển thị dưới dạng gallery trượt hoặc lưới ảnh bên trong trang chi tiết dự án.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **project** | Chọn từ danh sách | Liên kết khóa ngoại. Bắt buộc. | Chọn Dự án cụ thể (ở mục 3.3) mà hình ảnh này thuộc về để chèn vào thư viện ảnh của nó. |
| **image** | Ảnh | Tải lên thư mục `project_images/`. | Ảnh chi tiết (ví dụ: Ảnh chụp màn hình tính năng, sơ đồ hệ thống, quy trình thiết kế). Kích thước chuẩn: `1920x1080 px` hoặc tỷ lệ tương tự ảnh bìa. |
| **caption** | Chữ ngắn | Tối đa 255 ký tự. Có thể để trống. | Chú thích ngắn gọn hiển thị phía dưới hoặc khi di chuột vào ảnh. Ví dụ: `Giao diện màn hình phân tích biểu đồ thống kê`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt ảnh này trong bộ sưu tập. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị các ảnh con trong slide/bộ sưu tập ảnh của dự án đó. |

---

### 4. MODULE: `contact` (Quản lý hòm thư liên hệ)

Bảng này dùng để ghi nhận các liên hệ từ khách hàng gửi qua form liên hệ trên website.

---

#### 📌 4.1 ContactMessage (Thư liên hệ từ Khách hàng)
> [!NOTE]
> Bảng này do người dùng bên ngoài điền và gửi tự động từ biểu mẫu (Form) trên website vào cơ sở dữ liệu. Đội ngũ Media **không tự nhập thủ công**.
> Tuy nhiên, Media Team hoặc đội ngũ Vận hành cần biết cấu trúc thông tin để kiểm tra, phản hồi thông tin hoặc quản trị khách hàng tiềm năng (Leads).

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Ý Nghĩa & Định Dạng Dữ Liệu |
| :--- | :--- | :--- |
| **name** | Chữ ngắn | Họ tên của khách hàng gửi yêu cầu tư vấn/liên hệ (Tối đa 255 ký tự). |
| **email** | Email | Địa chỉ email của khách hàng để nhận phản hồi từ ban quản trị. |
| **subject** | Chữ ngắn | Tiêu đề của thư liên hệ (Tối đa 255 ký tự). Ví dụ: `Yêu cầu báo giá dịch vụ AI`. |
| **message** | Văn bản dài | Nội dung lời nhắn chi tiết của khách hàng nêu rõ nhu cầu hoặc câu hỏi cụ thể. |
| **created_at** | Thời gian | Thời điểm khách hàng nhấn gửi thư (Hệ thống tự động lưu). |

---

### 5. MODULE: `blog` (Quản lý viết bài & Blog tin tức)

Mô-đun dùng để quản lý các hoạt động viết bài chia sẻ kiến thức, kinh nghiệm, thông báo tin tức và tối ưu hóa SEO bài viết.

---

#### 📌 5.1 PostCategory (Danh mục bài viết)
Phân loại chủ đề cho các bài viết trên blog (ví dụ: "Hướng dẫn lập trình", "Cập nhật công nghệ", "Chia sẻ kinh nghiệm").

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên danh mục bài viết. Ví dụ: `Trí Tuệ Nhân Tạo & Đời Sống`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của danh mục. Ví dụ: `tri-tue-nhan-tao-va-doi-song`. |
| **description** | **Rich Text / HTML** | Bắt buộc. Soạn thảo TinyMCE. | Đoạn giới thiệu chi tiết về chủ đề này, sẽ xuất hiện ở đầu trang danh mục bài viết. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt hiển thị danh mục bài viết này trên trang blog. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị của danh mục này trong thanh công cụ lọc chủ đề của blog. |

---

#### 📌 5.2 Tag (Thẻ bài viết)
Các từ khóa phụ phân loại bài viết nhỏ hơn danh mục, giúp người dùng dễ gom nhóm bài viết liên quan nhanh.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **name** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tên thẻ. Ví dụ: `Django`, `Machine Learning`, `Tutorial`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của thẻ tag. Ví dụ: `django`, `machine-learning`, `tutorial`. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật/tắt hiển thị và hoạt động của thẻ này. |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Thứ tự hiển thị sắp xếp nếu thẻ được hiển thị trong đám mây từ khóa (Tag Cloud). |

---

#### 📌 5.3 Post (Nội dung bài viết Blog chi tiết)
Nơi viết và biên tập các nội dung bài viết chi tiết trên website.

| Tên Trường (Trong Admin) | Kiểu Dữ Liệu | Yêu Cầu / Ràng Buộc | Ý Nghĩa & Hướng Dẫn Nội Dung |
| :--- | :--- | :--- | :--- |
| **category** | Chọn từ danh sách | Liên kết khóa ngoại. Bắt buộc. | Chọn Danh mục bài viết (ở mục 5.1) mà bài viết này thuộc về. |
| **tags** | Chọn nhiều | Liên kết Many-to-Many. Bắt buộc. | Chọn các Thẻ liên quan (ở mục 5.2) để gắn nhãn phân loại bổ sung cho bài viết. |
| **title** | Chữ ngắn | Tối đa 255 ký tự. Bắt buộc. | Tiêu đề của bài viết. Ví dụ: `Hướng Dẫn Từng Bước Tự Học Lập Trình Python Trong 30 Ngày`. |
| **slug** | Đường dẫn | Phải duy nhất (Unique). Bắt buộc. | Đường dẫn tĩnh của bài viết. Ví dụ: `huong-dan-tung-buoc-tu-hoc-lap-trinh-python-trong-30-ngay`. |
| **content** | **Rich Text / HTML** | Bắt buộc. Soạn thảo TinyMCE. | Toàn bộ bài viết chi tiết. Bạn có thể sử dụng các thẻ tiêu đề (H2, H3) phân cấp nội dung, chèn liên kết, hình ảnh trong bài viết, bôi đậm từ khóa quan trọng để tối ưu hóa SEO. |
| **is_active** | Checkbox | Mặc định tích chọn (True). | Bật để đăng bài ngay lên trang web. Bỏ tích chọn để giữ bài viết ở chế độ "Lưu nháp" (Chỉ Admin nhìn thấy). |
| **display_order** | Số nguyên | Số không âm. Mặc định `0`. | Cho phép ghim bài viết lên vị trí đầu bằng cách đặt số thứ tự nhỏ hơn hoặc sắp xếp theo mục tiêu truyền thông cụ thể. |

---

## III. CHECKLIST KIỂM TRA CHẤT LƯỢNG TRƯỚC KHI LƯU (LƯU Ý DÀNH CHO MEDIA TEAM)

Trước khi nhấn nút **Lưu (Save)** trong bảng quản trị Django Admin, Media Team cần rà soát lại thông tin theo checklist sau để đảm bảo nội dung hoàn chỉnh nhất:

1. [ ] **Slug hợp lệ:** Slug đã được kiểm tra không còn chữ in hoa, không còn khoảng trắng và không bị lỗi mã tiếng Việt?
2. [ ] **Kích thước ảnh:** Ảnh đại diện dịch vụ, ảnh đại diện dự án, ảnh chân dung khách hàng đều đã được chuyển sang định dạng WebP/PNG/JPG và được nén dưới 500KB chưa?
3. [ ] **Định dạng biểu tượng:** Biểu tượng FontAwesome đã được điền đúng class chưa? (Hãy copy chính xác từ trang chủ FontAwesome, ví dụ: `fa-solid fa-envelope`).
4. [ ] **Các liên kết ngoài:** Các trường URL (`github_url`, `live_url`, `profile_url`) đã điền đầy đủ giao thức `https://` và hoạt động bình thường khi click thử chưa?
5. [ ] **Trường Kỹ năng (`proficiency`):** Giá trị nhập vào cho kỹ năng có nằm trong khoảng từ `0` đến `100` (%) chưa?
6. [ ] **Bản quyền & SEO:** Các bài viết blog và thông tin SEO đã có đầy đủ `meta_title`, `meta_description` thu hút và thân thiện với SEO chưa?
7. [ ] **Trạng thái hiển thị:** Trường trạng thái `is_active` đã được bật (tích chọn) cho các nội dung cần hiển thị ngay chưa?

---
*Tài liệu này được soạn thảo và đồng bộ trực tiếp với mã nguồn và cấu trúc cơ sở dữ liệu của dự án. Mọi thay đổi về cấu trúc bảng hoặc thêm mới các trường dữ liệu ở phía Dev sẽ được cập nhật đồng thời vào tài liệu này.*
