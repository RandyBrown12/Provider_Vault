# How to Contribute

Welcome! Follow these steps to get started with local development and contributing to **Provider Vault**.

---

## Project Workflow
```mermaid
   flowchart TD
      A[Fork Dev Branch] --> B[Make changes]
      B --> C[Perform Pre-commit]
      C -- Failed --> B
      C -- Passed - Forked Branch is committed --> D[Code Review]
      D -- Failed --> B
      D -- Passed - Code is merged with branch --> E[Perform GitHub Actions Testing]
      E -- Failed --> B
      E -- Passed --> F[Perform Private Deploy to Server]
      F --> G[Perform User Acceptance Testing(UAT)]
      G -- Failed --> B
      G -- Passed --> H[Final Product is deployed]
```

---

## Running the Project Locally

1. **Fork the Repository**

   - Click the **Fork** button at the top of the GitHub page (above the About section).
2. **Switch to the `dev` Branch**

   ```bash
   git checkout dev
   ```
3. **Create and Activate a Virtual Environment**

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
4. **Install Dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```
5. **Set up pre-commit hooks**

   ```bash
   pre-commit install
   ```

   > **Note:** You must pass all pre-commit checks before commits can be made. To run all checks manually:
   >
   > ```bash
   > pre-commit run --all-files
   > ```
   >
6. **Configure Environment Variables**

   - Copy or rename `.env.template` to `.env` and add your environment variables.

---

## How to make commits to your repository

---

### Steps and Best Practices

1. **Stage your changes:**

   ```bash
   git add <file(s)>
   ```

   Or, go to the Source Control tab in VSCode and press the + button to stage all files, or click the + next to a file name to stage a single file.
2. **Write a clear commit message:**

   - Use present tense (e.g., "Fix bug in provider lookup logic").
   - Be concise but descriptive.
   - Example:
     ```bash
     git commit -m "Update README with setup instructions"
     ```

   Or, use the commit button in VSCode.
3. **Run pre-commit checks before committing:**

   - Pre-commit hooks run automatically if set up.
   - To run manually:
     ```bash
     pre-commit run --all-files
     ```
4. **Push your changes to your fork:**

   ```bash
   git push origin dev
   ```

   Or, using VSCode:
   1. Go to the Source Control tab (icon with branches) in the sidebar.
   2. Above the commit message box, click the "..." (More Actions) button.
   3. Select "Pull, Push" from the dropdown menu.
   4. Click "Push to...".
   5. Choose the remote branch (e.g., `origin/dev`) you want to push to.
   This will push your committed changes to the selected remote branch.

> **Tip:** Make small, focused commits for easier code reviews and troubleshooting.
> If you're working on multiple features, create a separate branch from the dev branch for each feature. Once a feature is complete and tested, merge it back into dev.

---

## How to Submit a Pull Request (PR)

Make sure your forked repository is updated with your latest commits before proceeding.

1. Go to the [Pull Request Page](https://github.com/RandyBrown12/Provider_Vault/pulls) for Provider Vault on GitHub.
2. Click the [New Pull Request](https://github.com/RandyBrown12/Provider_Vault/compare) button.
3. Click "compare across forks".
4. Set the base repository to `RandyBrown12/Provider_Vault` (branch: `dev`) and the head repository to your fork (branch: `dev`).
5. Add a title and description for your Pull Request.
6. Submit your Pull Request.

---

## Running the Project

Start the Django development server (inside the `provider_vault_django` folder containing `manage.py`):

```bash
python manage.py runserver
```

The app will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Running the tests

To run the Django tests, use:

```bash
python manage.py test
```

---
