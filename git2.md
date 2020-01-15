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
```shell
$ git commit #to commit
$ git commit -m "message_to_attach" #to commit with inline message
$ git commit -a #to add then commit 
$ git commit [-a -m|-am] "message_to_attch" #to add then commit with inline message
<<<<<<< HEAD

```
Remember that anything that is still unstaged—any files you have created or modified that you haven’t run git add on since you edited them—won’t go into this commit.
### Removing Files
```shell
$ rm file_name # to remove from working directory
$ git rm file_name # to stage file removal
$ git rm file_name -f # to force file removal if the file has been modified and stagged
$git rm file_name --cached # to keep the file in your working tree but remove it from your staging area
We can use file_name|directory|glob_pattern as:
$ git rm log/\*.log
```
### Moving Files
```shell
$git mv file_from file_to
This is equivalent to
$ mv file_from file_to
$ git rm file_from
$ git add file_to
```
### Viewing the Commit History
```shell
$ git log
$ git log -p -2 # -p(patch) shows the differences and -2 limit entries to 2
This is very helpful for code review or to quickly browse what happened during a series of commits that a collaborator has added. 
$ git log --stat #  to see some abbreviated stats for each commit
$ git log --pretty=oneline
$ git log --pretty=format:"%h - %an, %ar : %s"  
#%H Commit hash
#%h Abbreviated commit hash,
#%T Tree hash 
#%t Abbreviated tree hash 
#%P Parent hash 
#%p Abbreviated parent hash,
#%an Author name
#%ae Author e-mail
#%ad Author date

=======

```
Remember that anything that is still unstaged—any files you have created or modified that you haven’t run git add on since you edited them—won’t go into this commit.
### Removing Files
```shell
$ rm file_name # to remove from working directory
$ git rm file_name # to stage file removal
$ git rm file_name -f # to force file removal if the file has been modified and stagged
$git rm file_name --cached # to keep the file in your working tree but remove it from your staging area
We can use file_name|directory|glob_pattern as:
$ git rm log/\*.log
```
### Moving Files
```shell
$git mv file_from file_to
This is equivalent to
$ mv file_from file_to
$ git rm file_from
$ git add file_to
```
### Viewing the Commit History
```shell
$ git log
$ git log -p -2 # -p(patch) shows the differences and -2 limit entries to 2
This is very helpful for code review or to quickly browse what happened during a series of commits that a collaborator has added. 
$ git log --stat #  to see some abbreviated stats for each commit
$ git log --pretty=oneline
$ git log --pretty=format:"%h - %an, %ar : %s"  
#%H Commit hash
#%h Abbreviated commit hash,
#%T Tree hash 
#%t Abbreviated tree hash 
#%P Parent hash 
#%p Abbreviated parent hash,
#%an Author name
#%ae Author e-mail
#%ad Author date

$git log --graph #--graph. This option adds a nice little ASCII graph showing your branch and merge history
```
|Option |Description|
|----|----|
|-p|Show the patch introduced with each commit.|
|--stat|Show statistics for files modified in each commit.|
|--shortstat|Display only the changed/insertions/deletions line from the --stat command.|
|--name-only|Show the list of files modified after the commit information.|
|--name-status|Show the list of files affected with added/modified/deleted information as well.|
|--abbrev-commit|Show only the first few characters of the SHA-1 checksum instead of all 40.|
|--relative-date|Display the date in a relative format (for example, “2 weeks ago”) instead of using the full date format.|
|--graph|Display an ASCII graph of the branch and merge history beside the log output.|
|--pretty|Show commits in an alternate format. Options include oneline, short, full, fuller, and format (where you specify your own format).|
### Limiting Log Output
```shell
$ git log --since=2.weeks #time limit
$ git log --Sfunction_name #takes a string and only shows the commits that introduced a change to the code that added or removed that string.
```
|Option|Description|
|-(n)|Show only the last n commits|
|--since, --after|Limit the commits to those made after the specified date|
|--until, --before|Limit the commits to those made before the specified date|
|--author|Only show commits in which the author entry matches the specified string|
|--committer|Only show commits in which the committer entry matches the specified string|
|--grep|Only show commits with a commit message containing the string|
|-S|Only show commits adding or removing code matching the string|
Example
```shell
$ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" --before="2008-11-01" --no-merges -- t/
```
## Undoing Things
```shell
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend # to add stages files to the last commit not a new commit
```

