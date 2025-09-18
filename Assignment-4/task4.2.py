import functools
user = {
    "username": "Appu",
    "authenticated": False  
}
def require_authentication(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if user.get("authenticated"):
            return func(*args, **kwargs)
        else:
            return f"[ERROR] User '{user.get('username')}' is not authenticated. Please log in."
    return wrapper
def login():
    user["authenticated"] = True
    return f"User '{user['username']}' has been logged in successfully "
def logout():
    user["authenticated"] = False
    return f"User '{user['username']}' has been logged out successfully "
@require_authentication
def view_dashboard():
    return f"Welcome {user['username']}!  You are now viewing the dashboard."
print(view_dashboard())  
print(login())           
print(view_dashboard())  
print(logout())          
print(view_dashboard())  