import random
import string

def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    return {
        "name": f"Test-User {random_string(4)}",
        "username": f"testuser_{random_string(5)}",
        "email": f"{random_string(6)}@example.com",
        "phone": "123-456-7890",
        "website": "example.com"
    }

def generate_post_data(user_id=1):
    return {
        "userId": user_id,
        "title": f"Post title {random_string(5)}",
        "body": f"Post body {random_string(10)}"
    }