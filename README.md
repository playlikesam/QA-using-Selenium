## What does "works" actually mean for a Pay Bill button?
The button is visible and clickable after login.
It redirects or triggers the expected payment flow.
The user is able to submit a payment.
The confirmation or success message/page is shown after payment.
The payment is reflected in Recent Activities or Payment History and Change in current bill.
## How would you test it without accidentally charging someone real money?
Use a test/dummy account.
Ensure the site has a sandbox or staging mode (if not, simulate clicks without final submission).
Do not submit the final payment step.
Use mocking or interception to prevent actual payment if necessary.
## What could go wrong that your script should catch?
Pay Bill button is:
Not updating Recent transactions
No change in Current Bill
## If the button breaks, how would you know WHY it broke?
Capture and log:
HTTP status codes.
Browser console errors (via headless browser logs).
Missing elements or timeouts.
Unexpected redirections.
Any JS exceptions (e.g. using Selenium logs).
