# Authentication — Quick Guide

Endpoints:
- /register/  — user registration
- /login/     — user login (Django's auth view)
- /logout/    — user logout (Django's auth view)
- /profile/   — view & edit authenticated user's profile

How it works:
- Registration: uses a `UserRegisterForm` (extends `UserCreationForm`) to create a new Django `User`.
- Profile: `Profile` model (OneToOneField to User) stores extra fields (image, bio). Signals auto-create a Profile upon user creation.
- Profile update: `profile` view uses `UserUpdateForm` and `ProfileUpdateForm`. `enctype="multipart/form-data"` required for image uploads.
- Security: All forms include CSRF tokens. Passwords are hashed by Django. Views that edit personal data are protected with `@login_required`.

To test manually:
1. Run `python manage.py migrate` and `python manage.py runserver`.
2. Create a superuser: `python manage.py createsuperuser`.
3. Register a new user at `/register/`.
4. Login at `/login/`.
5. Visit `/profile/` to edit data & upload a profile picture.

To run automated tests:
- `python manage.py test blog.tests.test_auth`