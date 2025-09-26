# Architecture
- Multi-tenant (org_id -> outlet_id) and RBAC (Admin/Manager/Staff).
- API: FastAPI, Pydantic v2, SQLAlchemy 2, Alembic (future days).
- Security: JWT, org/role guards via FastAPI dependencies.
- Envs: local, staging, prod. Secrets via GCP Secret Manager (later).
