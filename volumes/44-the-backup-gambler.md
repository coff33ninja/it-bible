⚠️ WARNING: USER ERROR ZONE

## The Backup Gambler

---

**BEFORE YOU SAY 'I DO NOT NEED A BACKUP, I AM CAREFUL'...**

- "I have never lost a file" — until you do. The first time is always a surprise. The confidence before the loss is directly proportional to the severity of the loss. The people who say "I do not need backups" are the people who will need them most desperately tomorrow.
- You have a "backup strategy." It is called "I email files to myself." Your inbox is not a backup. It is a distributed denial of service attack against your own future. The attachment limit is 25 MB. Your database backup is 2 GB. The strategy fails at the first real test.
- "I keep everything on OneDrive" — OneDrive syncs. It is not a backup. If you accidentally delete a file, OneDrive syncs the deletion. If ransomware encrypts your files, OneDrive syncs the encryption. A sync is a mirror. A mirror reflects the disaster. It does not prevent it.
- "I back up to an external drive once a month" — the external drive is on your desk. If there is a fire, flood, or theft, the external drive is in the same physical location as the computer. The backup is not a backup. It is a copy with the same risk profile as the original.

*Note: A backup that is in the same building as the original is not a backup. It is a second copy with the same single point of failure. The "3-2-1 rule" exists because people like you keep learning the hard way: 3 copies, 2 media types, 1 offsite.*

---

**BEFORE YOU TEST YOUR RESTORE PROCEDURE...**

- "We have backups" — when was the last time you tested a restore? Not "we have a process." Not "we have a script." When did you actually restore a file from backup and verify it opened correctly? If the answer is "never," you do not have backups. You have hopes.
- The backup job has been failing silently for 6 months. The error log shows "access denied" for the backup destination. Nobody checked the logs because "the backup is automated." Automation does not guarantee success. It guarantees failure at scale without human intervention.
- You restored the backup. It is corrupted. The backup software did not verify the integrity after writing. The tape had a bad sector. The cloud upload was interrupted. The backup completed with errors that nobody read. The file is there. The file is garbage.
- "We use RAID, that is backup enough" — RAID is not a backup. RAID protects against drive failure. It does not protect against accidental deletion, ransomware, or the intern who ran `rm -rf /` on the wrong server. RAID is high availability. Backup is disaster recovery. They are not the same thing.

*Note: The backup that has never been restored is not a backup. It is a ceremony. It makes you feel safe without providing safety. The only valid backup is the one you have successfully restored from.*

---

**BEFORE YOU STORE YOUR ONLY BACKUP IN THE CLOUD...**

- Your cloud backup is on the same provider as your production infrastructure. A provider outage takes down both your live environment and your ability to restore. You are betting everything on a single cloud vendor. That bet will pay off exactly until it does not.
- The cloud backup is configured with the same credentials as your live environment. A credential compromise gives an attacker access to both the original data and the backup. The backup is not a safety net. It is an additional attack surface.
- Your cloud backup bucket is publicly accessible. You did not check the permissions. You assumed "default settings are secure." The default setting was "public read." Your backup data is being indexed by search engines. Your customers' data is publicly available because you assumed.
- The cloud backup costs $5 per month. The restore costs $500 in egress fees. You did not read the pricing page. You are now deciding whether to pay the ransom or pay the egress fee. Both are more expensive than reading the documentation would have been.

*Note: A cloud backup is a contract, not a safety net. The contract has terms, limits, and conditions. Read them before you need them. The fine print becomes most expensive when you are already in a panic.*

---

**BEFORE YOU SAY 'THE IT DEPARTMENT HANDLES BACKUPS'...**

- "I assumed IT was backing up my laptop" — IT backs up the server. Your laptop is your responsibility. The documents you have been working on for 3 months exist only on your local drive. When the drive fails, the work is gone. IT will not recover it. IT told you this in the onboarding email you did not read.
- "I thought the network drive was backed up" — it is. But you have been saving files to your desktop for 4 years because it is "faster." The desktop is local. Local is not backed up. The files you thought were safe have been living in the unprotected zone the entire time.
- "The IT guy said he would set it up" — he set it up for the main file server. Your departmental share was not included because you did not specify it. IT cannot read your mind. Backup is not automatic. Backup is configured. If you did not request it, it was not configured.
- "I did not know we had a backup policy" — the policy was sent to you 3 years ago. You archived the email without reading it. The policy document has the backup schedule, retention periods, and restore procedures. You are now asking for a restore outside the retention window. The backup does not exist.

*Note: "I did not know" is not a restore request. It is a confession of negligence. Backup policies exist. Read them. Or accept that your data's survival depends on luck, not process.*

---

**BEFORE YOU RELY ON AUTOSAVE AS YOUR ONLY BACKUP...**

- "The autosave will get it back" — autosave saved the corrupted version. Over the good version. The autosave interval is 10 minutes. You made the critical edit 9 minutes ago. The autosave captured exactly the wrong moment. Your document is now permanently saved in its broken state.
- "I use version history in Google Docs" — version history keeps snapshots for 30 days on the free tier. Your critical document was edited 31 days ago. The version history shows "No older versions." The document existed before today. The history does not. You are looking at the final snapshot before the cliff.
- Autosave wrote over your original file when the application crashed. The crash corrupted the file. Autosave preserved the corruption. You now have a perfectly preserved copy of a broken file. The autosave did not save you. It saved the crash.
- You rely on "recover unsaved documents" in Word. That feature is a temporary file that gets deleted when you close the application without saving. You closed the application. You did not save. The temporary file is gone. The feature cannot recover what it was never designed to keep.

*Note: Autosave is a convenience, not a backup strategy. It saves versions, not safety. If autosave is your only backup, you do not have a backup. You have a false sense of security with a 10-minute delay.*

---

**BEFORE YOU KEEP CRITICAL DATA ON A SHARED DRIVE WITH NO VERSIONING...**

- "It is on the shared drive, so it is safe" — the shared drive has no versioning. Someone overwrote your file with a blank template. The original data is gone. The shared drive stores the latest version. The latest version is a blank template. Your work is in the void between saves.
- "Multiple people have copies of it" — multiple people have copies of the version from last month. The changes you made this week exist only on your laptop. Your laptop is not backed up. The collective copy network is a collection of outdated snapshots. Nobody has the current version.
- "I emailed it to myself as a backup" — you emailed the file to yourself 6 months ago. The file you need is the one with this quarter's data. You are going to spend 3 hours rebuilding it from the email attachment and your memory. The email was not a backup. It was a time capsule of obsolete information.
- The shared drive is mapped to a drive letter that changes when IT updates the network configuration. Your spreadsheet references the old drive letter. All the linked data is broken. The "backup" on the shared drive cannot be accessed by the file that needs it. Your data exists but your data does not work.

*Note: A shared drive is a collaboration space, not an archive. If it does not have versioning, retention policies, and regular snapshots, it is not a backup. It is a shared space where data goes to be accidentally overwritten.**
