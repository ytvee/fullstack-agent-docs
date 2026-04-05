#### Pull the MySQL image

Pull the latest MySQL image from Docker Hub. In your terminal, run `docker pull mysql` to pull the latest MySQL version from Docker Hub:

```bash copy
docker pull mysql
```

Alternatively, you can pull preferred version with a specific tag:

```bash copy
docker pull mysql:8.2
```

When MySQL image is downloaded, you can check it in `Images` tab in Docker Desktop or by running `docker images`:

<Section>
```bash copy
docker images
```

```plaintext
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
mysql        latest    4e8a34aea708   2 months ago   609MB
```
</Section>

