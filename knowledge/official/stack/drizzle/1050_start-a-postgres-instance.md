#### Start a Postgres instance

To start a new PostgreSQL container, run the following command:

```bash copy
docker run --name drizzle-postgres -e POSTGRES_PASSWORD=mypassword -d -p 5432:5432 postgres
```

1. The `--name` option assigns the container the name `drizzle-postgres`.
2. The `-e POSTGRES_PASSWORD=` option sets the `POSTGRES_PASSWORD` environment variable with the specified value.
3. The `-d` flag runs the container in detached mode (in the background).
4. The `-p` option maps port `5432` on the container to port `5432` on your host machine, allowing PostgreSQL to be accessed from your host system through this port.
5. The `postgres` argument specifies the image to use for the container. You can also specify other versions like `postgres:15`.

You can also specify other parameters like:

1. The `-e POSTGRES_USER=` option sets the `POSTGRES_USER` environment variable with the specified value. Postgres uses the default user when this is empty. Most of the time, it is `postgres` and you can check it in the container logs in Docker Desktop or by running `docker logs <container_name>`.
2. The `-e POSTGRES_DB=` option sets the `POSTGRES_DB` environment variable with the specified value. Defaults to the `POSTGRES_USER` value when is empty.

To check if the container is running, check `Containers` tab in Docker Desktop or use the `docker ps` command:

```plaintext
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
df957c58a6a3   postgres   "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds   0.0.0.0:5432->5432/tcp   drizzle-postgres
```

