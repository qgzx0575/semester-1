
# Task 2 - Python and httpx

We can use our existing virtual environment
- navigate to the `task2-python-httpx` folder

The template `fetch_post.py` shows a basic example
- Our program first needs to `import httpx` as a module

We can then access httpx methods which are documented at [python-httpx.org](https://www.python-httpx.org/)

# GET content

The code `fetch_post.py` demonstrates a successful GET request

The `httpx.get(url)` method returns a `response` object that we can interrogate
- we should first check the response code
    - modify the code to first print the response code as part of the program output
- if it is successful (200) we can extract the JSON content

# Compare to command-line httpx

What is the difference?

# Extension

`httpx.get()` may not succeed
- test the response code and report an error if 200 is not returned
- only print the JSON content if 200 is returned
- create a small test for successful and unsuccessful GET requests
