# git-auto-mirror

### Description
This project intends to enable auto-mirroring across multiples git servers and repositories.
Push once and have you app in all git servers you want to

![image](https://user-images.githubusercontent.com/13976414/187053973-bbaec319-6561-4d1a-82fa-9ab7dace4346.png)

### Installing
Starting by cloning this repository

    > git clone https://github.com/mrotame/git-auto-mirror.git
    > cd git-auto-mirror
After that config a new python environment (from your preference)

    > virtualenv env
    > source env/bin/activate
    # "env/Scripts/activate" on windows
Finally, install all packages required to run this app

    pip install -r requirements.txt
Create a file named *repos.ini*at the main directory. this will be the file where we will configure the master repository and the slaves (that will receive the mirrored master repository)

    > touch repos.ini
    > nano repos.ini
The file must be filled in as follows:

    [DEFAULT]
    url = 'https://username:password@url_from_master_git_repository'
    
    [slave01]
    url = 'https://username:password@url_from_slave_01_git_repository'
    
    [slave02]
    url = 'https://authToken@url_from_slave_02_git_repository'

to start the app, run the file *app.py* in *src/* directory

    > python src/app.py
