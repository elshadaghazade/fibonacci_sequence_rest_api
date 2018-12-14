# Fibonacci REST API

To create docker image and container, also to run a server type the following command:

```bash
docker-compose up -d
```
----------

## What was done?

1. GET /fib/<start_idx>/<end_idx> endpoint
2. GET /health endpoint
3. Unit tests were written
4. Logger
5. Caching layer to avoid recalculating Fibonacci numbers. Expire time is 1 year
6. Dockerize service

----------

## How to run?

### For endpoints
After successful dockerizing open any browser and enter to this url: [http://localhost:5000](http://localhost:5000)

----------

### For unit tests
```bash
python -m unittest tests.py
```