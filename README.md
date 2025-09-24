# TO DO LIST WITH USER AUTHENTICATION #

his project is a web-based To-Do List application that allows users to manage their daily tasks efficiently. Each user can create an account, securely log in, and maintain a personalized list of tasks. The application supports basic task operations such as adding new tasks, marking tasks as completed, updating, and deleting them. All task data is securely stored in a PostgreSQL database and linked to the respective user, ensuring privacy and data integrity. The project demonstrates key concepts of full-stack development, including user authentication, CRUD operations, and relational database management, making it an ideal beginner-friendly project to learn Python, web technologies, and database integration.

# FEATURES
Features

**User Registration**:Users can create an account by signing up with a username, email, and password.

**User Login and Logout**:Registered users can securely log in and log out of their accounts.

**Secure Password Storage**:Passwords are stored securely using hashing techniques to protect user data.

**Personalized To-Do List**:Each user has their own private to-do list, inaccessible to other users.

**Add Tasks**:Users can add new tasks with descriptions to their list.

**View Tasks**:Users can view all their current tasks.

**Update Tasks**:Users can mark tasks as completed or pending.

**Delete Tasks**:Users can remove tasks from their list.

**Timestamps**:Each task records creation and last update times.

**User Session Management**:Maintains user login sessions securely until logout.

## PROJECT STRUCTURE
TODOLISTWITHUSERAUTHENTICATION/
|
|---src/           #core application logic
|   |---logic.py   #bussiness logic and task
operations
|   |__db.py       # database operations
|
|---api/            # backend api
|   |__main.py      # fastapi endpoints
|
|---frontend/       # frontend application
|   |__app.py       # streamlit web interface
|
|___requirements.txt #python Dependencies
|
|___README.md   #project documentation
|
|___.env    #python variables

## quick start

### prerequisites

-python 3.8 or higher
-a supabase account
-Git(Push,cloning)

### 1.clone or download the project
# option 1:clone with git
git clone <repository-url>
# option 2: Download and extract the ZIP file

### 2.Install Dependencies
pip install -r requirements.txt

### 3. Set Up Supabase Database
1.Create a Supabase Project:
2.Create the Tasks Table:

Go to the SQL Editor in your Supabase dashboard
Run this SQL command:

--- sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    description TEXT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
---
3.** Get Your Credentials:
### 4. configure Environment variables
1.create a `.env` file in the project root
2.Add your Supabase credentials to `.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**example:**
SUPABASE_URL="https://rburcvpocmiedtiqnfrp.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJidXJjdnBvY21pZWR0aXFuZnJwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIyMTgsImV4cCI6MjA3MzY1ODIxOH0.BKFNOZnRNUnoEFHcNS0i09Mr-YYShn71HbBxUYSKuGM"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py
The app will open in your browser at `http://localhost:8501`

## FastAPI Backend
cd api
python main.py

The API will be available at `http://localhost:8000`

## How to Use

## Technical Details

### Technologies Used
-**Frontend**: Streamlit (python web framework)
-**Backend**: FastAPI (python REST APPI framework)
-**Database**: Supabase(PostgreSQL-based backend-as-a-service)
-**Language**: Python 3.8+

### key Components

1. ** `src/db.py`**: Database operations-Handles all CRUD operations with Supabase

2.**`src/logic.py`**:Business logic -Task validation and processing

## Troubleshooting

## Common Issues

1. **"Module not found"errors**
-Make sure you've installed all dependencies:`pip install -r requirements.txt`
-check that you're running commands from the correct directory

## Future Enhancements

ideas for extending this project:
**user authentication**:Add user accounts and login
-**Task Categories**:Organize tasks by subject or category
-**Notifications**:Email or push notifications for due dates
-**collaborations**: Share tasks with classmates
-**Mobile App**:React Native or Flutter mobile version
-**Data Export**:Export tasks to CSV or PDF 
-**Task Templates**: Create resusable task templates

## Support
If you encounter any issues or have questions:
mailid: manthrisulakshana66@gmail.com
phonenumber:8341746201

