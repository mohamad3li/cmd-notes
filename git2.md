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
![file stages in git](https://raw.githubusercontent.com/mohamad3li/notes/master/stages.jpg)
### Checking the Status of Your Files
The main tool you use to determine which files are in which state is the git status command
```shell
$ git status
```
### Tracking New Files
```shell
$ echo 'My Project' > README
$ git status
$ git add README # this will add README to the staging area
$ git status
#
```
### Staging Modified Files
```shell
$ git add [files_to_be_staged]
```
git add is a multipurpose command—you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as “add this content to the next commit” rather than “add this file to the project”
### Short Status
```shell
$ git status -s | git status --short
```
- ??: New files that aren’t tracked
- A: new files that have been added to the staging area
- M: modified files
- left hand column: indicates that the file is staged
- right hand column: indicates that it’s modified
### Ignoring Files
We may hava class of files that you don’t want Git to automatically add or even show you as being untracked.we can create a file listing patterns to match them named .gitignore.

The rules for the patterns you can put in the .gitignore file are as follows:

- Blank lines or lines starting with # are ignored.
- Standard glob patterns work.
- We can end patterns with a forward slash (/) to specify a directory.
- We can negate a pattern by starting it with an exclamation point (!).

Here is an example .gitignore file:
```shell
# a comment - this is ignored
*.a       # no .a files
!lib.a    # but do track lib.a, even though you're ignoring .a files above
/TODO     # only ignore the root TODO file, not subdir/TODO
build/    # ignore all files in the build/ directory
doc/*.txt # ignore doc/notes.txt, but not doc/server/arch.txt
```

Viewing Your Staged and Unstaged Changes
```shell
$ git diff #To see what you’ve changed but not yet staged
$ git diff --staged #To compare your staged changes to your last commit
```
### Committing Your Changes

