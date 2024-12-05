# CS 3200 - Coop Compass

Welcome to the **Coop Compass** project! This platform is designed to streamline the co-op experience for students at Northeastern University. By enabling students to access personalized reviews and recruiters to post job opportunities, the platform bridges the gap between information and opportunity. Students can share their co-op experiences anonymously or openly, empowering others to make informed decisions.

## Link to Presentation
https://youtu.be/gugf1gvZp2I

## Key Features

- **Student Reviews:** Personalized, detailed reviews of co-op experiences, with an option for anonymity.
- **Recruiter Listings:** Job postings from company recruiters, synchronized with NUworks.
- **Authentic Insights:** Connection features for students to learn more from reviewers directly.
- **User Role Management:** Distinct functionalities for students, companies, and admins.

## Prerequisites

Before you begin, ensure you have the following:

- A GitHub account
- A terminal-based or GUI Git client
- **VSCode** with the Python Plugin
- A Python distribution installed on your laptop (e.g., using **Choco** for Windows, **brew** for Mac, **miniconda**, or **Anaconda**)

## Project Components

The application consists of three core components, each running in its own Docker container:

1. **Streamlit App:** Found in the `./app` directory, it serves as the user-facing interface.
2. **Flask REST API:** Located in the `./api` directory, it handles backend logic and data management.
3. **SQL Database:** SQL files for the data model and database setup are in the `./database-files` directory.

## Docker Commands for Container Management

Use Docker Compose to manage the containers:

- **Start All Containers:** `docker compose up -d`
- **Shutdown and Delete Containers:** `docker compose down`
- **Start Specific Service:** `docker compose up <service-name> -d` (e.g., `db`, `api`, or `app`)
- **Stop Containers (without deletion):** `docker compose stop`

## Directory Structure and Role Management

### Blueprints

- **Companies, Job Listings, Reviews, and Management:** Each blueprint manages a distinct part of the application with specific routes for backend data retrieval and manipulation.

### Frontend Components

- **`components` Folder:** Houses smaller UI components and modal dialogs for consistent organization.
- **`pages` Folder:** Includes all the pages of the application.
- **`style` Folder:** Contains CSS files for styling, ensuring separation from logic for clean code management.

### Utilities

- **`utils` Folder:** 
  - **Frontend Routes:** Contains all URLs for connecting frontend components to API endpoints.
  - **Modal and Styling Utilities:** Ensures modular and reusable functionality for styling and interaction.

---

## Getting Started

1. Clone the repository from GitHub.
2. Install Docker and ensure it’s running on your system.
3. Use Docker Compose to spin up the required containers for the app, API, and database.
4. Start contributing by editing the respective directories for the app, API, or database.

## Contribution Guidelines

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes with clear messages.
4. Open a pull request.

Thank you for being a part of the Coop Compass project! 🚀

**Credits To:**
- Aaryan Jain
- Rodrido Aldrey
- Gavin Bond
- Sheyan Lalani
- Samuel Seelan
