# Digital Badge System

A simple web app using FastAPI and Vue + Vuetify for tracking and awarding achievements.

---

## 🛠️ Setup and Run Instructions

### Backend (FastAPI)

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```
2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the backend:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend (Vue + Vuetify)

1. Navigate to the frontend folder:
    ```bash
    cd frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Run the frontend:
    ```bash
    npm run dev
    ```

---

## 🌐 System Overview

- **Backend**: FastAPI, tracks achievements and progress via REST API.
- **Frontend**: Vue 3 + Vuetify, interactive UI to navigate pages and earn achievements.
- **Store**: Pinia used for tracking earned achievements and showing popups.

---

## 📸 Screenshots
### Start Page
![Dashboard Screenshot](assets/login.png)
### Dashboard Page
![Dashboard Screenshot](assets/dashboard.png)
### Dashboard Page showing achievements
![Dashboard Screenshot](assets/achievement.png)

---

## 🚀 Feature Improvements (Ideas)

- User authentication system
- Real-time chat with WebSocket
- Admin panel to manage achievements
- Achievement badges with animations

