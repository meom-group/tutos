# How to compute on Adstra machine

To connect to Adastra, ssh to adastra.cines.fr :

```$ ssh <login>@adastra.cines.fr```

You have only one login but maybe mutliple projects :

 - ```myproject -l```will list them
 - ```myproject -a ige2071``` will load the environment variables for this project
 - ```myproject -c``` will show you all the path (you need to load a project first)
 - ```myproject -s <project_id>```will show the quota for one project, ```myproject -S``` for all your projects

Look for a module and dependencies : ```module spider netcdf```

Aliases and module loading can be defined in a .bash_profile file


module load conda/22.9.0


