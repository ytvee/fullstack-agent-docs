#### Pull the PostgreSQL image

Pull the latest PostgreSQL image from Docker Hub. In your terminal, run `docker pull postgres` to pull the latest Postgres version from Docker Hub:

```bash copy
docker pull postgres
```

Alternatively, you can pull preferred version with a specific tag:

```bash copy
docker pull postgres:15
```

When postgres image is downloaded, you can check it in `Images` tab in Docker Desktop or by running `docker images`:

<Section>
```bash copy
docker images
```

```plaintext
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
postgres     latest    75282fa229a1   6 weeks ago     453MB
```
</Section>

