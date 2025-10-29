import requests

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:    
        users = response.json()
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print("Failed to retrieve users:", response.status_code)
    
    
#get_users();

def create_post(userId, title, body):
    post = {
        "userId": userId,
        "title": title,
        "body": body
    }
    
    response = requests.post("https://jsonplaceholder.typicode.com/posts",
                            data = post )
    if response.status_code == 201:
        print("Post created successfully")
        print("Response:", response.json())
    else:
        print("Failed to create post:", response.status_code)
        
#create_post(1, "My New Post", "This is the content of my new post.")

def delete_post(postId):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{postId}")
    if response.status_code == 200:
        print(f"Post with ID {postId} deleted successfully.")
    else:
        print("Failed to delete post:", response.status_code)

#delete_post(1)

def update_post(postId, title=None, body= None):
    if title is None:
        print( "Title is required")
    
    if body is None:
        print("Body is required")
    
    post = {
        "title": title,
        "body": body
    }
    
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{postId}",data = post)
    if response.status_code == 200:
        print(f"Post with ID {postId} updated successfully.")
        print("Response:", response.json())
    else:
        print("Failed to update post:", response.status_code)


update_post(1, title="Updated Title", body="Updated body content.")