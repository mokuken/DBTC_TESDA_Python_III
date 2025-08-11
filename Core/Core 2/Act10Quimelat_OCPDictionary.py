role_access = {
    "admin": "Full access",
    "editor": "Edit access",
    "viewer": "Read-only access",
}

def get_access(role):
    return role_access.get(role, "No access")

print(get_access("admin"))
print(get_access("editor"))
print(get_access("viewer"))
print(get_access("guest"))

role_access["contributor"] = "Contribute access"
print(get_access("contributor"))
