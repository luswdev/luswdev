from wakatime import wakatime
from github import github

if __name__ == '__main__':
    wakatime_api = wakatime()
    stats = wakatime_api.get_stats()

    github_api = github()
    github_api.update_readme(stats)

