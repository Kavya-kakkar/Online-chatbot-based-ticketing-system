# 🏛️ Ciphers Museum – Chatbot-Based Ticketing System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-092E20.svg?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-7952B3.svg?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Overview

**Ciphers Museum** is a comprehensive, Django-based web application designed to provide a seamless digital experience for museum visitors. The platform empowers users to explore upcoming exhibitions, discover events, and book tickets effortlessly through an integrated AI-powered chatbot system. 

Built with modern web standards, it prioritizes user convenience, secure authentication, and transparent access to essential museum information.

## 🚀 Key Features

*   **🤖 AI Chatbot Ticketing System** - Revolutionize the booking experience by allowing users to interact and book tickets conversationally.
*   **🔐 Secure User Authentication** - Robust login, registration, and logout functionalities utilizing Django's built-in authentication framework.
*   **🎨 Dynamic Exhibitions & Events Management** - Real-time displays of ongoing/upcoming museum events and captivating exhibits, managed easily via the backend.
*   **📱 Responsive & Modern UI** - A mobile-friendly layout and navigation powered by Bootstrap 5, ensuring a flawless experience across all devices.
*   **📑 Comprehensive Informational Pages** - Includes dedicated pages for About, Terms & Conditions, Privacy Policy, Career, Mission, Partnerships, FAQ, and more.
*   **🕰️ Timings & Scheduling** - Dynamic tracking of museum timings, open/close hours, and holiday schedules.
*   **🛡️ Data Security & Privacy** - Secure handling of user data with clear, transparent policy pages.

## 📁 Project Structure

The project follows a standard Django architecture with dedicated applications handling specific domains:

*   `lama/` - Core Django project settings, ASGI/WSGI configurations, and primary URL routing.
*   `onlinechatbot/` - The main application containing the models (`Exhibit`, `Event`, `Ticket`, `Staff`, `MuseumTiming`), views, and URL structures for the museum platform.
*   `accounts/` - Dedicated application managing user authentication (registration, login, logout).
*   `templates/` - Contains all HTML templates providing the frontend interface.
*   `static/` & `assets/` - Directory for serving static files such as CSS, JavaScript, and images.

## 🛠️ Technology Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
*   **Database:** SQLite (default for development)

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine.

### Prerequisites

*   Python 3.8+ installed
*   Virtual environment tool (`venv`)

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Kavya-kakkar/Online-chatbot-based-ticketing-system.git
    cd Online-chatbot-based-ticketing-system
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    *(If a `requirements.txt` is missing, you can install Django manually)*
    ```bash
    pip install django
    ```

4.  **Apply Database Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional - for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/Kavya-kakkar/Online-chatbot-based-ticketing-system/issues).

## 📄 License

This project is licensed under the MIT License.
