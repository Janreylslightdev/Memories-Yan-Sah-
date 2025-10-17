# TODO: Add Delete Album Feature

## Steps to Complete:
- [x] Add delete_album route in blueprints/albums.py
  - Check album ownership
  - Delete all associated images (files and DB records)
  - Delete the album itself
- [x] Update templates/albums.html
  - Add delete button for each album
  - Include confirmation dialog for safety
- [ ] Test the delete functionality
  - Create an album with images and delete it
  - Verify images are removed from filesystem and database
  - Check that only album owner can delete their albums
