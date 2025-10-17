from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from models import Album, Image, db

images_bp = Blueprint('images', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@images_bp.route('/upload/<int:album_id>', methods=['GET', 'POST'])
@login_required
def upload_images(album_id):
    album = Album.query.get_or_404(album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))
    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            if file and allowed_file(file.filename):
                original_filename = file.filename
                filename = secure_filename(file.filename)
                from flask import current_app
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                new_image = Image(filename=filename, original_filename=original_filename, album_id=album_id)
                db.session.add(new_image)
        db.session.commit()
        flash('Images uploaded successfully!')
        return redirect(url_for('albums.view_album', album_id=album_id))
    return render_template('upload.html', album=album)

@images_bp.route('/delete/<int:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    album = Album.query.get(image.album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))
    from flask import current_app
    os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename))
    db.session.delete(image)
    db.session.commit()
    flash('Image deleted successfully!')
    return redirect(url_for('albums.view_album', album_id=album.id))
