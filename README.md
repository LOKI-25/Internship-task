# Internship-task

# Django Blog Project

This is a Django-based blog project with user authentication and APIs for managing blog posts and comments.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)


## Features

1. User authentication using JWT (JSON Web Tokens).
2. Creation, listing, and updating of blog posts by authenticated users.
3. Creation and listing of comments on blog posts by authenticated users.
4. Listing of all blog posts and their comments for public access.
5. Restriction of blog post updates to their respective authors.

## Requirements

- Python 3.x
- Django
- Django REST framework
- PyJWT (for JWT token generation)
- Other dependencies mentioned in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
      git clone https://github.com/LOKI-25/Internship-task.git
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver


# Usage

1. Access the Django admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

2. Use the provided APIs as described in the **API Endpoints** section.

## API Endpoints

### User Authentication

- `POST /users/login/`: Obtain a JWT token by providing username and password.
- `POST /users/register/`: Register by giving username and password.
- `POST /users/logout/`: Logout.

### Blog Posts

- `GET /blog/`: List all blog posts.
- `POST /blog/create`: Create a new blog post (requires authentication).
- `PUT /blog/create/<blog_id>/`: Update a blog post (requires author's authentication).

### Comments

- `GET /blog/<blog_id>/comments/`: List comments on a blog post.
- `POST /blog/create/<blog_id>/comments/`: Create a comment on a blog post (requires authentication).



   
