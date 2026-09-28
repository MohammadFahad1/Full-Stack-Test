# Full Stack Interview: Starter Project

Please set this up **before** your interview. The task itself will be shared when the interview starts.

## Requirements

- **Node.js 22.12 or newer** (for the React frontend). Check with `node --version`.
- Git
- Your chosen backend language:
  - **Node.js:** same Node version as above
  - **Python:** Python 3.10 or newer
  - **PHP:** PHP 8.1 or newer

## Project Structure

```
client/          React app (same for everyone)
server-node/     Express starter
server-python/   FastAPI starter
server-php/      Plain PHP starter
```

Use only the server folder for your language. You can delete the other two.

The React app forwards every `/api` request to `http://localhost:3001`, so your backend **must run on port 3001**. You do not need to set up CORS.

## Setup

1. Click **Use this template** at the top of this page and create a **private** repository under your own GitHub account.
2. Clone your new repository.
3. Start the frontend in one terminal:

```bash
cd client
npm install
npm run dev
```

4. Start your backend in a second terminal:

**Node.js**
```bash
cd server-node
npm install
npm run dev
```

**Python**
```bash
cd server-python
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 3001
```

On macOS or Linux, use `python3` instead of `python` if needed.

**PHP**
```bash
cd server-php
php -S localhost:3001 index.php
```

5. Open these in your browser:
   - `http://localhost:5173` shows "Start here"
   - `http://localhost:5173/api/health` shows `{"ok":true}`

## Before the interview

Send the interviewer:

1. A screenshot of the `/api/health` response in your browser
2. The backend language you will use

If anything fails, tell us before the interview day so we can help.

## During the interview

- You will share your **entire screen**, not a single window.
- AI tools (ChatGPT, Copilot, Cursor, Claude, etc.) are **not allowed**. Please use an editor with all AI extensions turned off.
- At the end, push your code and add the interviewer as a collaborator on your private repository.
