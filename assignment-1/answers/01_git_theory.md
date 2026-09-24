### Git fundamentals

1. Git has three places a change can live: the working directory, the staging area, and the repository.
Describe each, and explain what you would lose if the staging area did not exist.
Ans: 
working directory is our system where we add/edit the files. git doesn't track it.
staging is a holding area which appears after we git add . in order to send our changes from working directory to git.
repository is the .git folder's permanent history which we can see in github as well and in our history by git log.
if there is no staging area then we will have to commit and push all the changes done in our working directory. Sometimes, we do not want to push everything in the same branch. So, staging is required.

2. git init and git clone both leave you with a Git repository. Explain what each one actually does,
and give a situation where each is the right choice.
Ans:
git init is creates new and empty .git folder in the folder which will have no history. It is good while starting a project from scratch. If you do git init in existing project then it will fix corruption, update existing history and branches. So, it is safe to do that.
git clone helps you get all the files and folders of repository in your system or working directory. We do this when we want to work on the existing remote repository.

3. What does a commit store, and why is "committing" not the same as "saving a file"? Why is Git much less useful if user.name and user.email are unset or wrong?
Ans:
Saving a file is just a overwrites its previous content. There is no record of what changed, when and why whereas in commit it staged files along with its author's name/email, timestamp and message. 
The author's name and email is the thing that helps us track the commit data which is gt by the user.name and user.email. So, it should be set else it won't be able to find the user trying to push the changes.

4. git status , git log , and git diff answer three different questions. State the question each one answers, and describe a moment in your workflow where you would reach for each.
Ans:
git status - is to see if there is any changes since our last commit.
git log - is to see commit history
git diff - is to see what changes has been made before the staging or commiting.

5. Explain what makes a commit message good. Why is "update" a genuine problem for a team six months later, and when is it worth writing a message body rather than just a summary line?
Ans:
A good commit message can explain why the changes was made. Just 'update' is a problem as it do not define what is updated properly which might take alot of time looking at the code to find what diff as been made.
When a one-line is not just enough to explain what changes has been done.

### Remotes and the everyday workflow

6. Explain the relationship between your local repository and origin. What do push and pull each move, in which direction, and why is pulling before pushing the habit to build?
Ans:
Origin is the default name of our remote copy on github. pull helps to get everything from the remote repo to our local and push helps in pushing our local staged changes to the github. Pulling is important so that our teammate's merged changes in our remote repo can come into our local. then, we can push our changes.

7. git fetch and git pull are not the same command. What is the difference, and when would you
deliberately choose fetch ?
Ans:
Fetch gets the remote's new commits into our local repo but doesn't make changes in our branch so that we can inspect what's new in remote before deciding what to do with it. Pull will get all kind of changes in our local or to other branches as well.

### Branching, merging, pull requests

8. A branch in Git is often described as "just a pointer." Explain what that means, and explain concretely
what goes wrong on a team when everyone commits directly to main .
Ans:
If all teammembers start to commit to main then our local won't have changes of main and won't be able to push our changes. Creating a branch helps us manage changes in merging main properly.

9. A merge conflict happens when two branches change the same lines of the same file. Explain why Git
cannot resolve this automatically, what the <<<<<<< , ======= , >>>>>>> markers mean, and what you
must do to finish the merge.
Ans:
It shows our changes and our team-member's changes. So that we can see what to keep our change, their change or both of the changes. Git cannot do it as it won't know what to keep.

10. You could merge a branch locally with git merge and push. What does opening a Pull Request add
that a local merge does not? What belongs in a PR description?
Ans:
We could but opening pull request will show us if there is pull request it will show us comparison to our merging branch, write good description, have reviews by team members.

### Issues
11. Explain the purpose of labels and assignees on an Issue, and what Fixes #12 in a merged PR does.
Why is linking work to Issues better than closing them by hand?
Ans:
label catgories an issue as bug, feature, chore etc so that we can filter it.
assignee shows who is responsible for working on it, so nothing falls out of the no owner.
fixes #12 bind issue #12 with the pull-request then after mergin gthe pull-request, the issue is automatically closed.

### Project structure, environments, secrets

12. Why should .gitignore be one of your first commits? If a file is already tracked, does adding it to
.gitignore stop Git from tracking it — and if not, what do you do instead?
Ans:
.gitignore has list of file or folders name which will be ignored by the github like __pycache__/, .env. 

13. Explain the difference between .env and .env.example , and why they get opposite treatment. If a real
API key was committed three weeks ago, why is deleting it in a new commit not a fix, and what should
actually be done?
Ans:
.env will have secret keys and .env.example have same key but with pseudo values to it. .env.example is the skeleton to .env to be used by team-members. Even if we remove it in new commit, it will be there in old commits. We should rotate/revoke the leaked key immediately and scrub it from history.

14. What problem do a virtual environment and requirements.txt solve together? Why is venv/ itself
never committed, when requirements.txt always is?
Ans:
virtual environment is os/machine-specific and fully reconstructable which to be generate using requirements.txt and requirements.txt is created using venv with a command. venv is a large folder to commit whose smaill, portable part is requirements.txt

15. Explain what git push --force does to a shared branch and whose work it can destroy. How does --
force-with-lease behave differently, and why is that safer?
Ans:
git push --force overwrites the remote branch's histrory with our local version unconditionally. it will wipes all the commits from the remote if our local don't have it.
--force-with-lease checks first whether the remote branch has changd since you last fetched. If someone else has pushed in the meantime, it refuses to push and fails safely. That is why, its safer.

