Before play around, give commit a branch. 

Checkout hash and make branch: 
branch is just a pointer to a commit (that moves to the new commit when you commit to that branch)

commits that have no pointers to them (in the form of a branch, tag, or child commit(s)) are the ones that go away during garbage collection
So... "git reflog" to find the commit, "git branch foobar1 <hash1>" to give names to the hashes. Then "gitk --all" to see how everything is connected, and then inspect stuff.

I try to use "git fetch -v --all", then inspect "gitk --all", and then I decide whether to merge or rebase or whatever.