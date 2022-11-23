# Some informations regarding the irene machine at TGCC

Most of the information can be consulted on irene once loggued in using `irene.info` at command prompt.

## Login and projects
  Each user has a unique login name, eventually shared between various projects.
In addition, apart from the projects, a user has a main group coresponding to the lab it belongs to. 
Example: all users having an account on irene at IGE belong to the same group `ige` independently to the 
reseach team it belongs to.  As a consequence, within a project 2 users from 2 different lab (ie IGE, LOPS) 
have different main group.... This needs to be clear in the mind for those working on irene. TGCC implements a series 
of customized command `ccc_xxx` as well as specific environment variables `CCCxxxx` aiming at simplifying the work on irene.
### Connecting to irene
Connection is **only possible**  from the machines declared at TGCC, when creating the user account. Connection is done via SSH :

```
   ssh <USER>@irene-fr.ccc.cea.fr
```

Password is mandatory, SSH keys exchange is not implemented.

## The different workspaces
### HOME :
  * When login, we are dropped in $HOME, which is the HOME corresponding to the main group (lab group, *i.e.* `ige`). The `.bashrc` and related 
files in this HOME are used at initialization of the shell.
  * For a particular project, there is a specific HOME directory, associated to `CCCHOME` environment variable. This latter environment variable
is set when loading a specific project module called `dfldatadir/<PROJECT>`(<PROJECT> is the project ID, *e.g.* gen12020, currently).  
If the module is not loaded, then CCCHOME points to HOME.

Note that it is important to load the project module not only for the HOME but for all the other workspaces, where quota can be an issue.
### WORK :
  * Mid-term personal workspace for big data with back-up.
  * Always associated to a project (after `module load dfldatadir/<PROJECT>`). The path is `$CCCWORKDIR`

### SCRATCH :
  * Faster temporary personal workspace for big data, no back-up, accessible from jobs
  * Always associated to a project (after `module load dfldatadir/<PROJECT>`). The path is `$CCCSCRATCHDIR`

### STORE :
  * Long-term storage of archived data. Although it is transparent to the user, files on STORE are migrated to tapes (via DMF), and it is
very important to minimize the number of files by concatenation of files or by making big tar files of full directories. When files are
migrated on tape, they need to be re-hydrated to disk before use, and this may take a lot of time if there are thousands of small files.
  * Always associated to a project (after `module load dfldatadir/<PROJECT>`). The path is `$CCCSTOREDIR`
  * Specific commands for DMF management:
    * lfs hsm_state <file > : give the status of a file regarding the migration on tape. If migrated, file state is `released`.
    * lfs hsm_action <file> : indicates if there is an on-going action on file : can be NOOP or RESTORE.
    * lfs hsm_restore <file> : Rehydrate file on disk. Note that rehydration is done in background, and the number of simultatneous rehydratation is limited. (Need to repeat the hsm_restore command).

Workflow should be : storage of inputs and results on WORK as long as you need, intermediate files stored on SCRATCH, long-term archives of results on STORE 
### Quotas 
  * quotas can be monitored using the `ccc_quota` command.   Note that on STORE there is only a quota for the number of inodes.

## The different partitions of irene
Below the name **irene** there are in fact various computers (partition)  with different architecture. A given project has only access to the 
partition it has hours granted on. As of Oct. 2022, we have access to the **rome** partition, each compute node having 128 cores.

## Computing hours
  Computing hours are obtained by submitting a scientific/technical proposal to GENCI via the DARI interface. Once approved, users can check the project
consumption with the `ccc_myproject` command. 

## Job submission
Apart from compilation and short scripts tests, the right way to use irene ressources is through the batch system (SLURM derived). Jobs must be submitted with
the `ccc_msub <batch_file>` command, using a batch file. The batch file must have a header part with some #MSUB directives like in the following example:

```
#!/bin/bash

#MSUB -r  name                # Request name                     
#MSUB -n  128                 # Number of tasks to run            
#MSUB -N  1                   # Number of nodes to use          
#MSUB -T 3600                 # Elapsed time limit in seconds   
#MSUB -o zname.o%I            # Standard output. %I is the job id
#MSUB -e zname.e%I            # Error output. %I is the job id   
#MSUB -q rome                 # pqrtition  name                                   
#MSUB -A gen12020             # Project ID for accounting       
#MSUB -x                      # exclusve compute node
#MSUB -m store,work,scratch   # list the file system used by the job
### COMMENT :   There are 128 core per node on rome nodes

```

For parallel computing, executable must be launched with the `ccc_mprun` command (a wrapper for slurm `srun`). See details in the `irene.info` documentation.

`ccc_msub` does not allow to pass argument to the batch script, in contrary to `sbatch`. A workaround for this limitation is to use a template script where some
parameters can be changed usig `sed` for instance. See this [example](restore_occi.sh) for instance.


