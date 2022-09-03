#!/usr/bin/env python

import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from github.PullRequest import PullRequest
from github.Repository import Repository

from pr_another_repo import git
from pr_another_repo.client import gh
from pr_another_repo.settings import settings


def clone_dest_repo(repo: Repository) -> tempfile.TemporaryDirectory:
    temp_dir = tempfile.TemporaryDirectory()
    clone_url = urlparse(repo.clone_url)
    clone_url_with_credentials = clone_url._replace(
        netloc=f"{settings.action_inputs.github_api_token.get_secret_value()}@{clone_url.netloc}"
    )
    subprocess.run(
        ["git", "clone", clone_url_with_credentials.geturl(), temp_dir.name], check=True
    )
    return temp_dir


def copy_folder(repo_dir: Path) -> Path:
    source_files = Path(__file__).parent.joinpath(settings.action_inputs.source_folder)
    if settings.action_inputs.source_folder.is_absolute():
        dest_path = Path(*settings.action_inputs.source_folder.parts[1:])
    else:
        dest_path = settings.action_inputs.source_folder
    dest_dir = repo_dir / dest_path
    return shutil.copytree(source_files, dest_dir)


def commit_changes_to_branch(repo_dir: Path) -> None:
    subprocess.run(
        ["git", "checkout", "-b", settings.action_inputs.destination_head_branch],
        cwd=repo_dir,
        check=True,
    )
    subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
    subprocess.run(
        ["git", "commit", "-m", "automated commit message"], cwd=repo_dir, check=True
    )
    subprocess.run(
        [
            "git",
            "push",
            "-u",
            "origin",
            f"HEAD:{settings.action_inputs.destination_head_branch}",
        ],
        cwd=repo_dir,
        check=True,
    )


def delete_remote_branch_head_branch(repo: Repository):
    ref = repo.get_git_ref(f"heads/{settings.action_inputs.destination_head_branch}")
    ref.delete()


def issue_pr(repo: Repository) -> PullRequest:
    return repo.create_pull(
        settings.action_inputs.pull_request_title,
        settings.action_inputs.pull_request_body,
        settings.action_inputs.destination_base_branch,
        settings.action_inputs.destination_head_branch,
    )


def main():
    destination_repo = gh.get_repo(
        f"{settings.action_inputs.destination_owner}/{settings.action_inputs.destination_repo}"
    )
    with clone_dest_repo(destination_repo) as temp_dir:
        repo_dir = Path(temp_dir)
        try:
            git.init_project_git_user(repo_dir)
            copy_folder(repo_dir)
            commit_changes_to_branch(repo_dir)
            pr = issue_pr(destination_repo)
            if settings.action_inputs.pull_request_reviewers:
                pr.create_review_request(
                    reviewers=settings.action_inputs.pull_request_reviewers
                )
        except Exception as e:
            # delete new remote branch
            print("encountered exception, cleaning up")
            delete_remote_branch_head_branch(destination_repo)
            raise e


if __name__ == "__main__":
    main()
