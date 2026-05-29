⚠️ WARNING: USER ERROR ZONE

## The "It Worked in Dev" Gambit

---

**BEFORE YOU DEPLOY TO PRODUCTION WITHOUT TESTING IN STAGING...**

- "It worked on my machine" — your machine is not production. Your machine has 32 GB of RAM, no concurrent users, and a pristine database with 3 test records. Production has 500 concurrent users, a database with 2 million records, and exactly 47 edge cases you did not think of. Your machine is a toy. Production is a battlefield.
- You deployed directly from your local branch to production. You bypassed staging, bypassed CI/CD, and bypassed code review. The one line change you made was to a config file that was different in production. Your local config points to localhost. Production now points to localhost. The site is down.
- "I did not think the database schema was different" — production uses a different schema than your local environment because the DBA made a change last week that you did not pull. Your migration dropped a column that production still uses. The column is gone. The data is gone. The backup is 3 days old.
- The code worked in dev because dev runs on the latest version of the runtime. Production runs on the version that was current when the server was provisioned in 2021. Your code uses a feature from the 2024 runtime. Production does not have that feature. Your code does not run.

*Note: "It worked in dev" is not a deployment argument. It is a confession that you did not test the actual target environment. Staging exists for a reason. Use it.*

---

**BEFORE YOU SAY 'IT IS JUST A SMALL CHANGE'...**

- "It is just a CSS change" — you changed a CSS class name. That class was referenced in 12 components, 3 of which are on the checkout page. The checkout button is now invisible. Users cannot complete purchases. The "small change" is a revenue emergency.
- "I am just updating a library version" — you updated a patch version. The library maintainer removed a function that was deprecated in 2019. Your code relied on that function. The build now fails. The dependency graph shows 17 packages that depend on the old behaviour. You are now in transitive dependency hell.
- "It is a one-line fix" — the one line is in a file that is imported by every module in the application. That one line introduces a circular import. The application no longer starts. The one-line fix caused a zero-line startup.
- "I am just renaming a variable" — the variable was referenced in a stored procedure, a report query, and a monitoring dashboard. None of those are in the codebase you searched. The rename broke production data pipelines. The "variable" was a column name.

*Note: There is no small change in production. Every change touches a system you cannot fully trace. The size of the change is not measured in lines of code. It is measured in surfaces of impact.*

---

**BEFORE YOU DEPLOY ON A FRIDAY AFTERNOON...**

- You deployed at 4:45 PM on a Friday. The deployment introduced a bug that causes data corruption after 6 hours of uptime. The corruption will manifest at 10:45 PM. You are at a bar. The on-call engineer is at a wedding. The data loss is unattended until Monday.
- "I will just revert if something goes wrong" — the revert requires a database migration rollback. The migration added a not-null constraint. The rollback fails because production data now exists that violates the old schema. You cannot revert. You can only write a forward fix. On a Friday night.
- You deployed a hotfix without tagging it. Nobody knows what version is running. The monitoring dashboard shows the old version number. The alerting system is checking against the wrong baseline. The false negatives will last until Tuesday when someone notices the version mismatch.
- "It is just a config change" — you changed an environment variable. The application caches environment variables at startup. The cache does not refresh until the next deployment. The config change you deployed is not active. But you are confident it is. The disconnect between reality and belief is now a production incident.

*Note: Friday deployments are not brave. They are reckless. The production gods do not care about your weekend plans. They will break on Saturday at 3 AM because that is when the universe balances the equation.*

---

**BEFORE YOU SKIP THE DEPLOYMENT CHECKLIST...**

- "We do not need a rollback plan" — you always need a rollback plan. The deployment will fail in a way you did not anticipate. The failure will be unique, novel, and specifically designed to make the rollback impossible. The lack of a plan is not confidence. It is denial.
- "The tests passed locally" — the tests passed locally because the test suite has not been updated in 8 months. There are no tests for the feature you are deploying. The tests that exist test code that was removed last sprint. The green checkmark means "the test framework loads successfully."
- "We can skip the smoke test" — the smoke test would have caught that the API returns 500 for authenticated requests. You skipped it. The first user to log in gets a white screen. All users log in. All users get a white screen. The smoke test would have taken 30 seconds. The outage takes 2 hours.
- "The staging environment is down, so we will just test in production" — staging being down is not a reason to use production as a test environment. It is a reason to fix staging. Production testing is not a backup plan. It is a disaster origin story.

*Note: A deployment checklist is not bureaucracy. It is the accumulated scar tissue of every outage that came before you. Ignoring it does not make you efficient. It makes you the next scar.*
