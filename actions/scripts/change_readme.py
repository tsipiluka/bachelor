import re

class WordCountUpdater:
    def __init__(self):
        self.word_count = 0
        self.table_fig_count = 0

    def update_word_count(self):
        with open('output.texcount', 'r') as file:
            contents = file.read()
            matches = re.finditer(r'Sum count: (\d+)', contents)
            last_match = None
            for match in matches:
                last_match = match
            if last_match:
                self.word_count = int(last_match.group(1))

    def update_table_fig_count(self):
        with open('output.texcount', 'r') as file:
            contents = file.read()
            matches = re.finditer(r'Number of floats/tables/figures: (\d+)', contents)
            last_match = None
            for match in matches:
                last_match = match
            if last_match:
                self.table_fig_count += int(last_match.group(1))

    def update_readme_file(self):
        with open('README.md', 'r') as file:
            readme_content = file.read()

        readme_content = re.sub(r'Anzahl%20Wörter-\d+', f'Anzahl%20Wörter-{self.word_count}', readme_content)
        readme_content = re.sub(r'Tabellen/Abbildungen-\d+', f'Tabellen/Abbildungen-{self.table_fig_count}', readme_content)

        with open('README.md', 'w') as file:
            file.write(readme_content)

    def run(self):
        self.update_word_count()
        self.update_table_fig_count()
        self.update_readme_file()
        print(self.word_count)
        print(self.table_fig_count)

updater = WordCountUpdater()
updater.run()