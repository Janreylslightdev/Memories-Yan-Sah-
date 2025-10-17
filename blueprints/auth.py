from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('auth.register'))
        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('albums.list_albums'))
        flash('Invalid username or password.')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'change_username':
            new_username = request.form.get('new_username')
            if User.query.filter_by(username=new_username).first():
                flash('Username already exists.')
                return redirect(url_for('auth.settings'))
            current_user.username = new_username
            db.session.commit()
            flash('Username updated successfully!')
        elif action == 'change_password':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            if not check_password_hash(current_user.password_hash, current_password):
                flash('Current password is incorrect.')
                return redirect(url_for('auth.settings'))
            current_user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            flash('Password updated successfully!')
        return redirect(url_for('auth.settings'))
    return render_template('settings.html')
