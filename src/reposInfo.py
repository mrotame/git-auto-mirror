import configparser
import os
from typing import Dict

class ReposInfo():
    config = configparser.ConfigParser()
    repo_list: Dict = {}
    repo_master: Dict = {}

    def __init__(self):
        self.config.read(os.environ.get('repos_settings_path','repos.ini'))
        for sect in self.config:
            if sect == 'DEFAULT':
                self.repo_master['name'] = sect 
                self.repo_master['settings'] = dict(self.config.items(sect))
            else:    
                self.repo_list[sect] = dict(self.config.items(sect))
    

if __name__ == "__main__":
    print(ReposInfo().repo_master)
    print(ReposInfo().repo_list)
    
    
