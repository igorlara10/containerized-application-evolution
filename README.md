🚀 Containerized Application Evolution

Projeto prático de DevOps / Cloud, construído de forma evolutiva, com foco em boas práticas, baixo custo e aprendizado real, simulando o ciclo completo de uma aplicação moderna — do ambiente local ao deploy na AWS.

Este repositório não mostra apenas o “funcionou”, mas como os problemas apareceram e foram resolvidos, refletindo um cenário próximo ao mundo real.

🎯 Objetivo do Projeto

Demonstrar, de forma prática:

Containerização de aplicações

Comunicação entre serviços

Uso de Nginx como reverse proxy

Deploy local e em cloud (AWS)

Evolução gradual para infraestrutura como código

Mentalidade DevOps (testar → corrigir → evoluir)

🧱 Arquitetura Geral

Frontend: HTML/CSS/JS (site estático)

Backend: FastAPI (Python)

Banco de Dados: PostgreSQL

Reverse Proxy: Nginx

Containers: Docker + Docker Compose

Cloud: AWS (EC2 – Free Tier)

📁 Estrutura do Repositório
containerized-application-evolution/
│
├── part-01-local/
│   ├── frontend/
│   ├── backend/
│   ├── nginx/
│   ├── docker-compose.yaml
│   └── README.md
│
├── part-02-aws-ec2/
│   ├── deploy-notes.md
│   └── README.md
│
├── part-03-terraform-aws/   # (em andamento)
│   └── README.md
│
└── README.md

🧪 Parte 01 — Ambiente Local Containerizado

Nesta etapa, a aplicação foi construída e validada 100% localmente, garantindo que tudo funcionasse antes de qualquer subida para a cloud.

O que foi implementado:

🐳 Containers para Frontend, Backend e PostgreSQL

🔀 Nginx como reverse proxy

🌐 Comunicação entre containers via Docker Network

🔍 Endpoint /health para verificação do backend

🧾 Cadastro de usuários (nome + CPF) persistido no banco

Problemas reais enfrentados:

❌ Erro 502 Bad Gateway (Nginx)

❌ Upstream incorreto apontando para porta inexistente

❌ Ordem de inicialização dos serviços

❌ Configuração incorreta de rede entre containers

✅ Todos os problemas foram diagnosticados, documentados e corrigidos, reforçando a importância de logs, testes e validação incremental.

📄 Detalhes completos em:
part-01-local/README.md

☁️ Parte 02 — Deploy na AWS (EC2)

Após validação local, a aplicação foi levada para a AWS, mantendo a mesma arquitetura containerizada.

O que foi feito:

🖥️ Criação de instância EC2 (Free Tier)

🔐 Configuração de Security Groups

🐳 Instalação manual do Docker e Docker Compose

🚀 Execução do mesmo docker-compose em ambiente cloud

🌍 Acesso via IP público da instância

Aprendizados importantes:

Diferença entre ambiente local e cloud

Permissões de usuário para Docker (docker.sock)

Exposição correta de portas

Validação de aplicação em ambiente real

📄 Detalhes completos em:
part-02-aws-ec2/README.md

🧱 Parte 03 — Infraestrutura como Código (em andamento)

Próxima evolução do projeto, focada em automação e padronização.

Planejamento:

🧱 Provisionamento da AWS com Terraform

🖥️ Criação automática de EC2

🔐 Security Groups via código

🐳 Instalação automática do Docker

🚀 Deploy sem configuração manual

📄 Planejamento em:
part-03-terraform-aws/README.md

🔮 Melhorias Futuras (fora do escopo atual)

Este projeto foi estruturado para permitir crescimento futuro, como:

☁️ Uso de serviços gerenciados (RDS)

📦 ECS / EKS ou Fargate

🔁 Pipeline de CI/CD

✉️ Envio de e-mail de confirmação de cadastro

🧪 Separação de ambientes (test / prod)

Essas melhorias fazem parte da visão de evolução, não do escopo atual.

👤 Autor

Igor Lara
Focado em DevOps, Cloud e Automação, com aprendizado baseado em projetos práticos e resolução de problemas reais.

🔗 GitHub: https://github.com/igorlara10
