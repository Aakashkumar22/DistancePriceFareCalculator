# 🚖 Django Ride Pricing Module

![Django](https://img.shields.io/badge/Django-3.2+-green)  
![Python](https://img.shields.io/badge/Python-3.7+-blue)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A configurable pricing engine for ride-hailing services (Uber/Ola-like), supporting dynamic and day-specific pricing logic with a user-friendly admin panel and REST API.

---

## ✨ Features

- ✅ **Multi-Rule Dynamic Pricing**
  - Base and additional distance pricing
  - Time-of-day multipliers (e.g. peak hour)
  - Waiting time charges
- 📆 **Day-Specific Pricing Rules**
- 🔧 **Admin Configurable** via Django Admin
- 🌐 **Real-time Pricing API** (GET endpoint)
- 🕵️‍♂️ **Audit Logging** of pricing changes
- 🧪 **Unit Tests** for price calculation logic

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Django 3.2+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/django-ride-pricing.git
cd django-ride-pricing

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver

---
    




