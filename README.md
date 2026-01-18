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
python3 main.py
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

## Deployment

### Prerequisites
- A GitHub account and repository set up for the project.
- Node.js installed (for building the frontend).
- Optionally, the gh-pages package for deployment: `npm install -g gh-pages`.

### Build Steps
1. Build the frontend for production:
   ```bash
   cd frontend
   npm install
   npm run build
   ```
   This creates a `dist/` directory with the production-ready files.

### Deployment Commands
1. Deploy the frontend to GitHub Pages:
   ```bash
   gh-pages -d frontend/dist
   ```
   This command pushes the contents of the `dist` folder to the `gh-pages` branch of your GitHub repository, making it available at `https://<username>.github.io/<repository-name>`.

   Note: Ensure your repository settings have GitHub Pages enabled for the `gh-pages` branch.

   For automated deployments, consider setting up GitHub Actions to build and deploy on pushes to the main branch.

### Backend Limitations and Deployment
GitHub Pages only serves static files and does not support running Python servers like the FastAPI backend. Therefore, the backend must be deployed separately to a platform that supports Python applications.

Recommended deployment options:
- **Vercel:** Use the Vercel CLI to deploy the backend as serverless functions. Follow Vercel's documentation for Python deployments.
- **Netlify Functions:** Deploy Python functions using Netlify. Note that Netlify primarily supports Node.js, but Python functions are available.
- **Cloud Hosts:** Platforms like Heroku, AWS Lambda, Google Cloud Functions, or DigitalOcean App Platform for full server deployment.

### Setting the VITE_API_BASE Environment Variable
The frontend uses the `VITE_API_BASE` environment variable to point to the backend API.

Before building the frontend, set this variable to the URL of your deployed backend:
```bash
export VITE_API_BASE=https://your-backend-url.vercel.app
```
Then run the build command. In production, ensure the frontend is configured to use the correct API base URL.
