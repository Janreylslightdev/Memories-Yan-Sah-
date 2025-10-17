from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import Album, db
import os

albums_bp = Blueprint('albums', __name__)

@albums_bp.route('/')
@login_required
def list_albums():
    albums = Album.query.filter_by(user_id=current_user.id).all()
    return render_template('albums.html', albums=albums)

@albums_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_album():
    if request.method == 'POST':
        name = request.form.get('name')
        new_album = Album(name=name, user_id=current_user.id)
        db.session.add(new_album)
        db.session.commit()
        flash('Album created successfully!')
        return redirect(url_for('albums.list_albums'))
    return render_template('create_album.html')

@albums_bp.route('/<int:album_id>')
@login_required
def view_album(album_id):
    album = Album.query.get_or_404(album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))
    return render_template('album.html', album=album)

@albums_bp.route('/<int:album_id>/set_cover')
@login_required
def set_cover(album_id):
    album = Album.query.get_or_404(album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))
    return render_template('set_cover.html', album=album)

@albums_bp.route('/<int:album_id>/update_cover/<int:image_id>', methods=['POST'])
@login_required
def update_cover(album_id, image_id):
    album = Album.query.get_or_404(album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))

    # Verify the image belongs to this album
    image = None
    for img in album.images:
        if img.id == image_id:
            image = img
            break

    if not image:
        flash('Image not found in this album.')
        return redirect(url_for('albums.set_cover', album_id=album_id))

    album.cover_image_id = image_id
    db.session.commit()
    flash('Album cover updated successfully!')
    return redirect(url_for('albums.list_albums'))

@albums_bp.route('/<int:album_id>/delete', methods=['POST'])
@login_required
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)
    if album.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('albums.list_albums'))

    # Delete all associated image files
    from flask import current_app
    for image in album.images:
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    # Delete the album (this will cascade delete images due to foreign key)
    db.session.delete(album)
    db.session.commit()
    flash('Album deleted successfully!')
    return redirect(url_for('albums.list_albums'))
