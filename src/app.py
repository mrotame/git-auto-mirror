import subprocess
from typing import List
import os
from git import Repo
from reposInfo import ReposInfo
import time
from git.exc import NoSuchPathError

class App():
    reposInfo: ReposInfo = ReposInfo()
    master: Repo
    parent_path = os.path.join('src','repos')
    branches_outdated: List[str] = []

    def __init__(self):
        self.baixarMaster()
        self.ativaGitMaster()
        while True:
            self.baixarTodasAsBranches(self.master)
            self.atualizaMaster()  
            self.publicaParaSlaves()  
            time.sleep(5)

    def baixarMaster(self)->None:
        caminho = os.path.join(self.parent_path, self.reposInfo.repo_master['name'])
        if self.verificaSeGitJaExiste(caminho) == True:
            self.master = Repo(caminho)
            return
        self.master = Repo.clone_from(self.reposInfo.repo_master['settings']['url'], caminho, branch='main')
        self.baixarTodasAsBranches(self.master)

    def ativaGitMaster(self)->None:
        os.chdir(os.path.join(self.parent_path, self.reposInfo.repo_master['name']))

    def baixarTodasAsBranches(self, repo: Repo)->None:
        for b in repo.remote().fetch():
            repo.git.checkout('-B', b.name.split('/')[1], b.name)
        #repo.git.checkout(self.reposInfo.repo_master['settings']['main_branch_name'])

    def verificaSeGitJaExiste(self, caminho:os.path)->bool:
        try:
            repo = Repo(caminho)
            return not repo.bare
        except NoSuchPathError:
            return False

    def atualizaMaster(self)->None:
        self.master.git.pull()

    def publicaParaSlaves(self)->None:
        for repo in self.reposInfo.repo_list:
            process = subprocess.run(["git", "push",'--mirror',self.reposInfo.repo_list[repo]['url']], stdout=subprocess.PIPE)


if __name__ == "__main__":
    App()

