# Online Gallery

A modern web application for managing personal photo galleries with user authentication, album organization, and image upload capabilities.

## Features

- 🔐 User authentication (register/login/logout)
- 📁 Album creation and management
- 🖼️ Image upload with bulk support
- ⭐ Album cover setting
- 🗑️ Secure album deletion with cleanup
- 📱 Responsive design
- 🔒 Secure file handling

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd online-gallery
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Production Deployment

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI

2. Initialize a git repository (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

3. Create a Heroku app:
```bash
heroku create your-app-name
```

4. Set environment variables:
```bash
heroku config:set SECRET_KEY=your-super-secret-key-here
```

5. Deploy to Heroku:
```bash
git push heroku main
```

6. Open your app:
```bash
heroku open
```

### Environment Variables

- `SECRET_KEY`: Flask secret key for sessions (required in production)
- `DATABASE_URL`: Database connection string (optional, defaults to SQLite)
- `PORT`: Port for the server (automatically set by Heroku)

### Database

The application uses SQLite by default, which is suitable for development and small-scale production. For larger deployments, consider using PostgreSQL.

## Project Structure

```
online-gallery/
├── app.py                 # Main Flask application
├── wsgi.py               # WSGI entry point for production
├── models.py             # Database models
├── requirements.txt      # Python dependencies
├── Procfile              # Heroku deployment configuration
├── blueprints/           # Flask blueprints
│   ├── auth.py          # Authentication routes
│   ├── albums.py        # Album management routes
│   └── images.py        # Image management routes
├── templates/            # Jinja2 templates
├── static/               # Static files (CSS, JS, images)
└── README.md            # This file
```

## Security Features

- Password hashing with Werkzeug
- User session management with Flask-Login
- File upload restrictions (16MB max, image types only)
- CSRF protection
- SQL injection prevention with SQLAlchemy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
