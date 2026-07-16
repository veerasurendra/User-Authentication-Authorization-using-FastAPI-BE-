# 🚀 Task Manager Backend

<p align="center">
<img src="images/banner.png" width="100%">
</p>

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-green?logo=fastapi)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📖 Overview
Secure FastAPI backend with JWT authentication and user-scoped task management.

## ✨ Features
- JWT Login/Signup
- Refresh Tokens
- Logout Blacklist
- CRUD Tasks
- Swagger Docs
- Docker Ready

## 🏗 Architecture
```text
React → Axios → FastAPI → SQLAlchemy → SQLite/MySQL
```

## 📂 Project Structure
```text
backend/
├── app/
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🚀 Installation
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📡 API Examples
### Signup
```http
POST /auth/signup
```
```json
{"full_name":"John Doe","email":"john@example.com","password":"Password123"}
```

### Login
```http
POST /auth/login
```

## 📸 Screenshots
![Swagger](images/swagger.png)

## 🐳 Docker
```bash
docker compose up --build
```

## 🚀 Deployment
- Render
- Railway
- Azure
- AWS

## 👨‍💻 Author
Veera Surendra
