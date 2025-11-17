


# 🏦  Bank API

A **production-ready, scalable, and secure banking API** built with **Django REST Framework**, **Docker**, **NGINX**, **Celery**, **Redis**, **RabbitMQ**, and **PostgreSQL**.  
Designed with clean architecture, async background tasks, full containerization, and deployment-ready configuration.

![System Architecture](System%20Architecture.png)

---

## 📖 Table of Contents

- [🎯 About the Project](#about-the-project)
- [✨ Features](#features)
- [💻 Tech Stack](#tech-stack)
- [🚀 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🧪 Running Tests](#running-tests)
- [🚢 Deployment](#deployment)
- [📚 API Documentation](#api-documentation)
- [📫 Contact](#contact)

---

## 🎯 About the Project

**NextGen Bank API** is a robust and extensible backend system for banking operations.  
It includes powerful features such as:

- Secure JWT authentication  
- User profile management  
- Account creation and fund transfers  
- Asynchronous operations via Celery  
- Fully containerized system with NGINX, Redis, and RabbitMQ  

Designed for **local development**, **production deployment**, and **scalability** with distributed task processing.



## ✨ Features

- 🔐 **JWT Authentication** — Register, login, logout securely  
- 👤 **User Profiles** — Manage personal user details  
- 🏦 **Account Management** — Create and manage customer bank accounts  
- 💸 **Transaction System** — Transfer funds between accounts  
- 📧 **Async Tasks** — Celery + Redis + RabbitMQ for emails & background jobs  
- 📝 **API Documentation** — Swagger & Redoc via **drf-spectacular**  
- 🐳 **Fully Containerized** — API, NGINX, Celery workers, Celery beat  
- 📊 **Monitoring** — Flower for Celery task monitoring  
- 🔐 **Reverse Proxy Security** — NGINX for routing & environment isolation  

---

## 💻 Tech Stack

### **Backend**
<img src="https://cdn.simpleicons.org/python/3776AB" height="40" />  
<img src="https://cdn.simpleicons.org/django/092E20" height="40" />  
<img src="https://cdn.simpleicons.org/djangorestframework/A30000" height="40" />

### **Database**
<img src="https://cdn.simpleicons.org/postgresql/4169E1" height="40" />

### **Caching, Queues & Async**
<img src="https://cdn.simpleicons.org/redis/DC382D" height="40" />  
<img src="https://cdn.simpleicons.org/rabbitmq/FF6600" height="40" />  
<img src="https://cdn.simpleicons.org/celery/37814A" height="40" />

### **Infrastructure / DevOps**
<img src="https://cdn.simpleicons.org/docker/2496ED" height="40" />  
<img src="https://cdn.simpleicons.org/nginx/009639" height="40" />  
<img src="https://cdn.simpleicons.org/jsonwebtokens/000000" height="40" />

---

## 🚀 Getting Started

### Prerequisites

- Docker  
- Docker Compose  

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amirthegreat1/nextgen-bank.git
````

2. **Navigate into the project**

   ```bash
   cd nextgen-bank
   ```

3. **Setup environment variables**

   ```bash
   cp .envs/.env.example .envs/.env
   ```

   Then fill in the required environment variables inside `.env`.

4. **Build and start all services**

   ```bash
   docker-compose -f local.yml up --build
   ```

5. **Access the API**
   [http://localhost:8000](http://localhost:8000)

---

## 🧪 Running Tests

Run backend tests inside the API container:

```bash
docker-compose -f local.yml exec api python manage.py test
```

---

## 🚢 Deployment

The project includes an automated deployment script:

```bash
./do_server_deploy.sh
```

---

## 📚 API Documentation

Once running, access the documentation at:

* **Swagger UI** → [http://localhost:8080/api/v1/schema/swagger-ui](http://localhost:8080/api/v1/schema/swagger-ui)
* **ReDoc** → [http://localhost:8080/api/v1/schema/redoc](http://localhost:8080/api/v1/schema/redoc)

---

## 📫 Contact

**Amirhossein Zahmatkeshani**
Email: [amirhosseinzhmt@gmail.com](amirhosseinzhmt@gmail.com)

---

```

💻 Tech Stack
Backend
<img src="https://cdn.simpleicons.org/python/3776AB" height="40" /> <img src="https://cdn.simpleicons.org/django/092E20" height="40" /> <img src="https://cdn.simpleicons.org/djangorestframework/A30000" height="40" />
Database
<img src="https://cdn.simpleicons.org/postgresql/4169E1" height="40" />
Caching, Queues & Async
<img src="https://cdn.simpleicons.org/redis/DC382D" height="40" /> <img src="https://cdn.simpleicons.org/rabbitmq/FF6600" height="40" /> <img src="https://cdn.simpleicons.org/celery/37814A" height="40" />
Infrastructure / DevOps
<img src="https://cdn.simpleicons.org/docker/2496ED" height="40" /> <img src="https://cdn.simpleicons.org/nginx/009639" height="40" /> <img src="https://cdn.simpleicons.org/jsonwebtokens/000000" height="40" />
