# EasyHome- Service Management app

## Overview
This project consists of a **Flask-based backend** and a **Vue.js frontend** for managing service requests, handling user authentication, sending emails asynchronously, and providing an API interface.

## Features
### Backend (Flask)
- **User Authentication**: JWT-based login system.
- **Database Management**: Uses SQLAlchemy with SQLite3.
- **Email Notifications**: Flask-Mail integration for sending emails asynchronously.
- **Asynchronous Task Processing**: Celery for handling email sending in the background.
- **CORS Support**: Allows cross-origin requests.
- **Migrations**: Flask-Migrate for database schema changes.

### Frontend (Vue.js)
- **User Authentication**: JWT-based login system.
- **Role-based Routing**: Separate views for users and admins.
- **Service Browsing**: View and search available services.
- **Booking System**: Users can book services.
- **Admin Dashboard**: Manage users, service providers, and bookings.

## Technologies Used
### Backend
- **Flask**: Web framework
- **Flask-JWT-Extended**: JSON Web Token (JWT) authentication
- **Flask-SQLAlchemy**: ORM for database interaction
- **Flask-Mail**: Email sending
- **Celery**: Task queue for async email sending
- **Redis**: Message broker for Celery
- **Flask-CORS**: Cross-origin resource sharing
- **Flask-Migrate**: Database migrations

### Frontend
- **Vue.js**: Frontend framework
- **Vue Router**: Client-side routing
- **Vuex (optional)**: State management
- **Axios**: API requests
- **Tailwind CSS**: Styling
- **Vite**: Build tool for fast development

## Installation

### Prerequisites
Ensure you have **Python, Sqlite3, Redis, Node.js, and npm** installed.

### Backend Setup
#### 1. Clone the Repository
```bash
git clone https://github.com/jatmanis11/mad2_project.git
cd mad2_project/backend
```

#### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
Create a `.env` file and add:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export SQLALCHEMY_DATABASE_URI="postgresql://username:password@localhost/db_name"
export JWT_SECRET_KEY="your-secret-key"
export MAIL_USERNAME="your-email@gmail.com"
export MAIL_PASSWORD="your-app-password"
export CELERY_BROKER_URL="redis://localhost:6369/0"
export CELERY_RESULT_BACKEND="redis://localhost:6369/0"
```

#### 5. Start Services
```bash
redis-server
```

#### 6. Start Celery Worker
```bash
celery -A run.celery worker --loglevel=info
```
#### 7. Start Celery Beat
```bash
celery -A run.celery beat --loglevel=info
```

#### 8. Run the Application
```bash
flask run
```

### Frontend Setup
#### 1. Clone the Repository
```bash
cd ../frontend
```

#### 2. Install Dependencies
```bash
npm install
```

#### 3. Run the Development Server
```bash
npm run dev
```

#### 4. Compile and Minify for Production
```bash
npm run build
```

## API Endpoints
### Authentication
- `POST /login`: Authenticate user and return JWT token.

### Email Services
- `POST /send-email`: Send an email asynchronously.
- `POST /send-email-csv`: Send an email with a CSV attachment.
- `POST /send-email-pdf`: Send an email with a PDF attachment.

### Service Requests
- `GET /job1`: Export completed service requests as a CSV and email admins.

## Project Structure
```bash
backend/
├── app.py           # Flask application entry point
├── models.py        # Database models
├── routes/          # API endpoints
├── tasks.py         # Celery tasks
├── config.py        # Configuration settings
├── migrations/      # Database migrations
└── requirements.txt # Dependencies

frontend/
├── src/
│   ├── components/  # Reusable components
│   ├── views/       # Page components
│   ├── router/      # Vue Router setup
│   ├── store/       # Vuex store (if used)
│   ├── assets/      # Static assets
│   ├── utils/       # Helper functions
│   └── main.js      # Application entry point
└── package.json     # Frontend dependencies
```

## Deployment
To build the frontend for production:
```bash
npm run build
```

To deploy the backend, use services like **Heroku, AWS, or DigitalOcean**.
For frontend deployment, platforms like **Vercel or Netlify** are recommended:
```bash
npm run build && npm run preview
```

## Contributors
- jatmanis1

## License
This project is licensed under the MIT License.

## Customize Configuration
See [Vite Configuration Reference](https://vite.dev/config/).

