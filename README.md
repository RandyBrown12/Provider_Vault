
# Provider Vault (EMRTS)

## Prerequisites

- **Python** 3.11 or higher
- **PostgreSQL** 17.2 or higher
- **uv** 0.7.9 or higher (install globally for virtual environment management)

---

## Installation

1. **Clone the repository**
	```bash
	git clone https://github.com/RandyBrown12/Provider_Vault.git
	cd Provider_Vault
	```

2. **Create and activate a virtual environment**
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

3. **Install dependencies**
	```bash
	uv pip install -r requirements.txt
	```

---

## Running the Project

Start the Django development server:

```bash
python provider_vault_django/manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Development: Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) hooks to help aid use in development.

1. **Ensure `pre-commit` is installed in your environment:**
	```bash
	uv pip install pre-commit
	```

2. **Set up pre-commit hooks:**
	```bash
	pre-commit install
	```
	This installs Git hook scripts so that every commit automatically runs all configured pre-commit checks.

3. **(Optional) Run all pre-commit hooks manually:**
	```bash
	pre-commit run --all-files
	```

> **Note:** Passing all pre-commit checks is required before commits can be made.
