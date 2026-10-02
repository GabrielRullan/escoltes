# Dispatch to Explorer 2

Investigate Firebase configuration, Firestore collections (especially `experiencies`), document schema, frontend Firebase SDK usage across docs/pages, Firestore security rules if present, and requirements for `docs/mallorca/admin_comentaris.md`.
Report findings in `handoff.md`.

## 2026-10-02T06:01:51Z
You are Explorer 2 (Firestore & Admin Interface Architecture).
Your working directory is: c:\Users\gabri\Documents\escoltes\.agents\teamwork\explorer_survey_2
Parent conversation ID: dcb42897-fdd4-46e4-b072-4c35d17ef50c

MANDATORY INPUT:
Read the authoritative user request at:
c:\Users\gabri\Documents\escoltes\.agents\teamwork\ORIGINAL_REQUEST.md

YOUR TASK:
Investigate Firebase/Firestore configuration, security rules, and architecture for the admin moderation page:
1. Where is Firebase configured in the repository? What SDK version (v8, v9 compat, modular v9+) is used across docs and HTML templates?
2. What is the current schema/structure of the `experiencies` collection documents (if any exist or are referenced)?
3. Are there `firestore.rules`? If so, what do they permit?
4. How should `docs/mallorca/admin_comentaris.md` be implemented?
   - How will it connect to Firestore?
   - How will it display pending comments (`authorized: false`)?
   - How will "Aprovar" (`authorized: true`) and "Rebutjar / Esborrar" (delete doc) work?
   - How will authorized comments be listed with option to revoke/delete?
   - What styling/UI approach matches the Escoltes Portal theme (Material for MkDocs)?
5. Detail the exact Firestore document fields, state transitions, and HTML/JavaScript code structure needed for `docs/mallorca/admin_comentaris.md`.

CONSTRAINTS:
- You are strictly read-only. Do not edit or create code files.
- Write your comprehensive findings to `c:\Users\gabri\Documents\escoltes\.agents\teamwork\explorer_survey_2\handoff.md`.
- Send a completion message back to parent when done.
