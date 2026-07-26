# Task Tracker API (Module 1)

A simple learning-project REST API for tracking tasks, built with Python and FastAPI.

## Current Scope

This is the initial project skeleton. It includes:

- A FastAPI application instance
- A `GET /health` endpoint for verifying the server is running
- The planned folder structure for future CRUD functionality

CRUD endpoints, task validation rules, and business logic (e.g. status transitions) are **not yet implemented** and will be added in a later step.

## Project Structure

## Steps to run task-tracker
check if you are at root folder: task-tracker

cd backend

#activate local environment
.\venv\Scripts\Activate.ps1

#start web server
uvicorn app.main:app --reload --port 8000

#check from broswer
http://localhost:8000/index.html

#run tests
python -m pytest -q tests/test_tasks.py                                     