#!/usr/bin/python3
# 100-github_commits.py
# @tonybnya
"""
This python script lists 10 commits (from the most recent to oldest)
of the repository 'rails' by the user 'rails'.
The script uses the GitHub API.
Here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


def main():
    """ Main function """
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    json = requests.get(url).json()

    print(json)


if __name__ == '__main__':
    main()
