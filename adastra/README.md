# How to compute on Adstra machine

## Connexion

To connect to Adastra, ssh to adastra.cines.fr :

```$ ssh <login>@adastra.cines.fr```

## Projects

You have only one login but maybe multiple projects :

 - ```myproject -l```will list them
 - ```myproject -a project``` will load the environment variables for this project (MEOM's project : hmg2840 (active), ige2071 (archive))
 - ```myproject -c``` will show you all the path (you need to load a project first)
 - ```myproject -s <project_id>```will show the quota for one project, ```myproject -S``` for all your projects

## Workspaces

On adastra, there are 4 types of space :
  - your home (/lus//home/CT1/project/login), limited to 110G 330 000 files
  - your scratch (/lus/scratch/CT1/project/login), temporary space (purged every month), limited to 110 Tb 1 100 000 files in total for hmg2840 group
  - your scratch (/lus/work/CT1/project/login), working space (purged every month), limited to 755 Tb 500 000 files in total for hmg2840 group
  - your store ( /lus/store/CT1/project/login ), archive space, limited to 19 000 000 files in total for hmg2840 group (no limitations on the size)

## Modules

Look for a module and dependencies : ```module spider netcdf```

Some useful modules to load (you may need to load dependencies) :
  - ```module load PrgEnv-intel```
  - ```module load conda/22.9.0```
  - ```module load cdo``` 

## Intel environment

There are no default module to load hdf5 and netcdf compiled with intel so you have to do it by hand :

  - this [tar file](https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/alberta/catalog.html) contains the libraries you need, put it somewhere on adastra
  - this [script](source.me) needs to be modified according to where you put the library and sourced in your .bashrc

