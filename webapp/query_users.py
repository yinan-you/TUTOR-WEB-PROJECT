from website import db
from website.models import User

def query_users():
    users = User.query.all()  # Fetch all users
    for user in users:
        print(f"ID: {user.id}, Email: {user.email}, First Name: {user.first_name}")

if __name__ == "__main__":
    query_users()