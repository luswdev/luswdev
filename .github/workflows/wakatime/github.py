from re import sub
import requests

from formatter import formatter

class github:
    def __init__(self):
        self.formatter = formatter()

        TAG_NAME = "wakatime_gen"
        self.START_SECTION = f"<!--START_SECTION:{TAG_NAME}-->"
        self.END_SECTION = f"<!--END_SECTION:{TAG_NAME}-->"
        self.README_REGEX = f"{self.START_SECTION}[\\s\\S]+{self.END_SECTION}"

    def insert_stats(self, fmt_stats):
        README_PATH = 'README.md'

        with open(README_PATH, 'r') as readme_file:
            readme_contents = readme_file.read()
        readme_stats = f"{self.START_SECTION}\n{fmt_stats}\n{self.END_SECTION}"
        new_readme = sub(self.README_REGEX, readme_stats, readme_contents)

        with open(README_PATH, 'w') as readme_file:
            readme_file.write(new_readme)

    def update_readme(self, stats):
        languages = self.formatter.format_array(stats['languages'], ':hammer: Language Leaderboard')
        editors = self.formatter.format_array(stats['editors'], ':floppy_disk: Editor Leaderboard')
        oss = self.formatter.format_array(stats['operating_systems'], ':computer: Operating System Leaderboard')
        fmt_stats = languages + editors + oss
        self.insert_stats(fmt_stats)

