users = []

def add_user(user_id, name):
    users.append({"id": user_id, "name": name})
    print("User added successfully!")

def view_users():
    if not users:
        print("No users found.")
    for u in users:
        print(u)
