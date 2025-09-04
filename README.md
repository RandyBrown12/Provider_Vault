# Provider Vault (EMRTS)

## Overview
This software provides medical doctors with a centralized system to upload documents and use them to apply for medical applications.

## Prerequisites

- **Python** 3.11 or higher
- **PostgreSQL** 17.2 or higher
- **uv** 0.7.9 or higher (install globally for virtual environment management)

## Contributing
For contribution guidelines and development steps, please see [CONTRIBUTE.md](CONTRIBUTE.md).

## Running the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RandyBrown12/Provider_Vault.git
   cd Provider_Vault
   ```

2. **Create and Activate a Virtual Environment**
   - **Windows**
     ```bash
     uv venv
     .venv\Scripts\activate
     ```
   - **Linux/macOS**
     ```bash
     uv venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Copy or rename `.env.template` to `.env` and add your environment variables.

5. **Start the Django Development Server**
   - Run the application
     ```bash
     python manage.py runserver
     ```
   - The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

6. **Using the Application**
   - Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
