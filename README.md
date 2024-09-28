# Stream Platform (RESTful API)

## Overview

The **Stream Platform** is a RESTful API-based project where users can browse, stream shows, and submit reviews. Built using Django Rest Framework (DRF), this project provides secure authentication and user authorization using JWT (JSON Web Tokens). The API structure allows for seamless integration with front-end applications or mobile apps, making it an ideal backend service for streaming platforms.

## Technologies Used

- **Python**: Backend development and core programming language.
- **Django Rest Framework (DRF)**: For building a powerful and scalable REST API.
- **REST API**: Ensuring smooth client-server communication for data exchange.
- **JWT Authentication**: Secure authentication and user authorization system using JSON Web Tokens.
- **SQLite**: A lightweight database to manage data like users, shows, and reviews.

## Features

- **User Authentication**: 
  - JWT-based secure login and registration system.
  - Token-based authorization to access protected resources.

- **Stream Shows**:
  - Users can browse available shows.
  - Show details including title, description, release date, and streaming status.

- **Submit Reviews**:
  - Authenticated users can submit reviews for shows.
  - Users can view all reviews associated with a particular show.
  
- **API Endpoints**:
  - List of shows, show details, and reviews.
  - User registration, login, and JWT token generation.
  - CRUD operations for reviews (Create, Read, Update, Delete) by authorized users.


## API Endpoints

- **Authentication**:
  - `POST /api/token/`: Obtain JWT access token.
  - `POST /api/token/refresh/`: Refresh JWT access token.
  
- **Shows**:
  - `GET /api/shows/`: List all available shows.
  - `GET /api/shows/<id>/`: Retrieve details of a specific show.

- **Reviews**:
  - `GET /api/shows/<id>/reviews/`: Get reviews for a specific show.
  - `POST /api/shows/<id>/reviews/`: Submit a new review (JWT authentication required).
  - `PUT /api/reviews/<id>/`: Update a review (JWT authentication required).
  - `DELETE /api/reviews/<id>/`: Delete a review (JWT authentication required).

## How to Run This Project Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/talhabinalam/Stream-Platform--RESTful-API.git
