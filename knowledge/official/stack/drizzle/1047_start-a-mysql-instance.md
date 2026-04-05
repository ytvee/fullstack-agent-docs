#### Start a MySQL instance

To start a new MySQL container, run the following command:

```bash copy
docker run --name drizzle-mysql -e MYSQL_ROOT_PASSWORD=mypassword -d -p 3306:3306 mysql
```

1. The `--name` option assigns the container the name `drizzle-mysql`.
2. The `-e MYSQL_ROOT_PASSWORD=` option sets the `MYSQL_ROOT_PASSWORD` environment variable with the specified value. This is password for the root user.
3. The `-d` flag runs the container in detached mode (in the background).
4. The `-p` option maps port `3306` on the container to port `3306` on your host machine, allowing MySQL to be accessed from your host system through this port.
5. The `mysql` argument specifies the image to use for the container. You can also specify other versions like `mysql:8.2`.

You can also specify other parameters like:

1. `-e MYSQL_DATABASE=` to create a new database when the container is created. Default is `mysql`.
2. `-e MYSQL_USER=` and `-e MYSQL_PASSWORD=` to create a new user with a password when the container is created. But you still need to specify `MYSQL_ROOT_PASSWORD` for `root` user.

To check if the container is running, check `Containers` tab in Docker Desktop or use the `docker ps` command:

```plaintext
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                               NAMES
19506a8dc12b   mysql         "docker-entrypoint.s…"   4 seconds ago    Up 3 seconds    33060/tcp, 0.0.0.0:3306->3306/tcp   drizzle-mysql
```

