<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="PR Pilot Logo">
</div>

<p align="center">
  <a href="https://github.com/apps/pr-pilot-ai/installations/new"><b>Install</b></a> |
  <a href="https://docs.pr-pilot.ai">Documentation</a> |
  <a href="https://www.pr-pilot.ai/blog">Blog</a> |
  <a href="https://www.pr-pilot.ai">Website</a>
</p>


# PR Pilot Command-Line Interface
[![Unit Tests](https://github.com/PR-Pilot-AI/pr-pilot-cli/actions/workflows/unit_tests.yml/badge.svg)][tests]
[![PyPI](https://img.shields.io/pypi/v/pr-pilot-cli.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pr-pilot-cli)][pypi status]
[![License](https://img.shields.io/pypi/l/pr-pilot-cli)][license]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
<br>

[pypi status]: https://pypi.org/project/pr-pilot-cli/
[tests]: https://github.com/PR-Pilot-AI/pr-pilot-cli/actions/workflows/unit_tests.yml
[codecov]: https://app.codecov.io/gh/magmax/python-inquirer
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black
[license]: https://github.com/PR-Pilot-AI/pr-pilot-cli/blob/main/LICENSE

[PR Pilot](https://docs.pr-pilot.ai) is **simple and intuitive CLI** that assists you in your daily work:

```bash
pilot edit main.py "Add docstrings to all functions and classes"
```

**It works with [the dev tools you trust and love](https://docs.pr-pilot.ai/integrations.html)** - exactly when and where you want it.

```bash
pilot task "Find all bug issues on Github and Linear opened yesterday, post them to #bugs-daily on Slack."
```

[Prompt templates](https://github.com/PR-Pilot-AI/pr-pilot-cli/tree/main/prompts) let you can create powerful,
**executable prompt-based commands**, defined as Jinja templates:

```markdown
I've made some changes and opened a new PR: #{{ env('PR_NUMBER') }}.

I need a PR title and a description that summarizes these changes in short, concise bullet points.
The PR description will also be used as merge commit message, so it should be clear and informative.

Use the following guidelines:

- Start title with a verb in the imperative mood (e.g., "Add", "Fix", "Update").
- At the very top, provide 1-sentence summary of the changes and their impact.
- Below, list the changes made in bullet points.

# Your task
Edit PR #{{ env('PR_NUMBER') }} title and description to reflect the changes made in this PR.
```

Send PR Pilot off to give any PR a title and description **according to your guidelines**:

```bash
➜ PR_NUMBER=153 pilot task -f generate-pr-description.md.jinja2 --save-command
✔ Task created: 7d5573d2-2717-4a96-8bae-035886420c74 (0:00:00.00)
✔ Update PR #153 title and description to reflect changes made (0:00:17.87)
╭──────────────────────────── Result ──────────────────────────────────────────╮
│ The PR title and description have been updated. You can view the PR here.    │
╰──────────────────────────────────────────────────────────────────────────────╯
```

The `--save-command` parameter makes this call **re-usable**:

```bash
➜ pilot task -f generate-pr-description.md.jinja2 --save-command

 Save the task parameters as a command:

  Name (e.g. generate-pr-desc): pr-description
  Short description: Generate title and description for a pull request

 Command saved to .pilot-commands.yaml
```

You can now run this command **for any PR** with `pilot run pr-description`:

```bash
➜ pilot run pr-description
Enter value for PR_NUMBER: 83
╭──────────── Result ─────────────╮
│ Here is the link to the PR #83  │
╰─────────────────────────────────╯
```

To learn more, please visit our **[User Guide](https://docs.pr-pilot.ai/user_guide.html)** and **[demo repository](https://github.com/PR-Pilot-AI/demo/tree/main)**.
