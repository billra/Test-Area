Docs for learning git
  http://progit.org/book/

git add [file]				initial add (also used for staging changes)
git status
git diff 				to see what is unstaged
git diff --staged			to see what is staged
git add [file]				stage change for next commit
git commit				commit staged changes
git commit -a -m 'some comment'		skip staging, checkin with comment
git log					show history
gitk					gui tool to show history

updating the original repository:
git status
# Your branch is ahead of 'origin/master' by 2 commits.
git push -u origin master


flow: (when not using staging)
  git add {some files} - to do the initial add
  git diff - to see local changes
  git commit -a -m 'some comment' - checkin with comment (skip staging)
  git status - see local vs remote
  git push -u origin master - update the remote

Troubleshooting:
  http://www.webbykat.com/content/fixing-connection-refused-error-message-when-pushing-git
  http://stackoverflow.com/questions/2122465/ssh-cannot-authenticate-to-gitgithub-com "Agent admitted failure to sign using the key." 

