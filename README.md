# UDo - Project & Task Management Dashboard

## 📌 Project Overview
UDo is a simple project and task management dashboard designed to help freelancers and teams organize their projects efficiently. The platform enables project owners to manage tasks, assign members, track progress, and communicate effectively.

## 🚀 Features
- User authentication & profile management
- Create, update, and delete projects
- Task assignment and status tracking
- Role-based access control (Admin, Member)
- Request and manage connections between users
- REST API for integration with mobile and other platforms

## 🛠️ Technologies Used
- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: Tailwindcss  / daisyUI 
- **Database**: MongoDB / SQLite (for development)
- **Authentication**: Django’s built-in authentication

## FAQ

#### what is u-do ?

U-DO is a project and task management platform designed to help teams, freelancers, and developers organize their workflow, track progress, and collaborate efficiently.

#### how i do create new project ?

To create a new project, go to your dashboard, click on the "Create Project" button, fill in the required details, and submit the form. Your project will be added instantly.

#### Can I add team members to my project?

Yes! You can invite team members by entering their user ID in the project settings. They will receive a request to join your project and can accept it from their dashboard.

#### Is u-do free to use?

Yes, U-DO offers a free version with essential features. We also provide premium plans with advanced capabilities for larger teams and businesses.

## Authors

- [@Hirmaan rashidi](https://github.com/HirmanX)

## Project Structure

```
db.sqlite3
package.json
tailwind.config.js
.idea/
    .gitignore
    dataSources.xml
    djsource.iml
    misc.xml
    modules.xml
    inspectionProfiles/
        profiles_settings.xml
udo/
    db.sqlite3
    manage.py
    account/
        __init__.py
        admin.py
        apps.py
        customTag.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
        __pycache__/
        migrations/
        templates/
    api/
        __init__.py
        admin.py
        apps.py
        models.py
        serializers.py
        tests.py
        urls.py
        ...
    dashbord/
    home/
    static/
    templates/
    udo/
    uploads/
```

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Node.js
- npm
- MongoDB

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/HirmanX/u-do.git 
    cd .\u-do\ 
    ```
2. set up Virtual Environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Create Superuser (Admin Access):

    ```sh
    python manage.py createsuperuser
    ```

4. Install Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```sh
    python manage.py migrate
    ```

### Running the Project

1. Start the Django development server:

    ```sh
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

- `account/`: Contains the account-related Django apps.
  - [`views.py`](udo/account/views.py): Contains views for account management.
  - [`models.py`](udo/account/models.py): Contains models for user and friendship.
- `api/`: Contains the API-related Django apps.
- `dashbord/`: Contains the dashboard-related files.
  - [`urls.py`](udo/dashbord/urls.py): Contains URL patterns for the dashboard.
  - [`models.py`](udo/dashbord/models.py): Contains models for projects and tasks.
  - [`views.py`](udo/dashbord/views.py): Contains views for managing projects and tasks.
- `home/`: Contains the home-related files.
- `static/`: Contains static files.
- `templates/`: Contains HTML templates.
  - [`email.html`](udo/templates/email.html): Template for email content.
  - [`base.html`](udo/templates/base.html): Base template for the project.
- `udo/`: Contains the main Django project settings and URLs.
- `uploads/`: Contains uploaded files.
