# Setup development environment

## Setup

## Debugging

### Django debugging

### Django + shell debugging


```python
 # this way you can debug celery tasks:
 >>> from todo.tasks import send_undone_todos_email_to_all_users
 >>> send_undone_todos_email_to_all_users()
```

## Tests

```bash
./run-tests.sh
```

## Common commands

```bash
poetry add <package>     # install package
poetry add pytest-cov --group test # install package
```
