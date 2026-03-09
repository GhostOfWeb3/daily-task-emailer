# Daily-task-emailer

The Daily-task-emailer is a straightforward Python script designed to help users stay on top of their daily responsibilities by sending automated email reminders for tasks. By simply listing your daily tasks in a text file, this tool ensures you receive a convenient summary directly in your inbox, helping to improve productivity and task management.

## Features

*   **Automated Email Reminders**: Delivers your task list directly to your specified email address.
*   **Configurable Task List**: Easily define your daily tasks by editing a plain text file (`tasks.txt`).
*   **Simple Setup**: Quick and easy to get running with minimal configuration.
*   **Cross-platform Compatibility**: Runs on any system with Python installed.

## Tech Stack

*   **Python**: The core language used for scripting the email functionality and task processing.
*   **Standard Python Libraries**: Utilizes built-in modules for email handling (e.g., `smtplib`, `email.mime.text`).

## Project Structure

The project is organized into a few key files:

```
Daily-task-emailer/
├── .gitignore
├── main.py
├── requirements.txt
└── tasks.txt
```

*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `main.py`: The primary script responsible for reading tasks, formatting the email, and sending it via an SMTP server.
*   `requirements.txt`: Lists the Python dependencies required to run the project.
*   `tasks.txt`: A plain text file where you list all your daily tasks, one task per line.

## Installation Instructions

Follow these steps to set up the Daily-task-emailer on your local machine:

### Prerequisites

*   Python 3.x installed on your system.

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Daily-task-emailer.git
    cd Daily-task-emailer
    ```
    (Replace `https://github.com/yourusername/Daily-task-emailer.git` with the actual repository URL if different.)

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Email Settings**:
    Open `main.py` in a text editor. You will need to configure the following variables with your email provider's SMTP details and your email credentials:

    ```python
    # Email configuration
    SENDER_EMAIL = "your_sender_email@example.com"
    SENDER_PASSWORD = "your_email_password" # Consider using environment variables for security
    RECEIVER_EMAIL = "recipient_email@example.com"
    SMTP_SERVER = "smtp.example.com" # e.g., 'smtp.gmail.com' for Gmail
    SMTP_PORT = 587 # or 465 for SSL, 587 for TLS
    ```
    *   Replace `your_sender_email@example.com` with the email address that will send the reminders.
    *   Replace `your_email_password` with the password for the sender email account. **For better security, it is highly recommended to use environment variables for sensitive information like passwords instead of hardcoding them directly in the script.**
    *   Replace `recipient_email@example.com` with the email address where you want to receive the reminders.
    *   Update `smtp.example.com` and `SMTP_PORT` with the correct SMTP server and port for your email provider.

    **Note on Gmail users**: If you are using Gmail, you might need to generate an "App password" instead of using your regular Gmail password, especially if you have 2-Factor Authentication enabled. Google often blocks less secure apps by default. Refer to Google's documentation on App Passwords for more details.

## Usage Instructions

### 1. Define Your Tasks

Open the `tasks.txt` file. List each of your daily tasks on a new line. For example:

```
Buy groceries
Call client X for meeting confirmation
Prepare presentation for morning standup
Review pull request #123
Plan tomorrow's schedule
```

### 2. Run the Script Manually

To test the script and send an email reminder immediately:

```bash
python main.py
```

If successful, you should receive an email in your `RECEIVER_EMAIL` inbox containing the tasks listed in `tasks.txt`.

### 3. Schedule Daily Execution

To automate the daily sending of task reminders, you can schedule the script to run once a day using system utilities:

#### On Linux/macOS (using Cron)

1.  Open your crontab for editing:
    ```bash
    crontab -e
    ```
2.  Add a new line to schedule the script. For example, to run the script every day at 8:00 AM:
    ```cron
    0 8 * * * /usr/bin/python3 /path/to/Daily-task-emailer/main.py >> /path/to/Daily-task-emailer/cron.log 2>&1
    ```
    *   Replace `/usr/bin/python3` with the absolute path to your Python 3 interpreter (you can find this using `which python3`).
    *   Replace `/path/to/Daily-task-emailer/` with the absolute path to your project directory.
    *   The `>> /path/to/Daily-task-emailer/cron.log 2>&1` part is optional but highly recommended for logging output and errors for debugging.

#### On Windows (using Task Scheduler)

1.  Open "Task Scheduler" (search for it in the Start Menu).
2.  Click "Create Basic Task..." on the right panel.
3.  Follow the wizard:
    *   **Name**: `Daily Task Emailer`
    *   **Trigger**: `Daily`, set your desired time (e.g., 8:00 AM).
    *   **Action**: `Start a program`
    *   **Program/script**: Enter the path to your Python executable (e.g., `C:\Python39\python.exe`).
    *   **Add arguments (optional)**: `main.py`
    *   **Start in (optional)**: Enter the path to your `Daily-task-emailer` project directory (e.g., `C:\Users\YourUser\Documents\Daily-task-emailer`).
4.  Finish the wizard.

## License Information

This project is licensed under the MIT License. See the LICENSE file (not provided but generally expected in open-source projects) for details.