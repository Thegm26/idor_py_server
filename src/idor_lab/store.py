"""
In-memory user/profile store for the lab.

We keep it tiny:
- one normal user
- one admin
- one or two fields of profile data
"""


USERS = {
    "user": {"password": "user", "role":"user", "bio": "Normal User"},
    "admin": {"password": "admin", "role":"admin", "bio": "Admin User"},
}


#TODO get profile returns the entire record including the password. get_user should be more appropriate
def get_profile(username):
    """Return the profile for a username, or None if it does not exist."""
    return USERS.get(username)
