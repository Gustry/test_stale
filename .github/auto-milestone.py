import sys
from typing import Optional

import requests
from pkg_resources.extern import packaging


def parse_branch(branch: str, milestones_available: list) -> Optional[packaging.version.Version]:
    """ Returns the milestones available according to the branch name, otherwise None. """
    if branch == 'master':
        return milestones_available[-1]

    try:
        branch = branch.replace('release-', '').replace('_', '.')
        branch = packaging.version.Version(branch)
        for m in milestones_available:
            if m.major == branch.major and m.minor == branch.minor:
                return m
    except Exception as e:
        print(e)


def all_gh_milestones(token: str, owner: str, repo: str):
    r = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/milestones",
        headers={
            'Authorization': f'Bearer {token}'
        }
    )
    milestones = r.json()
    github_valid_milestones = []
    for m in milestones:
        if len(m['title'].split('.')) != 3:
            continue

        try:
            github_valid_milestones.append(packaging.version.Version(m['title']))
        except packaging.version.InvalidVersion:
            continue
    github_valid_milestones.sort()
    return github_valid_milestones, milestones


if __name__ == "__main__":
    args = sys.argv[1:]
    gh_milestones, gh_milestones_object = all_gh_milestones(token=args[0], owner=args[1], repo=args[2])
    final_milestone = parse_branch(args[3], gh_milestones)

    milestone_id = None
    for milestone in gh_milestones_object:
        if milestone['title'] == str(final_milestone):
            milestone_id = milestone['number']
            break

    if not milestone_id:
        exit(0)

    print(milestone_id)
