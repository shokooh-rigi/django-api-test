# Django Estimation App

This project is a comprehensive estimation application built with Django, featuring three main apps: **Estimates**, **Management**, and **User**. The application provides a user-friendly interface for managing estimates and includes authentication, testing, and API documentation.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Setup](#project-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Introduction

The Django Estimation App is designed to assist users in managing estimates effectively. It includes functionalities for creating, updating, and deleting estimates, along with user authentication to ensure secure access.

## Features
- **User Authentication**: Secure access with Django’s authentication system. Only superusers can create, update, or delete estimates.
- **Estimate Management**: Manage estimates easily through dedicated APIs.
- **API Documentation**: Swagger UI for easy reference of available API endpoints.
- **Token Authentication**: Use token-based authentication for accessing protected resources.
- **Testing**: Comprehensive unit tests for all critical operations.

## Project Setup

To set up the project on your local machine, follow these steps:  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/shokooh-rigi/django-api-test.git  
   cd django-api-test  

Install Dependencies: Ensure you have Python 3.8 or higher installed. Then install the required packages:

      pip install -r requirements.txt  

Create Database Migrations: Create the necessary database migrations by running:

      python manage.py makemigrations  

Apply Migrations: Apply the migrations to set up the database schema:

      python manage.py migrate  

Run the Development Server: Start the development server with:

    python manage.py runserver  

    You can access the application at http://127.0.0.1:8000/.

###Usage
###Apps Overview:

 ####Estimates: 
Handle all operations related to estimates (Create, Update, Delete).
 ####Management:
Manage user-related functionalities and administrative tasks.
 ####User:
Manage user accounts and authentication.

###API Endpoints

Here are the available API endpoints for the application:
Estimates

 Create Estimate:   POST /api/estimates/
 Retrieve Estimates:   GET /api/estimates/
 Update Estimate:   PUT /api/estimates/{id}/
 Delete Estimate:   DELETE /api/estimates/{id}/

###Management

Manage Users:
Endpoints to create, update, or delete users. Ensure only superusers can access these.

###User

 User Registration:
 POST /api/users/register/
 User Login: POST /api/users/login/ - Returns a token for authentication.

Make sure to include the necessary authentication headers (Bearer Token) when accessing protected endpoints.
###Testing

To ensure the application is functioning as expected, you can run the unit tests included in the project:

      python manage.py test  

This will run tests for all apps, including the Estimates, Management, and User apps.
API Documentation

###The API is documented using:
Swagger UI, which allows you to explore and interact with the available endpoints. You can access the documentation at: 
http://127.0.0.1:8000/swagger/