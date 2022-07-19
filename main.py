#!/usr/bin/env python

import subprocess
from pathlib import Path
import shutil
import tempfile

from github.Repository import Repository

from pr_another_repo.client import gh
from pr_another_repo.settings import settings
from pr_another_repo import git

def clone_dest_repo(repo: Repository) -> tempfile.TemporaryDirectory:
    temp_dir = tempfile.TemporaryDirectory()
    clone_url = repo.clone_url
    subprocess.run(["git", "clone", clone_url, temp_dir.name], check=True)
    return temp_dir

def copy_folder(repo_dir: tempfile.TemporaryDirectory) -> Path:
    source_files = Path(__file__).parent.joinpath(settings.action_inputs.source_folder)
    dest_dir = Path(repo_dir.name) / settings.action_inputs.source_folder
    return shutil.copytree(source_files, dest_dir)



def create_branch(repo_dir: tempfile.TemporaryDirectory):
    print('TODO: create branch')
    

def issue_pr(repo: Repository):
    print('TODO: issue a PR')


def main():
    # git.init_git_user()
    destination_repo = gh.get_repo(settings.action_inputs.destination_repo)
    local_repo_location = clone_dest_repo(destination_repo)
    try: 
        copied_folder = copy_folder(local_repo_location)
        create_branch(copied_folder)

        issue_pr(destination_repo)
    finally:
        local_repo_location.cleanup()


if __name__ == "__main__":
    main()
