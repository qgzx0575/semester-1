
import httpx

base_url = "https://dummyjson.com/"

content = "posts/1"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)
