# MarketView - Stock Market Analysis Platform

A comprehensive Django-based web application for real-time stock market analysis, news aggregation, and financial data visualization.

## 🚀 Features

### Core Functionality
- **Real-time Stock Data**: Search and view daily stock prices with interactive charts
- **Market News Aggregation**: Categorized financial news from multiple sources
- **User Authentication**: Secure signup, login, and logout functionality
- **Interactive Stock Charts**: Candlestick charts using Lightweight Charts library
- **Stock Symbol Search**: Autocomplete search functionality for stock symbols
- **Responsive Design**: Modern UI built with Bootstrap and custom CSS

### Advanced Features
- **News Sentiment Analysis**: Categorized news by topics (Blockchain, Earnings, IPO, etc.)
- **Foreign Market Data**: Access to international market data
- **User Profiles**: Customizable user profiles with portfolio links and profile pictures
- **Real-time Data**: Live stock data integration via Alpha Vantage API

## 🛠️ Technology Stack

### Backend
- **Django 5.0.6**: Web framework
- **SQLite**: Database
- **Python 3.x**: Programming language

### Frontend
- **Bootstrap**: CSS framework for responsive design
- **Lightweight Charts**: Interactive financial charts
- **Autocomplete.js**: Search functionality
- **Custom CSS**: Styling and animations

### APIs & External Services
- **Alpha Vantage API**: Stock market data and news
- **TradingView Widgets**: Advanced charting (commented out)

## 📁 Project Structure

```
ASMA-marketview/
├── ASMA/
│   ├── prediction_models.ipynb
│   └── tradingplatform/
│       ├── marketview/          # Main Django app
│       │   ├── models.py        # Database models
│       │   ├── views.py         # View functions
│       │   ├── urls.py          # URL routing
│       │   ├── forms.py         # Django forms
│       │   ├── dataread.py      # Data fetching utilities
│       │   └── static/          # Static files (CSS, JS, images)
│       ├── templates/           # HTML templates
│       ├── media/               # User uploaded files
│       └── tradingplatform/     # Django project settings
├── finalized_model.sav          # Machine learning model
└── README.md
```

## 🔌 API Endpoints

### Authentication Endpoints
- `GET/POST /marketview/register/` - User registration
- `GET/POST /marketview/user_login/` - User login
- `GET /logout/` - User logout (requires authentication)

### Market Data Endpoints
- `GET /marketview/search/` - Stock symbol search (AJAX)
- `GET /marketview/foreign_market/` - Stock price charts
- `GET/POST /marketview/news/` - Market news by category

### Admin Endpoints
- `GET /admin/` - Django admin interface

## 🗄️ Database Models

### UserProfileInfo
- `user`: OneToOneField to Django User
- `portfolio_site`: URLField for user's portfolio
- `profile_pic`: ImageField for profile picture

### NewsList
- `title`: News article title
- `thumbnail`: News image
- `date`: Publication date
- `time`: Publication time
- `source`: News source
- `author`: Article author
- `link`: Article URL
- `summary`: Article summary

## 🔧 Key Functions

### Views (`views.py`)

#### Authentication Functions
- `register(request)`: Handle user registration with profile creation
- `user_login(request)`: Authenticate and login users
- `user_logout(request)`: Logout authenticated users

#### Market Data Functions
- `search(request)`: AJAX endpoint for stock symbol search
- `foreign_market(request)`: Display stock price charts
- `news(request)`: Fetch and display categorized market news

#### Utility Functions
- `index(request)`: Homepage view

### Data Utilities (`dataread.py`)
- `Stocks.StockFrame()`: Fetch intraday stock data
- `Stocks.News()`: Fetch market news data

## 🎨 Frontend Features

### Interactive Components
- **Autocomplete Search**: Real-time stock symbol suggestions
- **Candlestick Charts**: Interactive price charts with Lightweight Charts
- **News Feed**: Categorized news display with thumbnails
- **Responsive Navigation**: Bootstrap-based navigation

### Styling
- **Custom CSS**: Modern gradient backgrounds and animations
- **Bootstrap Integration**: Responsive grid system and components
- **Professional Design**: Clean, financial industry-focused UI

## 🔑 API Configuration

### Alpha Vantage API
- **API Key**: Configured in `settings.py`
- **Endpoints Used**:
  - `TIME_SERIES_DAILY`: Daily stock prices
  - `TIME_SERIES_INTRADAY`: Intraday data
  - `SYMBOL_SEARCH`: Stock symbol search
  - `NEWS_SENTIMENT`: Market news and sentiment

### News Categories
- Blockchain, Earnings, IPO, Mergers & Acquisitions
- Financial Markets, Economy, Energy & Transportation
- Finance, Life Sciences, Manufacturing
- Real Estate & Construction, Retail & Wholesale, Technology

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- Django 5.0.6
- Alpha Vantage API key

### Installation Steps
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure Alpha Vantage API key in `settings.py`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Start development server: `python manage.py runserver`

### Environment Variables
```python
ALPHAVANTAGE_API_KEY = "your_api_key_here"
SECRET_KEY = "your_django_secret_key"
DEBUG = True  # Set to False in production
```

## 📊 Data Sources

### Stock Market Data
- **Alpha Vantage API**: Real-time and historical stock data
- **Supported Data**: Open, High, Low, Close prices
- **Timeframes**: Daily and intraday data

### News Data
- **Alpha Vantage News API**: Financial news aggregation
- **Categories**: 13 predefined financial categories
- **Features**: Sentiment analysis, source attribution

## 🔒 Security Features

- **Django Authentication**: Secure user management
- **CSRF Protection**: Built-in CSRF token validation
- **Password Hashing**: PBKDF2 password hashing
- **Login Required Decorators**: Protected views
- **Form Validation**: Server-side form validation

## 🎯 Future Enhancements

- **Machine Learning Integration**: Stock prediction models
- **Portfolio Management**: User portfolio tracking
- **Real-time Alerts**: Price alerts and notifications
- **Advanced Charting**: More chart types and indicators
- **Mobile App**: Native mobile application
- **Social Features**: User comments and sharing

## 📝 License

This project is developed as a self-learning project for stock market analysis and financial data visualization.

## 🤝 Contributing

This is a personal project for learning Django and financial data analysis. Feel free to fork and modify for your own learning purposes.

---

**Note**: This application uses the Alpha Vantage API for real-time financial data. Please ensure you have a valid API key and respect the API usage limits.
