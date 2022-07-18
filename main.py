#!/usr/bin/env python

from pr_another_repo.client import gh
from pr_another_repo.settings import settings


def issue_pr():
    destination_repo = gh.get_repo(settings.action_inputs.destination_repo)


def main():
    # clone source
    # issue commit
    # issue pr

    issue_pr()


if __name__ == "__main__":
    main()
