# Git CMS 

**Commands for First Setup**

```shell
git config --global user.name "FIRST_NAME LAST_NAME" # set your username 
git config --global user.email "MY_NAME@example.com" # set your email 
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # generate key-pair
 eval "$(ssh-agent -s)" # add keys into agent
cd ~/.ssh & cat id_rsa.pub # show public key, then copy-past it into your github profile 
```

**Commands for commit / push etc. operations**

```shell
git add -A # add all the files & changes, local repo 
git commit -m "My commit message, e.g. added new functionality" # commit, local repo
git push origin <BRANCH_NAME> # push to remote repository all the changes made in local 
```

