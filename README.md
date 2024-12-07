# Stream Platform (RESTful API)

## Overview

The **IMDB Clone** is a RESTful API-based project where users can browse streaming platforms, manage their watchlist, and submit reviews. Built using Django Rest Framework (DRF), this project provides secure authentication and user authorization using JWT (JSON Web Tokens). The API is designed for seamless integration with front-end applications or mobile apps, making it an ideal backend for streaming services.

---

## Technologies Used

- **Python**: Backend development and core programming language.
- **Django Rest Framework (DRF)**: For building a scalable and efficient REST API.
- **REST API**: For client-server communication and data exchange.
- **JWT Authentication**: Secure user authentication and authorization using JSON Web Tokens.
- **SQLite**: A lightweight database to store user, watchlist, and review data.

---

## Features

- **JWT Authentication**:
  - Secure login and registration.
  - Token-based access for protected resources.
  
- **Watchlist Management**:
  - View and manage a personalized watchlist of shows.

- **Stream Platforms**:
  - Explore a list of streaming platforms.
  - Get detailed information on specific platforms.

- **Reviews**:
  - Authenticated users can create, view, update, or delete reviews.
  - View reviews associated with specific streaming platforms.

- **User Reviews**:
  - Get a list of all reviews submitted by a specific user.
 
- **Pagination**:
  - Implemented django restful pagination for api.

---

## API Endpoints

### Watchlist

- **View Watchlist**:
  - `GET /api/watchlist/`  
  - Fetch all watchlist items.

- **Global Watchlist**:
  - `GET /api/watch-list/`  
  - View all watchlists globally.

- **Watchlist Details**:
  - `GET /api/watchlist/<int:pk>/`  
  - Retrieve details of a specific watchlist item.

### Stream Platforms

- **View Platforms**:
  - `GET /api/stream/`  
  - Fetch all streaming platforms.

- **Platform Details**:
  - `GET /api/stream/<int:pk>/`  
  - Retrieve details of a specific platform.

### Reviews

- **List Reviews for a Platform**:
  - `GET /api/stream/<int:pk>/review/`  
  - Retrieve all reviews for a specific platform.

- **Create a Review**:
  - `POST /api/stream/<int:pk>/review-create/`  
  - Submit a new review for a specific platform (JWT authentication required).

- **Review Details**:
  - `GET /api/stream/review/<int:pk>/`  
  - Retrieve details of a specific review.

- **User Reviews**:
  - `GET /api/reviews/`  
  - Fetch all reviews created by the authenticated user.

---

## How to Run This Project Locally

### Prerequisites
- Python 3.x installed
- pip (Python package installer)
- A virtual environment (recommended)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/talhabinalam/imdb-clone-rest-api.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd clone-rest-api
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
7. **Access the API**: Open your browser and navigate to http://127.0.0.1:8000/api/

## Future Enhancements:
- Implement user-specific watchlist filtering.
- Support OAuth2 authentication.
