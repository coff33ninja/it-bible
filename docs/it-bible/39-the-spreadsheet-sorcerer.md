⚠️ WARNING: USER ERROR ZONE

## The Spreadsheet Sorcerer

---

**BEFORE YOU USE EXCEL AS A DATABASE...**

- Excel is not a database. It is a spreadsheet application. The fact that it has rows and columns does not make it SQL Server. A database has relationships, constraints, and transactional integrity. Excel has none of these.
- You have a single Excel file with 50,000 rows, 47 columns, and 14 different named ranges that you use as a "lookup table" for your department's operational data. The file is 200MB. It crashes on open. It corrupts on save.
- "It works fine" — it works fine until someone else needs to query the data, or the file becomes corrupted, or you accidentally sort one column without selecting the rest, permanently scrambling your data.

*Note: Excel is not a substitute for a proper database. If you need to store, query, and relate data, use a database. Your spreadsheet is not scalable. It is a disaster waiting for a victim.*

---

**BEFORE YOU USE EXCEL AS A PROJECT MANAGEMENT TOOL...**

- Your "project tracker" is a single Excel file shared via email. Everyone has a different version. The formulas have been broken by someone overwriting a cell. The conditional formatting was lost when someone saved it as an older format.
- There are 14 different versions of this file across the team. Nobody knows which one is current. The project manager is manually reconciling changes every week. This is not project management. This is spreadsheet-assisted chaos.
- Project management software exists. It is designed for this purpose. It has version control, concurrent editing, and actual project management features. Your Excel file has none of these.

*Note: A project managed in Excel is not a managed project. It is a shared delusion of organisation. Use proper tools.*

---

**BEFORE YOU BUILD A 'COMPLEX' SPREADSHEET WITHOUT DOCUMENTING IT...**

- You built a spreadsheet with 14 nested IF statements, 6 VLOOKUPs, 3 INDEX-MATCH combos, and a macro that runs on open. It works perfectly. Only you understand it. When you leave the company, it will become a cursed artefact that nobody can maintain.
- "The logic is obvious" — it is obvious to you because you wrote it. To anyone else, it is a wall of cell references with no explanation. They will not know what B2 is supposed to contain or why F7 is formatted differently.
- Document your formulas. Label your columns. Use named ranges. Add comments. Future IT will either thank you or curse your memory. Choose which.

*Note: An undocumented spreadsheet is a time bomb. When the person who built it leaves, the knowledge leaves with them.*

---

**BEFORE YOU LINK CELLS ACROSS 12 DIFFERENT WORKBOOKS...**

- Your "master spreadsheet" pulls data from 12 different Excel files stored on a network drive. When one of those files is moved, renamed, or opened by someone else, the links break and your spreadsheet fills with #REF! errors.
- The fragile web of cross-workbook references you have built is not a system. It is a house of cards. One person accidentally saving a file in the wrong format will collapse the entire structure.
- "It saves time because I do not have to copy data" — it also breaks silently when someone reorganises the network drive. You will not know until the numbers look wrong and you have to trace the source of the error.

*Note: Cross-workbook references are not "integration." They are "dependencies waiting to fail."*

---

**BEFORE YOU USE SPREADSHEETS FOR INVENTORY MANAGEMENT...**

- Your "inventory system" is an Excel file with 7,000 rows of product data. It has no validation. Anyone can type anything into any cell. The "Quantity" column contains text, numbers, and at least one entry that says "maybe 5?"
- There is no audit trail. When someone deletes a row, the data is gone. When someone overwrites a formula with a hardcoded value, the calculation breaks. The inventory is never accurate.
- Inventory management systems exist. They have barcode scanning, real-time updates, multi-user access control, and audit trails. Your Excel file has none of these. It is not an inventory system. It is a wish.

*Note: A spreadsheet is not an inventory system. It is a placeholder until you outgrow your denial and buy actual inventory software.*
