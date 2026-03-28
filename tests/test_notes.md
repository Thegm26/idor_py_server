# Test Notes

Manual checks to perform once you implement the handlers:

1. Log in or simulate a logged-in `guest`.
2. Request `/profile?user=guest`.
3. Change the query to `/profile?user=admin`.
4. Confirm the vulnerable route exposes data it should not.
5. Request `/fixed-profile?user=admin` as `guest`.
6. Confirm the fixed route denies access.

You can later turn these into automated tests if you want.
