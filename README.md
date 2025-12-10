# Social Network API
A robust social network REST API built with Python, Django, and PostgreSQL, following Clean Architecture principles and Domain-Driven Design patterns.
## 🏗️ Architecture
This project implements a layered architecture with clear separation of concerns:

Domain Layer: Core business entities, value objects, and repository interfaces
Application Layer: Use cases and DTOs for orchestrating business logic
Infrastructure Layer: Database implementations, authentication, and external integrations
Presentation Layer: HTTP controllers and API endpoints

## 🚀 Features
### User Management

User registration and authentication with JWT tokens
Password hashing using Argon2
User profile management (update, delete)
User search functionality

### Posts

Create, read, and delete posts
Tag-based organization
Search posts by title
Optional channel association

### Channels

Create and manage content channels
Channel search by name
Post count tracking per channel
User ownership validation

### Comments

Comment on posts
List comments with pagination
Delete own comments

### Technical Features

JWT-based authentication
Value objects for data validation (Email, Password, Username)
Circuit breaker pattern for database resilience
Pagination support for list endpoints
Comprehensive error handling

