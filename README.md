# Provider_Vault from EMRTS

## Developing while using pre-commit

### Setting Up Pre-commit Hooks

Before you begin development, ensure that your `uv` environment includes the `pre-commit` package.

To set up the pre-commit hooks, run:

```sh
pre-commit install
```

This command installs the necessary Git hook scripts so that every commit automatically runs all configured pre-commit checks.

To manually run all pre-commit hooks on every file in the repository, use:

```sh
pre-commit run --all-files
```

Passing all pre-commit checks is required before commits can be made.
