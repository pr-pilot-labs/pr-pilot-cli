import webbrowser

import click
import pr_pilot
from pr_pilot import RepoBranchInput
from pr_pilot.util import _get_config_from_env
from rich.console import Console

from cli.detect_repository import detect_repository
from cli.status_indicator import StatusIndicator
from cli.util import get_current_branch


@click.command()
@click.pass_context
def pr(ctx):
    """🌐 Find and open the pull request for the current branch."""
    # Identify the current Github repo
    if not ctx.obj["repo"]:
        ctx.obj["repo"] = detect_repository()
    repo = ctx.obj["repo"]

    # Identify the current branch
    branch = get_current_branch()
    status_indicator = StatusIndicator(
        spinner=ctx.obj["spinner"], display_log_messages=ctx.obj["verbose"], console=Console()
    )
    status_indicator.update_spinner_message(
        f"Looking for PR number for {repo} on branch {branch}..."
    )
    status_indicator.start()

    # Retrieve the PR number
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.PRRetrievalApi(api_client)
        if not repo:
            raise Exception("Repository not found.")
        response = api_instance.resolve_pr_create(RepoBranchInput(github_repo=repo, branch=branch))
        status_indicator.stop()
        pr_link = f"https://github.com/{repo}/pull/{response.pr_number}"
        status_indicator.log_message(f"Found PR {pr_link}")
        webbrowser.open(pr_link)