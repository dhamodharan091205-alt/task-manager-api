# Task Manager API 🚀
Backend API built with FastAPI + JWT Authentication

## What I Built
- User Register / Login with JWT Token
- Create, Read, Update, Delete Tasks
- Protected Routes - each user sees only own tasks

## Tech Stack
FastAPI, SQLAlchemy, SQLite, Python-Jose

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload
Open: http://127.0.0.1:8000/docs

## API Endpoints
POST /auth/register
POST /auth/login
GET /auth/me
POST /tasks
GET /tasks
DELETE /tasks/{id}

Built by Dhamodharan
