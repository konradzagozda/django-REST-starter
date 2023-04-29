# Setup development environment
This section is for VSCode users


# Debugging
Start containers with: `docker compose logs -f shell`
- server debugging: choose "Django" configuration and press `f5`
- shell debugging: choose "Django + Shell" configuration, run: `./run-cmd.sh python -m debugpy --wait-for-client --listen 0.0.0.0:5679 manage.py shell`, press `f5`
	```python
	# this way you can debug celery tasks:
	>>> from todo.tasks import send_undone_todos_email_to_all_users
	>>> send_undone_todos_email_to_all_users()
	```

# Tests
```bash
./run-cmd.sh pytest
./run-cmd.sh pytest -n 4
```

## Common commands
```bash
./run-cmd.sh poetry add <package> 				# install package
./run-cmd.sh poetry add pytest-cov --group test # install package
```
