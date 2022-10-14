# How to use git and github to back up your work

## Create a project on github
 - create an account on [github](https://github.com) or on [GRICAD's gitlab](https://gricad-gitlab.univ-grenoble-alpes.fr/users/sign_in)
 - create a new repository or project, let's call it *my_work* as an example
 - you can add a description in the README.md file when creating the project
 - you can now add files directly on github/gitlab
 
 
## Clone the project on any machine
  - in order to be able to download and upload files to your github account from a specific machine, you have to set up a SSH key as described [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
  - on github, go to your settings and in the SSH and GPG keys section
  
![pic](pics/ssh-key-github.png)
