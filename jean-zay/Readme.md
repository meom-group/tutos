# Some informations regarding the Jean-Zay machine at IDRIS

Most of the informations are gathered [here](http://www.idris.fr/jean-zay)

## The different workspaces
  
see http://www.idris.fr/jean-zay/cpu/jean-zay-cpu-calculateurs-disques.html

  - $HOME : personnal home space with back-up, 3Go, check quota with `idrquota -m`
  - $WORK : mid-term personnal workspace for big data with back-up, accessible from jobs, quota by project check with `idrquota -w -p project`
  - $SCRATCH : faster temporary personnal workspace for big data, no back-up, accessible from jobs, no quota. **CAUTION:** files are automatically deleted after one month. Long term files must be copied either on WORK or STORE (or both).
  - $STORE : long-term storage of archived data (tar), no back-up, not accessible from jobs, quota by project with `idrquota -s -p project`

Workflow should be : storage of inputs and results on $WORK as long as you need, intermediate files stored on $SCRATCH, long-term archives of results on $STORE

All the quotas at once : `idr_quota_user`and `idr_quota_project`

## Multi-projects

see http://www.idris.fr/jean-zay/cpu/jean-zay-cpu-doc_multi_projet.html

- To see your projects : `idrproj`
- To change the default project : `idrproj -d grp1`
- To change the active project : `eval $(idrenv -d grp1)`

Be careful, switching projects will change the env variables $HOME, $SCRATCH, $WORK and $STORE

## Computing hours

see http://www.idris.fr/jean-zay/cpu/jean-zay-cpu-doc_account.html

  - to check all your projects consumption : `idracct`
  
## Conda environment

- Conda is already installed on jean-zay, you can activate one of the pre-existing environment via the `module load python=version` command (see all the versions available with `module avail python`)

- You can then create your own environment, that will create a .conda repository in your $HOME, you better move it to your $WORK and make a link, because it will increase in size and inode quite rapidly

