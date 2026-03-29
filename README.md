# Python IDOR Lab

Small learning repo for building and then fixing an `IDOR` / broken access control example with Python's built-in HTTP tooling.

## Goal

You will implement:

- a deliberately vulnerable profile endpoint
- a simple fake authentication mechanism
- a fixed version with server-side authorization

## Suggested Flow

1. Start with a tiny in-memory user store
2. Add a route that reads a profile identifier from the query string.
3. Simulate a logged-in user.
4. Build the vulnerable behavior first.
5. Verify that changing the query exposes another profile.
6. Add the authorization check and compare the behavior.

## Repo Layout

- `src/idor_lab/app.py`: entry point
- `src/idor_lab/server.py`: request routing and HTTP handlers
- `src/idor_lab/auth.py`: fake login/session helpers
- `src/idor_lab/store.py`: in-memory data access
- `tests/`: room for your checks

## Run

Create a virtual environment if you want one, then:

```bash
python -m src.idor_lab.app
```

## Notes

- Keep this lab local only.
- The TODOs are intentional; fill them in as you build.
- Send me the code as you go and I will review the vulnerable path and the fix.
