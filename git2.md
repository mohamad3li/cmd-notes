## Getting a Git Repository
### Initializing a Repository in an Existing Directory
```shell
$ git init #To create the .git directory
$ git add [file_name|regex|.] # To begin tracking the files
$ git commit -m "message" # To commit stagged files
```
### Cloning an Existing Repository
```shell
$ git clone [url] [optional_dir_name]#Every version of every file for the history of the project is pulled down by default
e.g.
$ git clone https://github.com/libgit2/libgit2
$ git clone https://github.com/libgit2/libgit2 mylibgit
```
Git has a number of different transfer protocols you can use. 
- https:// protocol
- git:// protocol
- user@server:path/to/repo.git, which uses the SSH transfer protocol
### Recording Changes to the Repository
Each file in your working directory can be in one of two states: 
- tracked: files that were in the last snapshot; they can be unmodified, modified, or staged
- untracked: files in your working directory that were not in your last snapshot and are not in your staging area
![alt text](https://raw.githubusercontent.com/mohamad3li/notes/master/stages.png)

