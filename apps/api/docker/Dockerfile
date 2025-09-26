FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml /tmp/
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic "python-jose[cryptography]" passlib[bcrypt] httpx
COPY app ./app
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
