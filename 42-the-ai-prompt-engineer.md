⚠️ WARNING: USER ERROR ZONE

## The AI Prompt Engineer

---

**BEFORE YOU ASK THE AI TO WRITE PRODUCTION CODE WITHOUT REVIEW...**

- You pasted a prompt into ChatGPT and deployed the output directly to production. You did not read the code. You did not test it. You assumed it was correct because the AI "sounded confident." The AI writes code that compiles but does not work. Those are different things.
- The AI generated a regex that looks correct, passes the first test case, and fails catastrophically on every edge case you did not think to include in your prompt. You did not include edge cases because you did not think of them. The AI did not either.
- "It wrote 200 lines in 30 seconds, it must be efficient" — the AI wrote 200 lines because it does not know when to stop. It will generate boilerplate, then comment the boilerplate, then write a function that calls the boilerplate, then write a test for the function that calls the boilerplate. You now have technical debt that compounds faster than the AI can generate it.
- The AI does not know your codebase. It does not know your coding standards. It does not know that you use tabs, not spaces. It does not know that your team uses camelCase not snake_case. It is writing code in a vacuum and the vacuum is your production environment.

*Note: AI-generated code is not reviewed code. It is generated code that happens to look like reviewed code. The difference is the part where a human reads it and says "this is wrong." Do not skip that part.*

---

**BEFORE YOU TELL THE AI TO 'MAKE IT BETTER' WITHOUT SPECIFYING WHAT BETTER MEANS...**

- "Make it more efficient" — the AI replaced your readable, maintainable code with a one-liner that runs 3% faster and is completely incomprehensible. Your team will spend 4 hours figuring out what it does. The 3% speed gain will be lost in the time it takes to explain the code in code review.
- "Improve the design" — the AI redesigned the architecture. It now uses a microservices pattern for a CRUD app with 3 endpoints. You now have 6 services, a message queue, and a container orchestration layer for an application that could have been a single function.
- "Make it more secure" — the AI added 47 layers of input validation that block legitimate users and fail to stop the one injection attack you actually need to prevent. The security is performative. The vulnerability is still there.
- "Refactor this" — the AI refactored your clean, working code into an abstract factory pattern because that is what the training data suggests for the word "refactor." You now have 12 classes, 6 interfaces, and 3 abstract base classes. The original was 40 lines in a single file.

*Note: "Make it better" is a prompt, not a specification. It will always produce something that is technically different and functionally worse. Specify the outcome, not the improvement.*

---

**BEFORE YOU COPY-PASTE AI OUTPUT INTO A SECURITY CONTEXT...**

- You asked the AI to write an encryption function. It used a cipher mode that was deprecated in 2018. It generated a static IV. It handled key storage by "generating a random key and printing it to the console." The AI does not know cryptography. It knows what cryptography looks like in stack overflow posts.
- The AI generated a SQL query with string interpolation because that is what 80% of its training data uses. It does not know about SQL injection. It knows that SQL queries are often written with + signs. You deployed it. Your database is now exfiltrated.
- "The AI said it was secure" — the AI does not know what secure means. It has no internal model of threat, risk, or harm. It generates text that matches the pattern "this is secure" accompanied by text that matches the pattern of a secure function. The two are not connected.
- You pasted an API key into the AI prompt as an example. The AI stored it in its context window. The key is now part of the model's ephemeral memory. You do not know where that context will be used. You do not know how long it persists. You have compromised the key.

*Note: An AI that cannot distinguish between "this is an example" and "this is data to use" should not be given real credentials, real data, or real code. Treat every prompt as a disclosure.*

---

**BEFORE YOU USE AI TO WRITE YOUR SECURITY POLICIES...**

- The AI generated an acceptable use policy that prohibits the use of AI to generate policies. The AI did not detect the irony. It does not have irony. It has a pattern for "acceptable use policy" and a pattern for "no AI" and it combined them without understanding the contradiction.
- "Write a password policy" — the AI generated a policy requiring 12 characters, special symbols, and a change every 30 days. That policy was written by an AI trained on policies written before NIST updated its guidance in 2017. The policy contradicts current best practice. You now have a policy that reduces security by following outdated patterns.
- The AI generated a compliance document that references regulations that do not exist. It invented a law. It cited a statute number that looks real but leads to an unrelated regulation. The confidence in the citation was identical to the confidence in the real citations. You cannot distinguish them without checking every source.
- "Review this contract" — the AI summarised the contract, but it omitted the clause about automatic renewal with penalty because that clause used negative language that the AI interpreted as less important. You signed. The penalty is now enforceable. The AI will not be held liable.

*Note: An AI that generates text cannot distinguish between true and false, real and imaginary, current and outdated. It can only distinguish between probable and improbable text patterns. Compliance is not a pattern-matching problem.*

---

**BEFORE YOU RELY ON AI OUTPUT WITHOUT VERIFICATION...**

- The AI gave you a command that it said would install a package. The command contained a typo that installed a typosquatting package with the same name. The AI did not verify the package source. It generated the most probable character sequence for "install package." Malware uses probability too.
- "The AI said it tested it" — the AI did not test anything. It generated a description of what testing might look like. It generated a test output that matches the pattern of a successful test. There is no runtime. There is no environment. There is only text about what a test would do if one had been run.
- The AI generated a deployment script that works on its machine but fails on yours because the paths are absolute. The AI assumed a file system that matches the training data. Your file system is real. The two are not the same.
- You asked for a version number and the AI suggested a package version that does not exist. The AI hallucinated a version that is the average of the last 5 versions it saw in training. The version you pinned does not resolve. The build is broken. The AI is not in the build pipeline. You are.

*Note: The AI does not know the difference between "I generated this" and "this is true." The only thing between you and a hallucinated disaster is your willingness to verify. Verify everything. Then verify it again.*
