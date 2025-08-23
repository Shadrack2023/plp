import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

print(url)

if response.status_code == 200:
    data = response.json()  
    
    
    for post in data[:5]:  
        print("Post ID:", post["id"], "| Title:", post["title"])
else:
    print("Failed to fetch data. Status code:", response.status_code)
