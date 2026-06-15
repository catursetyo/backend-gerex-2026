# Backend GEREX 2026 - Gugus Checker

FastAPI backend for the GERIGI X UKM EXPO ITS 2026 Gugus Checker feature. The API looks up a new student's group data by NRP and returns the student's name, gugus, and region from a local SQLite database.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- SQLite

## Project Structure

```txt
backend-gerex-2026/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── gugus_checker.py
├── assets/
│   └── image1.png
├── scripts/
│   └── init_db.py
├── .gitignore
├── README.md
├── database.db
└── requirements.txt
```

`database.db` is generated locally by the initialization script and is ignored by Git.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/catursetyo/backend-gerex-2026.git
cd backend-gerex-2026
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python scripts/init_db.py
```

This command creates `database.db`, recreates the tables, and inserts sample data.

### 5. Run the API server

```bash
uvicorn app.main:app --reload
```

By default, the server runs at:

```txt
http://127.0.0.1:8000
```

## Database Schema

The project uses three main tables:

<img src="/assets/image1.png" alt="Database schema">

- `regions`: stores region names.
- `gugus`: stores gugus names and links each gugus to a region.
- `mahasiswa_baru`: stores student NRP, name, and assigned gugus.

Relationships:

- One region can have many gugus.
- One gugus can have many new students.

The database is initialized with the following sample records:

| NRP | Name | Gugus | Region |
| --- | --- | --- | --- |
| 5027251066 | Catur Setyo Ragil | Gugus Arjuna | Region Surabaya |
| 5027251001 | Evandra Raditya | Gugus Bima | Region Surabaya |
| 5027251051 | Hendra Manudinata | Gugus Nakula | Region Luar Surabaya |

## API Endpoints

### Health Check

```http
GET /
```

Example response:

```json
{
  "message": "Gugus Checker API",
  "usage": "Gunakan endpoint /{NRP}, contoh: /5027251066"
}
```

### Check Gugus by NRP

```http
GET /{nrp}
```

Example request:

```http
GET /5027251066
```

The `nrp` path parameter must contain numbers only.

Example success response:

```json
{
  "nrp": "5027251066",
  "nama": "Catur Setyo Ragil",
  "gugus": "Gugus Arjuna",
  "region": "Region Surabaya"
}
```

Example response when the NRP is not found:

```json
{
  "detail": "Data mahasiswa tidak ditemukan"
}
```

FastAPI returns HTTP `422 Unprocessable Entity` when the path parameter does not match the numeric NRP format.
