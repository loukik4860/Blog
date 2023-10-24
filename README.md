# Blog
DRF JWT LOGIN + Registration + Login + changePassword + reset password + reset password by Email

# Django Blog Project 
This README provides an overview of the Django Blog Project, including its structure, components, and key functionalities.




   ##Project Overview

This Django project is a simple blog application with user registration,
login, user profile management, and password reset functionality. 
It is built using Django 4.2.6 and the Django Rest Framework.

## Project Structure
The project structure follows typical Django conventions. Key directories and files include:

* **BlogProject/**: The main project directory.
* **AuthApp/** : The main app directory, containing the blog application.
* **settings.py** : Django project settings.
* **models.py** : Database models for user accounts.
* **admin.py** : Admin configurations for the user model.
* **serializers.py** : Serializers for user data.
* **views.py** : API views for user registration, login, profile, and password reset.
* **urls.py** : URL configurations for the blog application.
* **utils.py** : Utility functions for sending email.
* **renderers.py** : Custom renderer for API responses.

## Key Components

### Settings
**SECRET_KEY:** Django secret key for security.

**INSTALLED_APPS:** Installed Django apps, including rest_framework and corsheaders.

**AUTH_USER_MODEL:** Custom user model AuthorUser.
Email configuration for sending password reset emails.


### Models
* **AuthorUser:** Custom user model derived from AbstractBaseUser with additional fields.
* **AuthorUserManager:** Custom user manager for user model creation.

* Database fields include email, first name, last name, and various boolean flags for user attributes.

### Admin
* AuthorUserAdmin: Admin configuration for the custom user model.

### Serializers
* **AuthorUserRegistrationSerializer:** Serializer for user registration.

* **AuthorLoginSerializer:** Serializer for user login.

* **AuthorProfileSerializer:** Serializer for user profile data.
* **AuthorChangePasswordSerializer:** Serializer for changing the user's password.
* **AuthorPasswordEmailResetSerializer:** Serializer for sending a password reset email.
* **UserPasswordResetSerializer:** Serializer for resetting the user's password.

### Views
* API views for user registration, login, profile, password change, password reset email, and password reset.

### URLs
* URL routing for various API endpoints, including user registration, login, profile, and password reset.

### Utils

* Utils: Utility class for sending emails.
### Renderers
**UserRenderers:** Custom JSON renderer for API responses.

### Functionality
The Django Blog Project provides the following key functionality:

1. **User Registration:** Users can register by providing their first name, last name, email, and password.
2. **User Login:** Registered users can log in using their email and password.
3. **User Profile:** Users can view their profile information.
4. **Password Change:** Users can change their password.
5. **Password Reset**: Users can request a password reset email and reset their password.

### Installation
1. Install Python and Django on your system.
2. Create a virtual environment for the project.
3. Clone the project repository.
4. Install project dependencies using **pip install -r requirements.txt.**
5. Configure database settings in the **settings.py** file if needed.
6. Run database migrations using **python manage.py migrate.**
7. Start the development server with **python manage.py runserver.**

## Usage
1. Register a user by making a POST request to **/register/** with first name, last name, email, and password.
2. Log in with the registered user credentials by making a POST request to **/login/**.
3. View the user's profile by making a GET request to **/profile/**.
4. Change the user's password by making a POST request to **/changePassword/**.
5. Request a password reset email by making a POST request to **/password_reset_email/**.
6. Reset the password by making a POST request to **/password_reset/<uid>/<token>/** with the new password and confirmation.


This Django Blog Project is a foundation for building a blog application with user authentication and password management. 
Additional features and customization can be added as needed.