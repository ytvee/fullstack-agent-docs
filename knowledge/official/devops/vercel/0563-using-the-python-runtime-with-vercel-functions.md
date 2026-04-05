--------------------------------------------------------------------------------
title: "Using the Python Runtime with Vercel Functions"
description: "Learn how to use the Python runtime to run Python applications on Vercel."
last_updated: "2026-04-03T23:47:22.162Z"
source: "https://vercel.com/docs/functions/runtimes/python"
--------------------------------------------------------------------------------

# Using the Python Runtime with Vercel Functions

> **🔒 Permissions Required**: The Python runtime

Use the Python runtime to run ASGI (Asynchronous Server Gateway Interface) and
WSGI (Web Server Gateway Interface) applications on Vercel. The Python Framework
Presets work with [FastAPI](/docs/frameworks/backend/fastapi),
[Flask](/docs/frameworks/backend/flask), Django, and other Python web
frameworks.

## Run a Python application

Vercel detects your framework automatically when it finds a matching dependency in
`requirements.txt`, `pyproject.toml`, or `Pipfile`. Your application must expose a top-level
ASGI or WSGI application named `app` in one of the following entrypoints:

- `app.py`
- `index.py`
- `server.py`
- `main.py`
- `wsgi.py`
- `asgi.py`

Vercel also checks the `src/`, `app/`, and `api/` directories for these files.

Here's a FastAPI example:

```python filename="app.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Python on Vercel"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

```toml filename="pyproject.toml"
[project]
name = "my-python-api"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.117.1",
]
```

To deploy a Python API alongside a frontend such as a Next.js app within the
same project, use [Services](/docs/services).

For framework-specific setup guides, see:

- [FastAPI on Vercel](/docs/frameworks/backend/fastapi)
- [Flask on Vercel](/docs/frameworks/backend/flask)

## Python version

Vercel reads the Python version from `pyproject.toml`, `.python-version`, or
`Pipfile.lock`.

If the required Python version is not defined or not supported, Vercel uses the
default version. The available versions are:

- **3.12** (default)
- **3.13**
- **3.14**

## Dependencies

Define dependencies in `pyproject.toml` (with or without a `uv.lock`),
`requirements.txt`, or a `Pipfile` with a corresponding `Pipfile.lock`.

```python filename="requirements.txt"
fastapi==0.117.1
```

*An example \`requirements.txt\` file that defines \`FastAPI\` as a dependency.*

## Streaming

Vercel Functions support streaming responses when using the Python runtime.
This lets you send parts of a response as they become ready.

## Controlling what gets bundled

By default, Python Vercel Functions include all files from your project that
are reachable at build time. There is no automatic tree-shaking for Python.

Make sure your `pyproject.toml` or `requirements.txt` only lists packages
necessary at runtime. Explicitly exclude files you don't need to keep bundles
small and avoid hitting size limits.

> **💡 Note:** Python functions have a maximum uncompressed bundle size of . See the
> .

To exclude unnecessary files (tests, static assets, test data), configure
`excludeFiles` in `vercel.json` under the `functions` key. The pattern is a
[glob](https://github.com/isaacs/node-glob#glob-primer) relative to your
project root.

```json filename="vercel.json"
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/**/*.py": {
      "excludeFiles": "{tests/**,__tests__/**,**/*.test.py,**/test_*.py,fixtures/**,__fixtures__/**,testdata/**,sample-data/**,static/**,assets/**}"
    }
  }
}
```

*Exclude common development and static folders from all Python functions to
stay under the 500 MB bundle limit.*

## Reading relative files

Python uses the current working directory when you pass a relative path to
[open()](https://docs.python.org/3/library/functions.html#open). The working
directory is the base of your project, not the directory containing the file.

## Python serverless functions

You can also place `.py` files inside an `/api` directory. Each file that
defines a `handler` (inheriting from `BaseHTTPRequestHandler`) or an ASGI/WSGI
`app` becomes a separate Vercel Function.

```py filename="api/index.py"
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
```


