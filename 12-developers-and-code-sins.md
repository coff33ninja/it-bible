⚠️ WARNING: USER ERROR ZONE

## Developers & Code Sins

---

**BEFORE YOU SAY 'IT COMPILES ON MY MACHINE'...**

- Your machine is a chaotic petri dish of mismatched dependencies, disabled firewalls, and a Python environment that hasn't been cleaned since 2019.
- The production server is not your personal development sandbox. It runs a clean, immutable OS. If it doesn't run there, it doesn't run anywhere.
- "It compiles" is the bare minimum of achievement. Does it run? Does it scale? Does it randomly delete the user table at 3 AM?

*Note: A Docker container that explodes on deploy because you hardcoded your local file paths is a you problem, not an ops problem.*

---

**BEFORE YOU SAY 'I'LL FIX IT IN PROD'...**

- No. Absolutely not. Production is not your staging environment, your testing playground, or your "let's see what happens" lab.
- Pushing untested code directly to the live branch at 4:55 PM on a Friday is how you earn a permanent ban from the deployment pipeline.
- The audit trail exists. We will know it was you. The rollback script is already written and waiting.

*Note: "I'll fix it in prod" is the battle cry of someone who has never been woken up at 3 AM by a pager duty alert.*

---

**BEFORE YOU CLAIM 'THAT'S NOT A BUG, IT'S A FEATURE'...**

- If the undocumented behavior corrupts the database silently, it is not a feature. It is a liability.
- Hiding broken functionality behind "intentional design choices" is not clever; it is fraudulent software development.
- We have users actively filing tickets. The screenshots are timestamped. Your gaslighting does not survive contact with evidence.

*Note: Calling a crash "an unscheduled system restart for security hardening" will not save you from the post-mortem.*

---

**BEFORE YOU SUBMIT CODE WITHOUT RUNNING THE TESTS...**

- "I forgot to run the tests" translates to "I don't care if I broke everything."
- A pull request that fails CI/CD checks is not a pull request; it is a donation of broken code to the repository.
- Every time you skip linting, a production server somewhere silently weeps.

*Note: If your response to a failing test is "comment it out so it passes," you are not a developer. You are a code vandal.*

---

**BEFORE YOU MERGE WITHOUT A CODE REVIEW...**

- Your code is not perfect. You are not an exception to the rule. Everyone needs a second pair of eyes.
- Merging your own pull request directly into main without so much as a glance from a peer is not confidence; it is recklessness.
- The person who breaks the build and then pushes a "fix" that breaks it further does not get to complain about the rollback process.

*Note: We do not trust the person who introduced a SQL injection vulnerability because they "didn't think it mattered."*

---

**BEFORE YOU HARDCODE A SECRET INTO THE SOURCE...**

- An API key in plaintext, committed to a public repository, is not a configuration strategy. It is a data breach waiting to happen.
- "I'll encrypt it later" is the same energy as "I'll fix it in prod."
- Git history is forever. Even after you remove the secret, it lives in the commit logs for anyone with a search engine to find.

*Note: Rotating credentials because you couldn't be bothered to use environment variables is a waste of everyone's time.*

---

**BEFORE YOU DEPLOY 'ONE SMALL HOTFIX' ON A FRIDAY NIGHT...**

- The "small hotfix" will cascade. It will touch something unrelated. It will bring down the entire microservices architecture.
- Friday 4:55 PM deployments are statistically the leading cause of ruined weekends for DevOps teams.
- If it absolutely cannot wait until Monday, the change request must be signed in blood and approved by three separate teams.

*Note: There is no such thing as a "quick" deployment. There are only deployments that haven't broken anything yet.*

---

**BEFORE YOU COMPLAIN ABOUT THE CODE REVIEW COMMENTS...**

- I am not "nitpicking." I am ensuring the next person who inherits your spaghetti nightmare can actually read it.
- Variable names like `data`, `data2`, `dataFinal`, `dataFinal_ACTUAL`, and `dataFinal_ACTUAL_v2` are not descriptive. They are a cry for help.
- A 2,000-line function with no comments and 14 levels of nested conditionals is not "legacy." It is archaeological debris.

*Note: If you feel personally attacked by a linter, this industry may not be for you.*

---

**BEFORE YOU BLAME 'MERGE CONFLICTS' ON THE TEAM...**

- Merge conflicts happen when two people edit the same code simultaneously. They are not a personal attack on your workflow.
- Screaming "just accept mine" without reviewing the diff is how critical logic gets silently deleted.
- If every single one of your branches results in apocalyptic merge conflicts, the common denominator is standing right in front of the keyboard.

*Note: Yelling at Git will not resolve the conflict. It will, however, make the rest of the team question your emotional stability.*

---

**BEFORE YOU PUSH A DEPENDENCY UPDATE WITHOUT TESTING...**

- Updating a package because "it was the latest version" without reading the changelog or running the test suite is a gamble with production stability.
- That minor version bump you just pushed introduces a breaking change to a completely unrelated module because of transitive dependencies.
- "But it passed on my machine" does not cover the 200 integration tests you didn't run.

*Note: npm update, pip install --upgrade, and blind faith are not a deployment strategy.*
