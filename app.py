from flask import Flask
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

from models import db
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

from blueprints.auth import auth_bp
from blueprints.albums import albums_bp
from blueprints.images import images_bp

app.register_blueprint(auth_bp)
app.register_blueprint(albums_bp)
app.register_blueprint(images_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
