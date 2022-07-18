#!/usr/bin/env python

from pr_another_repo.client import gh


def main():
    original_repo = gh.get_repo("mspiegel31/dotfiles")
    destination_repo = gh.get_repo("mspiegel31/dotfiles")


if __name__ == "__main__":
    main()
