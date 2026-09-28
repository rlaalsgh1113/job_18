import requests

keyword = "파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0"
response = requests.get(url)
# print(response.status_code)
print(response.text)