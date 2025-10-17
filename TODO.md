# Online Gallery Development TODO

## 1. Set up Project Environment
- [x] Create virtual environment
- [x] Install Flask, SQLAlchemy, Werkzeug, and other dependencies

## 2. Create Flask App Structure
- [x] Initialize Flask app with blueprints
- [x] Set up configuration for database and uploads

## 3. Define Database Models
- [x] Create User model (id, username, password_hash)
- [x] Create Album model (id, name, user_id)
- [x] Create Image model (id, filename, album_id)
- [x] Set up database initialization

## 4. Implement Authentication
- [x] Create auth blueprint with register, login, logout routes
- [x] Add password hashing and session management
- [x] Create login/register templates

## 5. Implement Album Management
- [x] Create album blueprint with create, list, view routes
- [x] Add ownership checks
- [x] Create album templates (list, create, view)

## 6. Implement Image Management
- [x] Create image blueprint with upload, list, delete routes
- [x] Implement bulk upload functionality
- [x] Add image ownership checks
- [x] Create upload and image view templates

## 7. Create Frontend Templates and Static Files
- [x] Design base template with navigation
- [x] Add CSS for styling
- [x] Add JavaScript for bulk upload (drag-and-drop)

## 8. Test and Run Application
- [x] Run the Flask app
- [x] Test user registration, login, album creation, image upload/delete
- [x] Verify bulk upload and security features
- [x] Fix album deletion circular dependency issue
- [x] Ensure buttons are equal in size and centered
- [x] Test edge cases for album deletion (empty albums, albums with covers)
- [x] Verify file system cleanup during album deletion
