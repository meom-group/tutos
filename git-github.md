# How to use git and github to back up your work

## Create a project on github
 - create an account on [github](https://github.com) or on [GRICAD's gitlab](https://gricad-gitlab.univ-grenoble-alpes.fr/users/sign_in)
 - create a new repository or project, let's call it **my_work** as an example
 - you can add a description in the README.md file when creating the project
 - you can now add files directly on github/gitlab
 
 
## Add a ssh key for your machine
  - in order to be able to download and upload files to your github account from a specific machine, you have to set up a SSH key as described [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
  - on github, go to your settings and in the SSH and GPG keys section :
  
![pic](pics/ssh-key-github.png)

  - click on add a new key :

![pic](pics/new-ssh.png)

  - generate a ssh key by typing the ```ssh-keygen``` command in your terminal, and press enter to all questions, now you have a ```.ssh/id_rsa.pub```  :

![pic](pics/keygen.png)

  - copy the content of .ssh/id_rsa.pub and paste it in the Key field : 
  
![pic](pics/key.png)

  -  give a title to the key as you. will repeat the operation on every machine you will work on (cal1, dahu, supercomputers, etc ...)

## Clone your project on your machine

  - go back to your **my_work** repository on github and copy the SSH address :

![pic](pics/git-ssh.png)
