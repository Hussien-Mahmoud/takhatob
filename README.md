# Live Speech - Django Web Application

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Environment Setup](#environment-setup)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
5. [Configuration](#configuration)
   - [Environment Variables](#environment-variables)
6. [Features](#features)
   - [User Management](#user-management)
   - [Centers Module](#centers-module)
   - [Specialists Module](#specialists-module)
   - [Chat System](#chat-system)
   - [Payment Processing](#payment-processing)
7. [Development](#development)
   - [Adding New Features](#adding-new-features)
8. [Deployment](#deployment)
   - [Development Environment](#development-environment)
   - [Production Environment](#production-environment)
   - [Docker Support](#docker-support)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

Live Speech is a web platform that connects clients with specialists through centers. The platform features:
- Multi-user roles (Client, Specialist, Center)
- User profiles with ratings and reviews
- Real-time chat functionality
- Payment processing via Stripe
- Center profile management
- Specialist certification verification

## Technology Stack

- **Backend Framework**: Django 4.2+
- **Database**: PostgreSQL
- **Asynchronous Support**: Channels (WebSockets)
- **Frontend**: Django Templates, Bootstrap
- **Storage**: Local File System (dev) / Google Cloud Storage (prod)
- **Payment Processing**: Stripe API
- **Rich Text Editing**: TinyMCE
- **Image Handling**: Django ImageField

## Project Structure

- **main**: Core application functionality
- **users**: Custom user model with Client, Specialist, and Center user types
- **chat**: Real-time chat using Django Channels
- **centers**: Center profiles, listings, and review management
- **specialists**: Specialist profiles, certifications, and service offerings
- **payment**: Stripe payment integration
- **website**: Django project configuration with environment-specific settings

## Environment Setup

### Prerequisites

- Python 3.13.2
- PostgreSQL
- Virtualenv
- Stripe account (for payments)
- Google Cloud Storage (for production)

### Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration values
   ```

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Start the development server
   ```bash
   python manage.py runserver
   ```

## Configuration

The project uses different settings configurations for different environments:

- **Development**: `website/settings/dev.py`
- **Production**: `website/settings/prod.py`
- **Production with HTTPS**: `website/settings/prod_https.py`

### Environment Variables

Key environment variables needed (see `.env.example` for a complete list):

- `SECRET_KEY`: Django secret key
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `PGDATABASE`, `PGUSER`, `PGPASSWORD`, `PGHOST`, `PGPORT`: PostgreSQL connection settings
- `STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`: Stripe API credentials
- Google Cloud Storage credentials (for production)

## Features

### User Management

The application implements a custom user model with three user types:

- **Client**: End users who seek specialist services
  - Can browse centers and specialists
  - Can request chat sessions with specialists
  - Can provide reviews and ratings

- **Specialist**: Service providers with specialized skills
  - Can set service prices
  - Have profile pages with description, experience, and ratings
  - Can accept or reject chat requests from clients

- **Center**: Organizations that group specialists
  - Have profile pages with description and ratings
  - Can edit their profile information
  - Can be reviewed by clients

The system includes:
- Custom authentication using email
- Specialized registration forms for each user type
- Profile management
- Rating/review system

### Centers Module

Centers represent organizations or facilities that can be browsed by clients:

- **Center Listing**: Grid view of all centers with basic information
- **Center Details**: Detailed view of a center showing:
  - Description
  - Experience
  - Average rating
  - Reviews from clients
- **Center Management**: Centers can edit their profiles including:
  - Profile image
  - Username
  - Experience
  - Description (with rich text editing)

### Specialists Module

Specialists offer professional services through the platform:

- **Specialist Listing**: Browse all specialists with basic information
- **Specialist Profiles**: Detailed specialist information including:
  - Profile image
  - First and last name
  - Experience in years
  - Descriptive excerpt
  - Detailed description (with rich text formatting)
  - Service price
  - Average rating
  - Reviews from clients
  - Uploaded certifications with images
  
- **Profile Management**: Specialists can edit their profiles:
  - Update personal information
  - Set service prices
  - Upload profile image
  - Manage professional certifications
  - Update experience and qualifications
  
- **Certification System**: Specialists can upload images of their certifications to verify their expertise
  
- **Review System**: Clients can rate and review specialists they've worked with:
  - Rating on a 1-10 scale
  - Text review
  - One review per client per specialist
  
- **Chat Integration**: Direct access to request a chat with a specialist:
  - Chat request button on profile
  - Price display for chat services
  - Access to active chats

### Chat System

- Real-time communication via WebSockets
- Chat request and approval workflow
- Payment integration for chat services
- Persistent message history
- Notification system for new messages

### Payment Processing

- Secure payment handling with Stripe
- Payment webhook integration
- Service payment processing for specialist consultations

## Development

### Adding New Features

1. Create a new app if needed: `python manage.py startapp appname`
2. Add your app to INSTALLED_APPS in settings/base.py
3. Create models, views, and templates
4. Register URLs in your app's urls.py file

## Deployment

### Development Environment
- Uses local file storage
- Debug mode enabled
- Minimal security settings

### Production Environment
- Google Cloud Storage for media and static files
- Debug mode disabled
- Enhanced security settings
- HTTPS enforcement (with prod_https.py)

### Docker Support

Docker support for this project is currently under development and not yet ready for use.

## Contributors

- [Hussien Mahmoud](https://github.com/Hussien-Mahmoud) - Project Lead and Backend Developer
- [Ashraf M. Helmy](https://github.com/mansibaldaniya) - Fronend Developer
