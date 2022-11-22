# Some informations regarding the irene machine at TGCC

Most of the information can be consulted on irene once loggued in using `irene.info` at command prompt.

## Login and projects
  Each user has a unique login name, eventually shared between various projects.
In addition, apart from the projects, a user has a main group coresponding to the lab it belongs to. 
Example: all users having an account on irene at IGE belong to the same group `ige` independently to the 
reseach team it belongs to.  As a consequence, within a project 2 users from 2 different lab (ie IGE, LOPS) 
have different main group.... This needs to be clear in the mind for those working on irene. TGCC implements a series 
of customized command `ccc_xxx` as well as specific environment variables `CCCxxxx` aiming at simplifying the work on irene.
  ### conecting to irene
Connection is **only possible**  from the machines declared at TGCC, when creating the user account. Connection is done via SSH :

```
   ssh <USER>@irene-fr.ccc.cea.fr
```

Password is mandatory, SSH keys exchange is not implemented.

## The different workspaces

  - $HOME : personnal home space with back-up, 3Go, check quota with `idrquota -m`
  - $WORK : mid-term personnal workspace for big data with back-up, accessible from jobs, quota by project check with `idrquota -w -p project`
  - $SCRATCH : faster temporary personnal workspace for big data, no back-up, accessible from jobs, no quota
  - $STORE : long-term storage of archived data (tar), no back-up, not accessible from jobs, quota by project with `idrquota -s -p project`

Workflow should be : storage of inputs and results on $WORK as long as you need, intermediate files stored on $SCRATCH, long-term archives of results on $STORE

All the quotas at once : `idr_quota_user`and `idr_quota_project`

## The different partitions of irene
Below the name **irene** there are in fact various computers (partition)  with different architecture. A given project has only access to the 
partition it has hours granted on. As of Oct. 2022, we have access to the rome partition, each compute node having 128 cores.


## Multi-projects

## Computing hours

## Conda environment

