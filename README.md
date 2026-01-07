# Containerized Application Evolution 🚀

Este repositório documenta a evolução de uma aplicação **containerizada**, construída passo a passo com foco em **Docker, Nginx, Backend, Frontend e Banco de Dados**, evoluindo posteriormente para **AWS e práticas DevOps**.

O objetivo do projeto é demonstrar, de forma prática e didática, como uma aplicação real pode sair do ambiente local e evoluir para a nuvem, seguindo boas práticas de arquitetura e infraestrutura.

---

## 🎯 Objetivo do Projeto

- Consolidar conhecimentos em **Docker e Docker Compose**
- Entender a comunicação entre **Frontend, Backend, Nginx e Banco de Dados**
- Simular um fluxo real de evolução de um projeto DevOps
- Criar um **portfólio técnico evolutivo**, documentado por etapas

---

## 🧱 Arquitetura Geral (visão inicial)

- **Frontend**: aplicação web estática
- **Backend**: API em FastAPI
- **Banco de Dados**: PostgreSQL
- **Nginx**: reverse proxy e ponto único de entrada
- **Docker Compose**: orquestração local dos containers

---

## 📁 Estrutura do Repositório

containerized-application-evolution/
│
├── part-01-local/
│ ├── backend/
│ ├── frontend/
│ ├── nginx/
│ ├── docker-compose.yaml
│ └── README.md
│
├── part-02-aws-ec2/
│ └── README.md
│
├── part-03-terraform-ci-cd/
│ └── README.md
│
└── README.md

---

## 🧩 Partes do Projeto

### 🔹 Parte 01 — Ambiente Local Containerizado
Nesta etapa, toda a aplicação é executada localmente utilizando Docker e Docker Compose.

- Containers isolados por serviço
- Comunicação via network bridge
- Nginx atuando como reverse proxy
- Backend integrado ao PostgreSQL

📄 Detalhes completos em: `part-01-local/README.md`

---

### 🔹 Parte 02 — Deploy na AWS (EC2)
Nesta etapa, a aplicação será executada na **AWS**, utilizando uma instância EC2 (Free Tier).

- Criação de infraestrutura básica na AWS
- Instalação de Docker na EC2
- Execução da aplicação via Docker Compose
- Validação de acesso externo

📄 Detalhes em breve em: `part-02-aws-ec2/README.md`

---

### 🔹 Parte 03 — Evolução DevOps (futuro)
Planejada para etapas futuras do projeto:

- Infraestrutura como código
- Automatização de deploy
- Pipeline de CI/CD
- Boas práticas de versionamento e entrega contínua

📄 Planejamento em: `part-03-terraform-ci-cd/README.md`

---

## 🔮 Melhorias Futuras (fora do escopo atual)

Este projeto foi estruturado para permitir futuras evoluções, como:

- Uso de serviços gerenciados na AWS
- Escalabilidade da aplicação
- Envio de e-mail de confirmação de cadastro
- Separação de ambientes (test / prod)

Esses pontos fazem parte da visão de crescimento do projeto.

---

## 📌 Observação Importante

Este repositório **não representa um projeto final**, mas sim um **processo de aprendizado contínuo**, documentando decisões técnicas, erros encontrados e soluções aplicadas — exatamente como ocorre em ambientes reais.

---

## 👤 Autor

**Igor Lara**  
Projeto desenvolvido com foco em estudos práticos de **DevOps e Cloud Computing**.

---

⭐ Se este projeto te ajudou ou chamou sua atenção, fique à vontade para acompanhar sua evolução.
