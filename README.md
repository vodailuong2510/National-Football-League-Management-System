# National Football League Management System ⚽

The National Football League Management System is a comprehensive Django web application that allows efficient management and tracking of football leagues, clubs, players, coaches, and matches.

## 🌟 Key Features

- **League Management**: Create, edit, and track football leagues
- **Club Management**: Manage team information, stadiums, and players
- **Player Management**: Track detailed player information, positions, and statistics
- **Coach Management**: Manage coach information and club associations
- **Match Management**: Schedule, update results, and calculate rankings
- **User System**: Registration, login, and personal profile management
- **Follow System**: Users can follow their favorite clubs, players, coaches, and leagues
- **User-Friendly Interface**: Responsive design and easy-to-use interface

## 🏗️ System Architecture

```
National-Football-League-Management-System/
├── Web/                     # Main Django configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── home/                   # Home page application
│   ├── views.py           # Home page views
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, Images
├── account/               # User account management
│   ├── models.py          # User models
│   ├── views.py           # Login/registration views
│   └── templates/         # Account templates
├── club/                  # Club management
│   ├── models.py          # Club model
│   ├── views.py           # Club CRUD views
│   └── templates/         # Club templates
├── player/                # Player management
│   ├── models.py          # Player model
│   ├── views.py           # Player CRUD views
│   └── templates/         # Player templates
├── coach/                 # Coach management
│   ├── models.py          # Coach model
│   ├── views.py           # Coach CRUD views
│   └── templates/         # Coach templates
├── league/                # League management
│   ├── models.py          # League model
│   ├── views.py           # League CRUD views
│   └── templates/         # League templates
├── match/                 # Match management
│   ├── models.py          # Match & Ranking models
│   ├── views.py           # Match management views
│   ├── signals.py         # Automatic update signals
│   └── templates/         # Match templates
├── media/                 # File upload storage
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── dockerfile            # Docker configuration
```

## 🛠️ Technologies Used

### Backend
- **Django 5.1.4**: Main web framework
- **SQLite**: Database (can be migrated to PostgreSQL/MySQL)
- **Python 3.10+**: Programming language

### Frontend
- **HTML5/CSS3**: User interface
- **JavaScript**: Client-side interactions
- **Bootstrap**: CSS framework (if used)

### AI/ML (Optional)
- **TensorFlow**: Machine learning
- **OpenCV**: Image processing
- **spaCy**: Natural language processing

## 🚀 Installation and Setup

### System Requirements
- Python 3.10+
- pip (Python package manager)
- Git

### Installation

1. **Clone repository**
```bash
git clone <repository-url>
cd National-Football-League-Management-System
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run server**
```bash
python manage.py runserver
```

7. **Access application**
- Open browser and navigate to: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin/`

## 📊 Database Structure

### Main Models

#### Club
- CLUBID: Unique identifier
- LOGO: Club logo
- FOUNDED: Foundation date
- EMAIL, PHONE: Contact information
- STADIUM, CAPACITY: Stadium details
- TOTALPLAYERS: Number of players
- LEAGUEPLAYING: Current participating league

#### Player
- PLAYERID: Unique identifier
- PLAYERNAME: Player name
- BIRTHDAY: Date of birth
- NATIONALITY: Nationality
- CLUBID: Club association
- POSITION: Position (GK/DF/MF/FW)
- SHIRTNUM: Jersey number
- HEIGHT, WEIGHT: Physical attributes
- PREFERFOOT: Preferred foot

#### Coach
- COACHID: Unique identifier
- COACHNAME: Coach name
- BIRTHDAY: Date of birth
- NATIONALITY: Nationality
- CLUBID: Club association

#### League
- LEAGUE_ID: Unique identifier
- LOGO: League logo
- TOTAL_CLUB: Number of participating clubs
- ASSOCIATION: Association
- FOUNDED: Foundation date
- START_TIME, END_TIME: Duration

#### Match
- MATCHID: Unique identifier
- LEAGUEID: League association
- HOMETEAM, AWAYTEAM: Home and away teams
- ROUND: Match round
- DATE, TIME: Match date and time
- STADIUM: Venue
- REFEREE: Referee
- HOMESCORE, AWAYSCORE: Score

#### Ranking
- LEAGUE, CLUB: League and club associations
- PLAYED, WON, DRAWN, LOST: Matches played, won, drawn, lost
- GOALS_FOR, GOALS_AGAINST: Goals scored and conceded
- GOAL_DIFFERENCE: Goal difference
- POINTS: Points

## 🔧 Detailed Features

### League Management
- Create new leagues with detailed information
- Edit league information
- View all leagues list
- Delete leagues (with confirmation)

### Club Management
- Register new clubs
- Update club information
- Upload club logos
- View clubs list
- Follow favorite clubs

### Player Management
- Add new players with detailed information
- Edit player information
- Upload player photos
- Categorize by position
- Follow favorite players

### Match Management
- Create new matches
- Update match results
- Automatic ranking calculation
- View match schedule
- Manage referee information

### User System
- Register new accounts
- Login/Logout
- Manage personal profiles
- Change passwords
- Follow favorite entities

## 🎯 Usage

### 1. Access the system
- Open browser and navigate to: `http://localhost:8000`
- Register a new account or login

### 2. Manage leagues
- Create new leagues from the "Leagues" menu
- Add participating clubs
- Schedule matches

### 3. Manage clubs
- Register new clubs
- Add players and coaches
- Update information

### 4. Track matches
- View match schedule
- Update results
- View automatic rankings

## 🔧 Development

### Project structure
- **Web/**: Main Django configuration
- **home/**: Home page application
- **account/**: Account management
- **club/**: Club management
- **player/**: Player management
- **coach/**: Coach management
- **league/**: League management
- **match/**: Match management

### API Endpoints
- `/`: Home page
- `/admin/`: Admin panel
- `/account/`: Account management
- `/club/`: Club management
- `/player/`: Player management
- `/coach/`: Coach management
- `/league/`: League management
- `/match/`: Match management

### Adding new features
1. Create model in corresponding app
2. Create views and forms
3. Create HTML templates
4. Update URLs
5. Run migrations

## 🐳 Docker (Optional)

### Build image
```bash
docker build -t nfl-management-system .
```

### Run container
```bash
docker run -p 8000:8000 nfl-management-system
```

## 📝 Notes

- The system uses SQLite as the default database
- Can be migrated to PostgreSQL or MySQL for production
- All uploaded files are stored in the `media/` directory
- The system supports multiple languages (currently primarily Vietnamese)

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more details.

## 📞 Contact
- Email: vodailuong2510@gmail.com
- Project Link: [https://github.com/your-username/national-football-league-management-system](https://github.com/your-username/national-football-league-management-system)

---

**MyLeagueUIT.com** - Professional Football League Management System ⚽
