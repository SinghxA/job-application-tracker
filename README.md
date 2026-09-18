# JobTrack – Job Application Tracker

JobTrack is a Django-based web application that helps users manage and track their job applications in one place.

## Features

* User Signup and Login
* User Logout
* Add Job Applications
* Edit Job Applications
* Delete Job Applications
* Track Application Status
* User-specific Job Applications
* Dashboard with Application Statistics
* Bar Chart for Application Status
* Delete Account

## Tech Stack

* Python
* Django
* HTML
* CSS
* JavaScript
* SQLite
* Chart.js

## Application Status

JobTrack allows users to track applications using the following statuses:

* Applied
* Interview
* Offer
* Rejected

## How It Works

1. User creates an account.
2. User logs into JobTrack.
3. User adds their job applications.
4. Applications are stored in the database.
5. User can edit or delete applications.
6. Dashboard displays application statistics based on their application data.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/SinghxA/job-application-tracker-python.git
```

### 2. Open the Project Folder

```bash
cd job-application-tracker-python
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Then open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Future Improvements

* Search and filter job applications
* Email reminders for interviews
* Improved analytics
* Deployment
* Additional dashboard features

## Author

**SinghXA**

Built as a B.Tech Computer Science project using Python and Django.
