Minimal example to reproduce an issue I found with an import

To reproduce:

```
docker build -t breakme . && docker run -it --rm breakme litestar --help
```