# Full Stack Live Coding Task: Task Manager

## Overview

You will build a small task manager with a REST API and a React frontend.

- **Total session:** 45 minutes
- **Coding time:** 30 minutes
- **Code walkthrough and questions:** 10 minutes

The task has 4 levels. Nobody is expected to finish everything in 30 minutes. Complete the levels in order and focus on working, readable code over speed.

## Rules

- Share your entire screen for the whole session.
- You can use Google, MDN, and the official docs for your language and framework.
- AI tools (ChatGPT, Copilot, Claude, etc.) are **not allowed**. Please keep all AI extensions in your editor turned off.
- Think out loud while you work. We care about how you approach problems as much as the final result.
- Ask questions any time if something is unclear.

## Setup

Use the starter project you set up before the interview, with the backend folder for your chosen language.

Before you start coding, confirm:

1. The React app is running at `http://localhost:5173`.
2. `http://localhost:5173/api/health` returns `{ "ok": true }`.

Keep the backend on port `3001`. Store data **in memory** (an array or list). You do not need a database.

## Data Model

```json
{
  "id": 1,
  "title": "Write project proposal",
  "completed": false,
  "createdAt": "2026-09-28T10:00:00.000Z"
}
```

## Tasks

### Level 1: REST API

Build these endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/tasks` | Return all tasks |
| `POST` | `/api/tasks` | Create a task. Body: `{ "title": "..." }` |
| `PATCH` | `/api/tasks/:id` | Update `title` or `completed` |
| `DELETE` | `/api/tasks/:id` | Delete a task |

Test your endpoints with curl, Postman, or the browser before moving on.

### Level 2: Validation and Errors

- Reject a `POST` or `PATCH` with an empty or missing `title`. Return `400` with a clear error message.
- Return `404` when a task with the given `id` does not exist.
- Use correct status codes for success (`200`, `201`, `204`).

### Level 3: Frontend

- Show the task list from `GET /api/tasks`.
- Add a form to create a new task.
- Add a checkbox to mark a task as completed.
- Add a button to delete a task.
- Show a loading state and an error message when a request fails.

### Level 4: Filtering

- Support `GET /api/tasks?status=completed` and `GET /api/tasks?status=pending` on the backend.
- Add filter buttons in the frontend: **All**, **Completed**, **Pending**.
- Filtering should be done by the API, not only in the frontend.

### Bonus

- Write one or two tests for your API using any testing tool for your language.
- Show a clear empty state when there are no tasks (for example, "No tasks yet").

## After Coding

In the last 10 minutes, you will:

1. Walk us through your code and explain your decisions.
2. Answer a few follow-up questions about your implementation.
3. Ask us anything about the role or the team.

Good luck!
