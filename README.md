# Developer Task

1. [Task #1: Linux](./bash_task)<br>
Write a bash -oneliner to show all users that are able to log in and print all users in the following way to-
gether with their login shell:

```
/bin/zsh chris
/bin/zsh guest
/bin/bash root
/bin/sync sync
...
```

2. [Task #2: Python](./rest_api)<br>

Write a RESTful service in Python (both 2.x and 3.x is fine) that features the following endpoints. Try to
apply general python best practices where applicable (i.e. imagine this will be a larger application later).
- GET /fib/<start_idx>/<end_idx> : Generate the fibonacci numbers starting from » start_idx «
until » end_idx «. Remember, the fibonacci sequence is being calculated as follows: f n =
f n−1 + f n−2 ∀n > 2 ; with the first two numbers being f 1 = f 2 = 1 . Example result for
» /fib/3/5 « is 2 , 3 and 5 .
- GET /health : Return health information about the service. Definition of »healt check« is up to you.
You can use any framework we like. We recommend using Flask .