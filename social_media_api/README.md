🌐 Social Media API

This is a Django REST Framework (DRF)–powered backend for a Social Media API.
It features a custom user model, token-based authentication, and endpoints that allow users to register, log in, and view their profiles.

🚀 Features

Custom user model extending Django’s AbstractUser

Token-based authentication using DRF’s authtoken module

Secure registration and login endpoints

User profile endpoint (for authenticated users)

Scalable base for building full social media functionality (follow/unfollow, posts, likes, etc.)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd social_media_api

2️⃣ Create and Activate Virtual Environment
python -m venv venv
# Activate:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver


The server will start at:

http://127.0.0.1:8000/

🧩 User Model Overview

Model: CustomUser
File: accounts/models.py

Field	Type	Description
username	CharField	Unique identifier for each user
email	EmailField	User’s email (optional but recommended)
bio	TextField	Short user biography
profile_picture	ImageField	Optional user profile photo
followers	ManyToManyField	Self-referential relationship for following other users

Example model definition:

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)


This design allows each user to follow others without the relationship being mutual (as in most social media apps).

🔑 Authentication Setup
Installed Apps

In settings.py, ensure the following are added:

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

🧾 API Endpoints
🔹 Register User

URL: /api/accounts/register/
Method: POST

Request Body:

{
  "username": "brilliant",
  "email": "brilliant@example.com",
  "password": "mypassword123"
}


Response:

{
  "user": {
    "id": 1,
    "username": "brilliant",
    "email": "brilliant@example.com",
    "bio": null,
    "profile_picture": null,
    "followers": []
  },
  "token": "6f13b2c5a86f4a8c97e6c9a7af1c45b4d14c1e62"
}


✅ A new user account is created, and a token is automatically generated.

🔹 Login

URL: /api/accounts/login/
Method: POST

Request Body:

{
  "username": "brilliant",
  "password": "mypassword123"
}


Response:

{
  "user": {
    "id": 1,
    "username": "brilliant",
    "email": "brilliant@example.com"
  },
  "token": "6f13b2c5a86f4a8c97e6c9a7af1c45b4d14c1e62"
}


✅ Successfully authenticates a user and returns their token.

🔹 View Profile (Authenticated)

URL: /api/accounts/profile/
Method: GET

Headers:

Authorization: Token <your_token_here>


Response:

{
  "id": 1,
  "username": "brilliant",
  "email": "brilliant@example.com",
  "bio": null,
  "profile_picture": null,
  "followers": []
}


✅ Returns the currently authenticated user’s profile.

🧠 Testing the API

    🧩 Postman Test Setup

Open Postman and create a new collection called “Social Media API”. For each endpoint, we’ll create a separate request.

1️⃣ Register User

Step 1: Create a new request

Method: POST

URL: http://127.0.0.1:8000/api/accounts/register/

Step 2: Go to Body → raw → JSON and paste:

{
  "username": "brilliant",
  "email": "brilliant@example.com",
  "password": "mypassword123"
}


Step 3: Click Send

✅ Expected Response:

{
  "user": {
    "id": 1,
    "username": "brilliant",
    "email": "brilliant@example.com",
    "bio": null,
    "profile_picture": null,
    "followers": []
  },
  "token": "6f13b2c5a86f4a8c97e6c9a7af1c45b4d14c1e62"
}


Save the "token" for authenticated requests.

2️⃣ Login User

Step 1: Create a new request

Method: POST

URL: http://127.0.0.1:8000/api/accounts/login/

Step 2: Body → raw → JSON:

{
  "username": "brilliant",
  "password": "mypassword123"
}


Step 3: Click Send

✅ Expected Response:

{
  "user": {
    "id": 1,
    "username": "brilliant",
    "email": "brilliant@example.com",
    "bio": null,
    "profile_picture": null,
    "followers": []
  },
  "token": "6f13b2c5a86f4a8c97e6c9a7af1c45b4d14c1e62"
}


This confirms login works and returns a token.

3️⃣ Get Profile (Authenticated)

Step 1: Create a new request

Method: GET

URL: http://127.0.0.1:8000/api/accounts/profile/

Step 2: Go to Headers tab and add:

Key	Value
Authorization	Token 6f13b2c5a86f4a8c97e6c9a7af1c45b4d14c1e62

(Use the token from registration or login.)

Step 3: Click Send

✅ Expected Response:

{
  "id": 1,
  "username": "brilliant",
  "email": "brilliant@example.com",
  "bio": null,
  "profile_picture": null,
  "followers": []
}


This confirms token-based authentication works.

⚡ Tips for Postman Testing

    Save your token in Postman variables:

    Go to the top right → Manage Environments → Add a variable authToken.

    Then in the Headers use:

    Authorization: Token {{authToken}}


    Use the same collection to run all requests sequentially.

    Check status codes:

    201 Created → registration successful

    200 OK → login/profile successful

    401 Unauthorized → missing/invalid token

🧰 Technologies Used

    Python 3.10+

    Django 5+

    Django REST Framework

    SQLite3 (default database)

📝 Posts & Comments API (Tabulated)

    Post Model Overview

| Field        | Type             | Description                                |
| ------------ | ---------------- | ------------------------------------------ |
| `author`     | ForeignKey       | User who created the post                  |
| `title`      | CharField        | Post title                                 |
| `content`    | TextField        | Post content                               |
| `created_at` | DateTime         | Auto-created timestamp                     |
| `updated_at` | DateTime         | Auto-updated timestamp                     |
| `comments`   | Reverse relation | List of comments associated with this post |


Comment Model Overview

| Field        | Type       | Description                  |
| ------------ | ---------- | ---------------------------- |
| `post`       | ForeignKey | Post this comment belongs to |
| `author`     | ForeignKey | User who created the comment |
| `content`    | TextField  | Comment content              |
| `created_at` | DateTime   | Auto-created timestamp       |
| `updated_at` | DateTime   | Auto-updated timestamp       |

    Authentication Requirement

| Requirement    | Details                                  |
| -------------- | ---------------------------------------- |
| Authentication | All endpoints require a valid token      |
| Header         | `Authorization: Token <your_token_here>` |

