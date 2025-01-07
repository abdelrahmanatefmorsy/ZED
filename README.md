# ZED

ZED is a course platform that allows users to easily create and publish their own courses, as well as join available courses on the platform. 

ZED aims to create a collaborative learning environment that facilitates knowledge sharing and skill development.

## Table of Contents
- [Features](#Features)
- [Installation](#installation)
- [Usage](#Usage)
- [Technologies Used](#technologies-used)
- [Future Features](#Future-Features)
- [Screenshots](#screenshots)
- [Contributors](#Contributors)


## Features

- **Create and publish courses**: Users can create and publish their own courses by adding content such as lessons, texts, and quizzes.
- **Join courses**: Users can browse and join courses that are available to them based on their interests.
- **User profile**: Each user has a personal profile where they can view and manage the courses they have created or joined.
- **Course search**: Users can search for specific courses based on topics or keywords to easily find what they're looking for.
- **Edit courses**: Users can edit the courses they've created, including modifying the content and videos.
- **Video access**: Users can only access the course videos after they apply for the course, ensuring they are officially enrolled.
- **Course status**: When creating a course, users can choose whether the course is **Active** or **Inactive**. Active courses are visible to everyone, while inactive ones are hidden from public view.
- **Edit course videos**: The course creator can edit and manage the videos within the course at any time.
- **Control video visibility**: Course creators can control which videos are visible to users at any given time, allowing some videos to be hidden or shown based on the course's progress.

## Installation

Follow these steps to set up the project on your local machine:

#### 1. Install Python
Ensure that Python is installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

#### 2. Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/abdelrahmanatefmorsy/ZED
```
#### 3 . Create the enviroment

```bash
python -m venv env
```
#### 4. Activate the virtual environment
Clone the repository to your local machine using Git:

 - On Windows
 
   ```bash
   venv\bin\activate
   ```
- On macOS/Linux

   ```bash
   source venv/bin/activate
   ```

#### 5. Install Dependencies

```bash
pip install -r requirements.txt
```
#### 6. Change Directory To manage.py 
```bash
cd .\src\env\ZED\ 
```
#### 7. Configure the Database

```bash
python manage.py migrate
```

#### 8. Run The server

```bash
python manage.py runserver
```
#### 9. You can access The website at 
```
http://127.0.0.1:8000
```

## Usage

1. **Home Page**:
   - Upon visiting the website, you'll land on the **Home Page** where you can view all available courses.
   - You can browse courses without having an account, but you must sign up to apply for or join any course.

2. **Sign Up**:
   - To create an account, click on the **Sign Up** button located in the **Navbar**.
   - Fill in the necessary details to create your account.
   - Once signed up, you'll be able to apply for courses and create your own.

3. **Create a Course**:
   - After logging in, go to your **Profile** or the **Courses** page.
   - Click the **Add Course** button.
   - Fill in the course details such as:
     - **Course Name**
     - **Description**
     - **Course Type** (Active or Inactive)
   - Once completed, the course will appear in your profile, and you can modify it later.

4. **Edit or Manage Your Course**:
   - To edit or manage your course, go to your profile and click on **View Details** for the specific course.
   - From the **View Details** page, you can:
     - **Update Course**: Edit the course details like the name, description, and status (Active/Inactive).
     - **Delete Course**: If you wish to remove the course, click the **Delete Course** button.

5. **Add Videos to Your Course**:
   - To add a video to your course, go to the **View Details** page of the course you want to add videos to.
   - From there, you can click on the **Add Video** button.
   - You will need to provide:
     - **Video Title**
     - **Description**
     - The **Video File**
     - **Video Status** (Active or Inactive)
   - The video will then be added to your course, and you can:
     - **Edit the video**: You can update the video title, description, file, or status by clicking on the **Edit Video** button.
     - **Delete the video**: If you no longer want a video, you can delete it by clicking the **Delete Video** button.

6. **Join a Course**:
   - To join a course, visit the **Courses** page, where you can search or browse for courses.
   - Alternatively, you can go to publisher profile, select a course from his published courses. 
   - Click on the **View Details** button for the course you're interested in.
   - Click the **Apply** button to enroll in the course.
   - The course will be added to your profile, and you can access it from there.

7. **Access Course Videos**:
   - Once you've joined a course, go to your **Profile** and select the course from your list of joined courses.
   - Click on **Go** to start viewing the videos for that course.
   - You can watch the course videos if the course is **Active** and you have enrolled.

## Technologies Used

This project is built using the following technologies:

- **HTML**: For creating the structure of the website.
- **CSS**: For styling and making the website responsive.
- **JavaScript**: For dynamic behavior and client-side interactivity.
- **Python**: For backend logic and server-side programming.
- **Django Framework**: For building the backend with Python, handling database operations, and managing the overall structure of the web application.

## Future Features

- **Rating and Reviews**: Allow users to rate and leave reviews on courses to help others make informed decisions.
- **Course Certification**: Provide certificates for users who complete a course successfully.
- **User Messaging**: Add a messaging system for users to interact with instructors or fellow students.
- **Instructor Dashboard**: Add a dashboard for course Publisher to manage their courses, Users, and video content more efficiently.


## Contributors

- **Abdelrahman Atef** – Backend Development
- **Mohamed Adel** – Frontend Development
