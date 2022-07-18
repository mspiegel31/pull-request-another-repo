#!/usr/bin/env python

import subprocess
from pathlib import Path

from github.Repository import Repository

from pr_another_repo.client import gh
from pr_another_repo.settings import settings


def clone_dest_repo(repo: Repository) -> Path:
    clone_url = repo.clone_url
    subprocess.run(["git", "clone", clone_url, "/tmp/destination_repo"])
    return Path("/tmp/destination_repo")


def issue_pr(repo: Repository):
    pass


def main():
    destination_repo = gh.get_repo(settings.action_inputs.destination_repo)
    # clone source
    # issue commit
    # issue pr
    local_repo_location = clone_dest_repo(destination_repo)
    issue_pr(destination_repo)


if __name__ == "__main__":
    main()
