# Parte 01 — Ambiente Local Containerizado

Nesta etapa, o projeto foi estruturado e testado localmente utilizando Docker e Docker Compose.

## Componentes
- Frontend (HTML estático)
- Backend (FastAPI)
- PostgreSQL
- Nginx como reverse proxy

## Objetivo
Validar a arquitetura local antes de qualquer deploy em nuvem.

## Como executar
```bash
docker compose up -d --build

Endpoints

Frontend: http://localhost

Backend health: http://localhost/api/health
