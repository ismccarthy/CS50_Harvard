Git commands:
- git clone <url> : take a repository stored on a server (like GitHub) and downloads it

- git add <filename(s)> : add files to the staging area to be included in the next commit

- git commit -m "message" : take a snapshot of the repository and save it with a message about the changes

- git commit -am <filename(s)> "message" : add files and commit changes all in one

- git status : print what is currently going on with the repository

- git push : push any local changes (commits) to a remote server

- git pull : pull any remote changes from a remote server to a local computer

- git log : print a history of all the commits that have been made

- git reflog : print a list of all the different references to commits

- git reset --hard <commit> : reset the repository to a given commit

- git reset --hard origin/master : reset the repository to its original state (e.g. the version cloned from GitHub)