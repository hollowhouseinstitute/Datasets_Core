# Contributing to Hollow House Institute — Master License Suite

Thank you for contributing! This document explains how to contribute, propose changes, and request licenses.

How to contribute
1. Fork the repository and create a branch named `topic/<short-desc>` or `fix/<short-desc>`.
2. Commit changes with clear, concise messages.
3. Open a Pull Request describing:
   - Purpose of the change
   - Files changed and rationale
   - Any downstream impacts (data, licenses, privacy)
4. A maintainer will review; respond to review comments and iterate.

Code/style and tests
- Add or update tests for behavior changes.
- Follow any language-specific style guides (PEP8 for Python, etc.).
- Keep changes minimal and well-documented.

Data contributions
- Use the data/DATA_DICTIONARY_TEMPLATE.md for any new dataset.
- Include proof of consent/provenance and the license to publish.
- For large/external datasets: provide links and reproduction steps, do not commit PII.

Contributing legal language or licenses
- Changes to files in /legal must be coordinated with maintainers.
- If you propose a new license text or modification, open an Issue describing the justification and include versioned diffs.
- For commercial license requests, use the issue template “License Request” (see .github/ISSUE_TEMPLATE/license_request.md).

Issue & PR templates
- Please use the provided issue templates for bug reports and license requests.
- PRs that change license language must include a summary of legal impact and a maintainer sign-off.

Code of Conduct
- All contributors must follow the CODE_OF_CONDUCT.md. Be respectful and constructive.

Maintainers
- Maintainers will triage issues and prioritize critical items like security or privacy.