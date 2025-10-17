from models import db, User, Album, Image
from app import app
import os

with app.app_context():
    # Get album to delete (album 2 now)
    album = Album.query.get(2)
    if not album:
        print("Album not found")
        exit()

    print(f"Deleting album: {album.name} with {len(album.images)} images")

    # Simulate delete_album logic: delete images first, then album
    # Delete all associated image files and DB records
    upload_folder = app.config['UPLOAD_FOLDER']
    for image in album.images:
        file_path = os.path.join(upload_folder, image.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed file: {file_path}")
        else:
            print(f"File not found: {file_path}")
        db.session.delete(image)

    # Delete the album
    db.session.delete(album)
    db.session.commit()

    print("After deletion:")
    print(f"Albums: {Album.query.count()}")
    print(f"Images: {Image.query.count()}")

    # Check if files are gone
    print("Checking if files are removed from filesystem...")
    files = os.listdir(upload_folder)
    print(f"Files in upload folder: {len(files)}")
    for f in files:
        print(f" - {f}")
