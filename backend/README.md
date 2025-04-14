

# Flask Application with Celery, JWT, and Flask-Mail

## Overview
This Flask-based application is designed for managing service requests, sending emails asynchronously via Celery, handling user authentication using JWT, and providing an API interface with Flask-RESTful.

## Features
- **User Authentication**: JWT-based login system.
- **Database Management**: Uses SQLAlchemy with PostgreSQL.
- **Email Notifications**: Flask-Mail integration for sending emails asynchronously.
- **Asynchronous Task Processing**: Celery for handling email sending in the background.
- **CORS Support**: Allows cross-origin requests.
- **Migrations**: Flask-Migrate for database schema changes.

## Technologies Used
- **Flask**: Web framework
- **Flask-JWT-Extended**: JSON Web Token (JWT) authentication
- **Flask-SQLAlchemy**: ORM for database interaction
- **Flask-Mail**: Email sending
- **Celery**: Task queue for async email sending
- **Redis**: Message broker for Celery
- **Flask-CORS**: Cross-origin resource sharing
- **Flask-Migrate**: Database migrations

## Installation

### Prerequisites
Ensure you have Python installed along with PostgreSQL and Redis.

### 1. Clone the Repository
```bash
 git clone https://github.com/jatmanis11/mad2_project.git
 cd mad2_project/backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Update your `.env` file or modify `app.config`:
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

### 5. Start the Redis Server
```bash
redis-server
```

### 6. Start Celery Worker
```bash
celery -A run.celery worker --loglevel=info
```
### 7. Start Celery Beat
```bash
celery -A run.celery beat --loglevel=info
```

### 8. Run the Application
```bash
flask run
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


## Contributors
- jatmanis1 

