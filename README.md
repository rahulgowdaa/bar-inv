# Bar & Retail Inventory — Monorepo
Day 1 scaffolding with FastAPI stub, CI, pre-commit, and Docker.

## Dev quickstart
cd apps/api
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload

curl http://127.0.0.1:8000/me
curl -X POST http://127.0.0.1:8000/auth/login -H 'content-type: application/json' -d '{"email":"a@b.c","password":"x"}'
