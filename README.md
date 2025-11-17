# 🏦 NextGen Bank API

A fully-featured banking API built with Docker, Django Rest Framework, NGINX, Celery, Redis, and RabbitMQ. 🐳 💥

## 🏛️ System Architecture

![System Architecture](System%20Architecture.png)

## 💻 Tech Stack

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-A30000?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-3776A9?style=for-the-badge&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Flower](https://img.shields.io/badge/Flower-FF6600?style=for-the-badge&logo=flower&logoColor=white)
![JSON Web Tokens](https://img.shields.io/badge/JSON%20Web%20Tokens-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

## ✨ Features

- 🔐 **User Authentication:** Secure user registration, login, and logout using JWT.
- 👤 **User Profile:** Manage user profiles with details like name, phone number, and address.
- 📧 **Background Tasks:** Asynchronous task processing with Celery for sending emails.
- 📝 **API Documentation:** Auto-generated API documentation with Swagger/OpenAPI.
- 🐳 **Containerized:** Fully containerized with Docker for easy setup and deployment.

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amirthegreat1/nextgen-bank.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd nextgen-bank
   ```

3. **Create and configure the environment file:**

   - Create a `.env` file in the `.envs` directory by copying the example file:

     ```bash
     cp .envs/.env.example .envs/.env
     ```

   - Open the `.envs/.env` file and fill in the required environment variables.

4. **Build and run the application with Docker Compose:**

   ```bash
   docker-compose -f local.yml up --build
   ```

5. **Access the application:**

   - The API will be available at [http://localhost:8000](http://localhost:8000).

## 📚 API Documentation

The API documentation is automatically generated using `drf-spectacular`. You can access it at the following endpoints:

- **Swagger UI:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **ReDoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
