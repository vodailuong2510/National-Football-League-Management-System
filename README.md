# National Football League Management System ⚽

Hệ thống quản lý giải đấu bóng đá quốc gia là một ứng dụng web Django toàn diện cho phép quản lý và theo dõi các giải đấu bóng đá, câu lạc bộ, cầu thủ, huấn luyện viên và trận đấu một cách hiệu quả.

## 🌟 Tính năng chính

- **Quản lý Giải đấu**: Tạo, chỉnh sửa và theo dõi các giải đấu bóng đá
- **Quản lý Câu lạc bộ**: Quản lý thông tin đội bóng, sân vận động và cầu thủ
- **Quản lý Cầu thủ**: Theo dõi thông tin chi tiết cầu thủ, vị trí, thống kê
- **Quản lý Huấn luyện viên**: Quản lý thông tin HLV và liên kết với câu lạc bộ
- **Quản lý Trận đấu**: Lập lịch, cập nhật kết quả và tính toán bảng xếp hạng
- **Hệ thống Người dùng**: Đăng ký, đăng nhập và quản lý hồ sơ cá nhân
- **Theo dõi**: Người dùng có thể theo dõi câu lạc bộ, cầu thủ, HLV và giải đấu yêu thích
- **Giao diện thân thiện**: Thiết kế responsive và dễ sử dụng

## 🏗️ Kiến trúc hệ thống

```
National-Football-League-Management-System/
├── Web/                     # Cấu hình Django chính
│   ├── settings.py         # Cài đặt Django
│   ├── urls.py             # URL routing chính
│   └── wsgi.py             # WSGI configuration
├── home/                   # Ứng dụng trang chủ
│   ├── views.py           # Views trang chủ
│   ├── templates/         # Templates HTML
│   └── static/            # CSS, JS, Images
├── account/               # Quản lý tài khoản người dùng
│   ├── models.py          # Models người dùng
│   ├── views.py           # Views đăng nhập/đăng ký
│   └── templates/         # Templates tài khoản
├── club/                  # Quản lý câu lạc bộ
│   ├── models.py          # Model Club
│   ├── views.py           # Views CRUD câu lạc bộ
│   └── templates/         # Templates câu lạc bộ
├── player/                # Quản lý cầu thủ
│   ├── models.py          # Model Player
│   ├── views.py           # Views CRUD cầu thủ
│   └── templates/         # Templates cầu thủ
├── coach/                 # Quản lý huấn luyện viên
│   ├── models.py          # Model Coach
│   ├── views.py           # Views CRUD HLV
│   └── templates/         # Templates HLV
├── league/                # Quản lý giải đấu
│   ├── models.py          # Model League
│   ├── views.py           # Views CRUD giải đấu
│   └── templates/         # Templates giải đấu
├── match/                 # Quản lý trận đấu
│   ├── models.py          # Models Match & Ranking
│   ├── views.py           # Views quản lý trận đấu
│   ├── signals.py         # Signals tự động cập nhật
│   └── templates/         # Templates trận đấu
├── media/                 # Lưu trữ file upload
├── manage.py              # Django management script
├── requirements.txt       # Dependencies Python
└── dockerfile            # Docker configuration
```

## 🛠️ Công nghệ sử dụng

### Backend
- **Django 5.1.4**: Web framework chính
- **SQLite**: Cơ sở dữ liệu (có thể chuyển sang PostgreSQL/MySQL)
- **Python 3.10+**: Ngôn ngữ lập trình

### Frontend
- **HTML5/CSS3**: Giao diện người dùng
- **JavaScript**: Tương tác client-side
- **Bootstrap**: Framework CSS (nếu sử dụng)

### AI/ML (Tùy chọn)
- **TensorFlow**: Machine learning
- **OpenCV**: Xử lý hình ảnh
- **spaCy**: Xử lý ngôn ngữ tự nhiên

## 🚀 Cài đặt và thiết lập

### Yêu cầu hệ thống
- Python 3.10+
- pip (Python package manager)
- Git

### Cài đặt

1. **Clone repository**
```bash
git clone <repository-url>
cd National-Football-League-Management-System
```

2. **Tạo môi trường ảo**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Cài đặt dependencies**
```bash
pip install -r requirements.txt
```

4. **Chạy migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Tạo superuser (tùy chọn)**
```bash
python manage.py createsuperuser
```

6. **Chạy server**
```bash
python manage.py runserver
```

7. **Truy cập ứng dụng**
- Mở trình duyệt và truy cập: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin/`

## 📊 Cấu trúc cơ sở dữ liệu

### Models chính

#### Club (Câu lạc bộ)
- CLUBID: ID duy nhất
- LOGO: Logo câu lạc bộ
- FOUNDED: Ngày thành lập
- EMAIL, PHONE: Thông tin liên hệ
- STADIUM, CAPACITY: Sân vận động
- TOTALPLAYERS: Số cầu thủ
- LEAGUEPLAYING: Giải đấu đang tham gia

#### Player (Cầu thủ)
- PLAYERID: ID duy nhất
- PLAYERNAME: Tên cầu thủ
- BIRTHDAY: Ngày sinh
- NATIONALITY: Quốc tịch
- CLUBID: Liên kết với câu lạc bộ
- POSITION: Vị trí (GK/DF/MF/FW)
- SHIRTNUM: Số áo
- HEIGHT, WEIGHT: Chiều cao, cân nặng
- PREFERFOOT: Chân thuận

#### Coach (Huấn luyện viên)
- COACHID: ID duy nhất
- COACHNAME: Tên HLV
- BIRTHDAY: Ngày sinh
- NATIONALITY: Quốc tịch
- CLUBID: Liên kết với câu lạc bộ

#### League (Giải đấu)
- LEAGUE_ID: ID duy nhất
- LOGO: Logo giải đấu
- TOTAL_CLUB: Số câu lạc bộ tham gia
- ASSOCIATION: Hiệp hội
- FOUNDED: Ngày thành lập
- START_TIME, END_TIME: Thời gian diễn ra

#### Match (Trận đấu)
- MATCHID: ID duy nhất
- LEAGUEID: Liên kết với giải đấu
- HOMETEAM, AWAYTEAM: Đội nhà và đội khách
- ROUND: Vòng đấu
- DATE, TIME: Ngày và giờ thi đấu
- STADIUM: Sân vận động
- REFEREE: Trọng tài
- HOMESCORE, AWAYSCORE: Tỷ số

#### Ranking (Bảng xếp hạng)
- LEAGUE, CLUB: Liên kết với giải đấu và câu lạc bộ
- PLAYED, WON, DRAWN, LOST: Số trận đã đấu, thắng, hòa, thua
- GOALS_FOR, GOALS_AGAINST: Bàn thắng ghi được và bị thủng lưới
- GOAL_DIFFERENCE: Hiệu số bàn thắng
- POINTS: Điểm số

## 🔧 Tính năng chi tiết

### Quản lý Giải đấu
- Tạo giải đấu mới với thông tin chi tiết
- Chỉnh sửa thông tin giải đấu
- Xem danh sách tất cả giải đấu
- Xóa giải đấu (với xác nhận)

### Quản lý Câu lạc bộ
- Đăng ký câu lạc bộ mới
- Cập nhật thông tin câu lạc bộ
- Upload logo câu lạc bộ
- Xem danh sách câu lạc bộ
- Theo dõi câu lạc bộ yêu thích

### Quản lý Cầu thủ
- Thêm cầu thủ mới với thông tin chi tiết
- Chỉnh sửa thông tin cầu thủ
- Upload ảnh cầu thủ
- Phân loại theo vị trí
- Theo dõi cầu thủ yêu thích

### Quản lý Trận đấu
- Tạo trận đấu mới
- Cập nhật kết quả trận đấu
- Tự động tính toán bảng xếp hạng
- Xem lịch thi đấu
- Quản lý thông tin trọng tài

### Hệ thống Người dùng
- Đăng ký tài khoản mới
- Đăng nhập/Đăng xuất
- Quản lý hồ sơ cá nhân
- Đổi mật khẩu
- Theo dõi các đối tượng yêu thích

## 🎯 Sử dụng

### 1. Truy cập hệ thống
- Mở trình duyệt và truy cập: `http://localhost:8000`
- Đăng ký tài khoản mới hoặc đăng nhập

### 2. Quản lý giải đấu
- Tạo giải đấu mới từ menu "Giải đấu"
- Thêm câu lạc bộ tham gia
- Lập lịch thi đấu

### 3. Quản lý câu lạc bộ
- Đăng ký câu lạc bộ mới
- Thêm cầu thủ và huấn luyện viên
- Cập nhật thông tin

### 4. Theo dõi trận đấu
- Xem lịch thi đấu
- Cập nhật kết quả
- Xem bảng xếp hạng tự động

## 🔧 Phát triển

### Cấu trúc project
- **Web/**: Cấu hình Django chính
- **home/**: Ứng dụng trang chủ
- **account/**: Quản lý tài khoản
- **club/**: Quản lý câu lạc bộ
- **player/**: Quản lý cầu thủ
- **coach/**: Quản lý huấn luyện viên
- **league/**: Quản lý giải đấu
- **match/**: Quản lý trận đấu

### API Endpoints
- `/`: Trang chủ
- `/admin/`: Admin panel
- `/account/`: Quản lý tài khoản
- `/club/`: Quản lý câu lạc bộ
- `/player/`: Quản lý cầu thủ
- `/coach/`: Quản lý huấn luyện viên
- `/league/`: Quản lý giải đấu
- `/match/`: Quản lý trận đấu

### Thêm tính năng mới
1. Tạo model trong app tương ứng
2. Tạo views và forms
3. Tạo templates HTML
4. Cập nhật URLs
5. Chạy migrations

## 🐳 Docker (Tùy chọn)

### Build image
```bash
docker build -t nfl-management-system .
```

### Run container
```bash
docker run -p 8000:8000 nfl-management-system
```

## 📝 Ghi chú

- Hệ thống sử dụng SQLite làm cơ sở dữ liệu mặc định
- Có thể chuyển sang PostgreSQL hoặc MySQL cho production
- Tất cả file upload được lưu trong thư mục `media/`
- Hệ thống hỗ trợ đa ngôn ngữ (hiện tại chủ yếu tiếng Việt)

## 🤝 Đóng góp

1. Fork project
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 📞 Liên hệ
- Email: support@myleagueuit.com
- Project Link: [https://github.com/your-username/national-football-league-management-system](https://github.com/your-username/national-football-league-management-system)

---

**MyLeagueUIT.com** - Hệ thống quản lý giải đấu bóng đá chuyên nghiệp ⚽
