"""Helper functions for working with git on local filesystem"""
from pathlib import Path
import subprocess

from pr_another_repo.settings import settings


def init_project_git_user(directory: Path):
    git_user = settings.action_inputs.user_name
    git_email = settings.action_inputs.user_email
    subprocess.run(["git", "config", "user.name", git_user], check=True, cwd=directory)
    subprocess.run(["git", "config", "user.email", git_email], check=True, cwd=directory)
