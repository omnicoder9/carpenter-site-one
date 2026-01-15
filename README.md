# Slick Cabinets

A modern web application for a carpentry company, featuring a public portfolio and an internal admin portal.

## Tech Stack
- **Backend:** Python, FastAPI
- **Frontend:** Vue.js 3, TypeScript, Bootstrap 5
- **Database:** (Mocked) In-memory data with Pydantic models

## Project Structure
- `backend/`: FastAPI application code.
- `frontend/`: Vue.js application code.

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)

### 1. Setup Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
The API will start at `http://localhost:8000`.
API Documentation is available at `http://localhost:8000/docs`.

### 2. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```
The frontend will start at `http://localhost:5173`.

## Features
- **Service Catalog:** Browse core and specialized carpentry services.
- **Contact Form:** Send inquiries (logged to backend console).
- **Internal Portal:** Log in to view recent messages.
  - **Credentials:** username: `admin`, password: `slick2024`
