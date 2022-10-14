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
 -  press ENTER, read and accept the licence (press bar space and type yes), specify the location for miniconda3 to install all the librairies, be careful to indicate a location where the quotas are not very constraint, for instance not on the home of computing servers as they usually accept only a few Gb of memory, on cal1, specify a location in your workdir like : ```/mnt/meom/workdir/yourlogin/miniconda3```
 -  this installation has modified your .bashrc so you need to source it ```source /home/username/.bashrc```, or deconnect and connect again to your machine
 -  you now see the (base) mention at the beginning of the prompt, that means that you are in your base environment, the command ```conda list``` shows you the already installed libraries and the version of it (doing it in 2022, October the 14th it will install the 3.9.12 version of python)
 -  now you can install additional librairies with the command ```conda install library```but we recommend that you create an environment first

## Create a conda environment

Managing your libraries via an environment allows you to deal with incompatible librairies, incompatible versions of libraries or just to separate the downloading of libraries by project or type of workflows

  - create an environment with a specific version of python and some useful libraries for plotting data in a jupyter notebook : ```conda create --name plots python=3.5 numpy matplotlib cartopy xarray dask netcdf4 ipykernel jupyter pandas``` it will also install all the dependencies needed by those libraries
  - activate the environment with : ```conda activate plots```, now you have access to all the libraries installed, try ```python -c "import matplotlib"``` for instance to check
  - ```conda list``` will also give you the list of all the libraries for this environment
  - you can install extra libraries in this environment with the command ```conda install```, for instance we are adding the very useful cmocean library for plotting oceanic data : ```conda install -c conda-forge cmocean```, this library is only available in the conda-forge channel so we have to specify it
  - if you create several environments you can check them with the command : ```conda info --envs```, it will tell you where it is stored and which one is activated 
  - you can delete the environment by deleting the repository : ```rm -rf /mnt/meom/workdir/username/miniconda3/envs/plots``` for instance or with the command ```conda remove --name plots --all```

## Make a requirement file

- You can also create an environment from a yaml file in which you specify all the libraries you need. This requirement file env.yml must look like :

```yaml
name: plots
channels:
  - conda-forge
dependencies:
  - python=3.5
  - numpy 
  - matplotlib 
  - cartopy 
  - xarray
  - dask
  - netcdf4
  - ipykernel
  - jupyter
  - pandas
  - cmocean
```

- Then you create the environment with the command : ```conda env create -f env.yml```
- Now if you want to share your code it is recommended that you share the list of libraries needed to make it run by adding this env.yml file to your python script.

More informations about conda environments can be found [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)

