# Fibonacci REST API

To create docker image and container, also run a server type the following command:

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
After successful dockerizing open any browser and enter to this url: [http://localhost:8000](http://localhost:8000)

----------

### For unit tests
```bash
python manage.py test
```

## Video demo

[![](https://i.ytimg.com/vi/r5T83NUrhUY/hqdefault.jpg)](https://youtu.be/r5T83NUrhUY)