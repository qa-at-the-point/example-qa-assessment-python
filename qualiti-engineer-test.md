# Quality Engineer Test Task

Veriff has a demo application, which is publicly available for anyone to try out the verification flow.

To access it, please use the following link: [https://demo.saas-3.veriff.me](https://demo.saas-3.veriff.me)
Try changing configuration, explore different options and see how the verification flow changes based on your input.

## Create Test Plan

Please describe the approach you would use to test this application and write a test plan.

## Automate

Create a set of automated tests for the configuration of the verification flow.

> We expect to see both UI and API tests.

## Scope

- You don't need to write tests for the verification flow itself (taking pictures, videos, selfies)
- Please also ignore the QR Code and mobile fallback parts
- For UI tests, only the demo session configuration part is in scope - configuring language, document, country, type, etc.
- For API tests, 2 endpoints are in scope - one that creates a new session, and `/sessions` endpoint that requests session configuration.

> Hint: You can find these endpoints using dev tools

## Additional Requirements

- Project must use version control
- Tests should produce an actionable report
- We should be able to run tests on our machines (we have Docker if that helps)
- Use any language and tools you like
- For simplicity of the task, you may consider that only Google Chrome browser is supported

> To submit your assessment, simply send us a link to your repo.
