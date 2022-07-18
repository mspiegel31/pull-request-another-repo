#!/usr/bin/env python

from pr_another_repo.client import gh


def main():
    r = gh.get_repo("mspiegel31/dotfiles")
    print(r)


if __name__ == "__main__":
    main()
