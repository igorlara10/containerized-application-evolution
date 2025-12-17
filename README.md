# Containerized Application Evolution

Este repositório documenta a evolução de uma aplicação containerizada, iniciando em um ambiente **local com Docker** e evoluindo gradualmente para uma arquitetura **cloud-ready na AWS**, seguindo boas práticas de **DevOps**, **Cloud** e **Infraestrutura como Código**.

O objetivo principal deste projeto é **estudo prático**, **portfólio técnico** e **documentação de decisões reais**, incluindo problemas encontrados e como foram resolvidos ao longo do caminho.

---

## 🎯 Objetivo do Projeto

* Construir uma aplicação simples, porém realista
* Rodar tudo localmente com containers
* Garantir comunicação correta entre frontend, backend e banco de dados
* Evoluir o projeto em etapas bem definidas
* Preparar o terreno para deploy em cloud sem reescrita

---

## 🧩 Arquitetura – Parte 1 (Local)

Arquitetura inicial totalmente local utilizando Docker:

* **Frontend**: HTML + CSS + JavaScript (site estático)
* **Backend**: Python + FastAPI
* **Banco de Dados**: PostgreSQL
* **Proxy Reverso**: Nginx
* **Orquestração Local**: Docker Compose

### Fluxo de Comunicação

* User → Nginx (HTTP :80)
* Nginx → Frontend (HTTP :80 – network interna)
* Nginx → Backend (HTTP :8000 – network interna)
* Backend → PostgreSQL (TCP :5432)

Todos os containers se comunicam através de uma **bridge network interna** (`app-network`).

---

## 📁 Estrutura do Repositório

```
containerized-application-evolution/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── nginx/
│   └── nginx.conf
├── docker-compose.yaml
└── README.md
```
## ⚙️ Funcionalidades Implementadas (Parte 1)

- Cadastro de usuário (Nome e CPF)
- Persistência dos dados no PostgreSQL
- Endpoint de health check no backend
- Comunicação completa entre frontend e backend via Nginx
- Interface simples para cadastro e visualização

---

## 🧪 Problemas Reais Enfrentados

Durante o desenvolvimento, alguns erros reais foram encontrados e resolvidos, como:

- **Erro 502 Bad Gateway (Nginx)**
  - Causa: serviço de frontend não disponível na porta esperada
  - Solução: ajuste de portas e upstream no `nginx.conf`

- **Erro de conexão entre containers**
  - Causa: serviços fora da mesma network
  - Solução: padronização da `app-network` no Docker Compose

- **Configuração incorreta do Nginx**
  - Causa: uso indevido de diretivas globais em arquivos de conf.d
  - Solução: separação correta entre `nginx.conf` e `server blocks`

Esses problemas fazem parte do projeto propositalmente para simular um cenário real.

---

## 🚀 Como Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/containerized-application-evolution.git
cd containerized-application-evolution

# Subir os containers
docker compose up --build
````

Acesse:

* Frontend: [http://localhost](http://localhost)
* Backend Health Check: [http://localhost/api/health](http://localhost/api/health)

---

## 🧭 Evolução do Projeto

### 📌 Parte 1 – Ambiente Local (Atual)

* Aplicação containerizada
* Comunicação via Nginx
* Persistência em PostgreSQL
* Testes locais completos

### 📌 Parte 2 – Deploy Inicial na AWS

* Deploy da aplicação na AWS utilizando Free Tier
* Manter arquitetura simples e funcional
* Validação de funcionamento em ambiente cloud

### 📌 Parte 3 – Testes em Ambiente Cloud

* Testes completos com a aplicação rodando na AWS
* Validação de conectividade, performance básica e estabilidade

---

## 🔮 Melhorias Futuras (Fora do Escopo Atual)

Este projeto foi estruturado para permitir evoluções futuras, caso seja necessário:

* Uso de serviços gerenciados:

  * Amazon RDS (PostgreSQL)
  * ECS, EKS ou Fargate
* Infraestrutura como Código com Terraform
* Pipeline de CI/CD
* Envio de e-mail de confirmação de cadastro (SES / SNS / SQS)

Essas melhorias fazem parte da visão de longo prazo do projeto.

---

## 🧠 Motivação

Este repositório não é apenas sobre o resultado final, mas sobre o **processo**, as **decisões técnicas** e a **evolução contínua** de uma aplicação real.

---

## 📌 Autor

**Igor Madeira de Lara**
Cloud | DevOps | Containers | AWS

LinkedIn: [https://www.linkedin.com/in/igor-madeira-de-lara-2b0163213/](https://www.linkedin.com/in/igor-madeira-de-lara-2b0163213/)

---

📢 Este projeto faz parte de uma série de estudos documentados publicamente, com evolução contínua.
