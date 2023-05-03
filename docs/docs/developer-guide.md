# Setup development environment

This section is for VSCode users

## Setup

1. `cd backend`
2. `poetry install`
3. select correct environment with vscode

## Debugging

### Django debugging

1. `docker compose down`
2. choose "Django" configuration and press `f5` containers will start automatically

### Django + shell debugging

1. Start containers with: `docker compose -f docker-compose.yml -f docker-compose.debug.yml up`
2. choose "Django + Shell" configuration
3. run shell: `./run-cmd.sh python -m debugpy --wait-for-client --listen 0.0.0.0:5679 manage.py shell`
4. connect debugger with `F5`

```python
 # this way you can debug celery tasks:
 >>> from todo.tasks import send_undone_todos_email_to_all_users
 >>> send_undone_todos_email_to_all_users()
```

## Tests

```bash
./run-cmd.sh pytest
./run-cmd.sh pytest -n 4
```

## Common commands

```bash
./run-cmd.sh poetry add <package>     # install package
./run-cmd.sh poetry add pytest-cov --group test # install package
```
