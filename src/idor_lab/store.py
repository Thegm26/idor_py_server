"""
In-memory user/profile store for the lab.

Keep it tiny:
- one normal user
- one admin
- one or two fields of profile data
"""


USERS = {
    "user": {"password": "user", "role":"user", "bio": "Normal User"},
    "admin": {"password": "admin", "role":"admin", "bio": "Admin User"},
}



def get_profile(username):
    """Return the profile for a username, or None if it does not exist."""
    return USERS.get(username)
