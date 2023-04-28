# Start project:

```sh
docker compose up -d
./load-data.sh
```

# useful commands:

```sh
docker compose logs -f backend    # backend logs
docker compose logs -f            # all logs
./run-cmd.sh pytest -n 4          # run tests
```

# What's available:

### main parts

- backend: [http://127.0.0.1:8000](http://127.0.0.1:8000)

```
# preloaded users:
admin : admin
user1 : user1
user2 : user2
user3 : user3
```

### documentation

- swagger: [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/)
- redoc: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- mkdocs: [http://127.0.0.1:7000](http://127.0.0.1:7000)

- pgadmin: [http://127.0.0.1:5050](http://127.0.0.1:5050)

```
postgres@postgres.com : postgres
password db: postgres
```

### tools

- last coverage report [http://127.0.0.1:8888](http://127.0.0.1:8888)
- mailhog [http://127.0.0.1:8025](http://127.0.0.1:8025)
- rabbitmq management [http://127.0.0.1:15672](http://127.0.0.1:15672)
- redis commander [http://127.0.0.1:8081](http://127.0.0.1:8081)
- admin: [http://127.0.0.1:8000](http://127.0.0.1:8000/admin)
