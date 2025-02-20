# DreVa- Dream Vault Dashboard

## Project Overview

Dream Vault is a personal dashboard designed to help users keep track of their goals, dreams, and significant life events. The platform allows users to record, manage, and reflect on their personal and professional progress, dream interpretations, and milestones in life. With an easy-to-use interface, users can monitor their journey, unlock new events, and achieve their aspirations in a meaningful way.

This dashboard serves as a vault for your personal data, organizing your dreams, goals, and events to foster reflection and growth.

## Image Gallery

<div style="display: flex; justify-content: space-between;">
    <img src="path_to_image/image1.png" alt="Image 1" width="200" />
    <img src="path_to_image/image2.png" alt="Image 2" width="200" />
    <img src="path_to_image/image3.png" alt="Image 3" width="200" />
</div>

*Figures: Sample Images of the Project.*

## Features

### 1. **Goals Tracker**
   - **Manage Personal & Professional Goals**: Users can add, view, and track their progress toward goals.
   - **Progress Monitoring**: See the percentage of progress made towards each goal.
   - **Actionable Insights**: Easily understand which goals need more attention and which ones are on track.

### 2. **Dream Log**
   - **Record Dreams**: Add your dreams and track their details like date and interpretation.
   - **Dream Interpretation**: Interpret your dreams and reflect on their meanings over time.
   - **Growth Over Time**: Track how your understanding of your dreams evolves.

### 3. **Event Capsule**
   - **Significant Life Events**: Log major life events and milestones.
   - **Event Unlocking**: Mark events as unlocked when they happen.
   - **Milestones Tracking**: Keep a personal record of key moments in life.

## Setup

To get started with this project locally, follow the steps below:

### Prerequisites
- Python 3.x installed
- Django framework
- Basic knowledge of Python, Django, and web development
- Text editor or IDE (e.g., VSCode, PyCharm)

### 1. Clone the repository:
   ```bash
   git clone https://github.com/RJ-Hossan/DreVa.git
   cd Dreva
   ```

### 2. Install dependencies:
   Create a virtual environment and install the required dependencies.

   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/MacOS
   env\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

### 3. Setup Django Database:
   - Run migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

### 4. Run the server:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

   Now, open your browser and visit `http://127.0.0.1:8000/` to see the Dream Vault Dashboard in action.

## Usage

Once the project is up and running, users can log in and access the following features:

### Goals:
   - Track the progress of personal and professional goals.
   - Add new goals and monitor progress through percentage completion.
   - Edit and delete goals as needed.

### Dreams:
   - Record your dreams and add their interpretations.
   - View previously recorded dreams with dates and interpretations.
   - Add new dreams with detailed descriptions and interpretations.

### Events:
   - Create and view events that mark important milestones in life.
   - Unlock events as they happen.
   - Track event details including the name, date, and unlock status.

## Folder Structure

- `vault/` - Main app folder for the Dream Vault Dashboard.
  - `templates/` - Contains HTML templates for rendering views.
  - `static/` - Contains static files like CSS and images for styling.
  - `models.py` - Defines the database models for Goals, Dreams, and Events.
  - `views.py` - Contains the logic for rendering views and handling requests.
  - `urls.py` - Maps URLs to specific views for easy navigation.

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS (using static files)
- **Database**: SQLite (used in development)
- **Version Control**: Git/GitHub

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch to work on your feature/fix (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request to merge your changes back into the main repository.


## Acknowledgments

- The design and inspiration for the Dream Vault Dashboard were conceptualized with simplicity and reflection in mind.
- Special thanks to Django and other open-source contributors who make building web applications easy and accessible.
