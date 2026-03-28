"""
Fake authentication/session helpers for the lab.

Implement the smallest thing that lets you answer:
- who is the current user?
- what role do they have?
"""


def get_current_user(handler):
    """
    Return the currently authenticated user for the request.

    Ideas:
    - read a cookie
    - read a header
    - hardcode a value first, then improve it
    """
    raise NotImplementedError("Implement current-user lookup")
