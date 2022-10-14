# How to use conda to manage your python libraries

## Table of contents

1. [Install conda](#install-conda)
2. [Create a conda environment](#create-a-conda-environment)
3. [Make a requirement file](#make-a-requirement-file)

## Install conda

We are going to install [miniconda](https://docs.conda.io/en/latest/miniconda.html), the free minimal installer for conda because it is faster and takes less disk space, but feel free to install [Anaconda](https://www.anaconda.com/) if you have time and space !

 - check [this webpage](https://docs.conda.io/en/latest/miniconda.html) to know which installer you need, depending on which machine you want to install it on, get the link by right-clicking on it and press save link address
 - log in to the machine, and retrieve the chosen installer : ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```  for instance
 -  make it an executable : ```chmod +x https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```
 -  execute it : ```./Miniconda3-latest-Linux-x86_64.sh```
 -  press ENTER, read and the licence (press bar space and type yes), specify the location for miniconda3 to install all the librairies, be careful to indicate a location where the quotas are not very constraint, like homes of computing serverd as they usually accept only a few Gb of memory, on cal1 specify a location in your workdir like : ```/mnt/meom/workdir/yourlogin/minconda3```

## Create a conda environment

## Make a requirement file
