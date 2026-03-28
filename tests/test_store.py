from src.idor_lab.store import get_profile

def test_get_profile_returns_user_when_username_exists():
    profile = get_profile("user")
    assert profile is not None
    assert profile["role"] == "user"

def test_get_profile_returns_none_when_username_does_not_exist():
    profile = get_profile("missing")
    assert profile is None