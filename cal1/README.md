# How to compute on cal1

## Description

ige-meom-cal1.u-ga.fr is a virtual machine on which you can make small computations (10 cores, 32.6Gb memory) and store data (300Tb)

If you have an IGE account, please ask Aurélie Albert or Jean-Marc Molines to give you acces to it.

## Access and workspaces

Then, you can access the machine with the command : ```ssh -CX yourlogin@ige-meom-cal1.u-ga.fr```

You will have access to 2 personnal workspaces : ```/home/yourlogin``` (automatically created) and ```/mnt/meom/workdir/yourlogin``` (create it yourself with mkdir in /mnt/meom/workdir), the first one is limited in space and you should only put scripts on it, the second is like a scratch where your temporary and results files should be stored.

You can see how much of these spaces are filled with the command ```df -h``` (look for /home and /mnt/meom to see how much space is left)

You can trasnfer data from your computer to cal1 with the command ```scp myfile yourlogin@ige-meom-cal1.u-ga.fr:/mnt/meom/workdir/yourlogin/where_you_want_it/myfile``` and you can download data from cal1 to your computer with the command : ```scp yourlogin@ige-meom-cal1.u-ga.fr:/mnt/meom/workdir/yourlogin/path_to_your_file/myfile .```

Some data are visible to anyone : ```/mnt/meom/DATA_SET``` and ```/mnt/meom/MODEL_SET```, a catalog will soon be available to see the details of all the datasets.

## Computation

To prevent a user from using all the cores and/or all the memory, a job submission system has recently been set up.

### Useful commands
 - the command ```htop``` will show you some indicators of the workload of the machine
 - Always indicate ```--account=fortran``` or ```--account=python``` depending on your type of scripts (bash scripts, nco commands are fortran-like ...)
 - When your job has been submitted :
    - command ```squeue```  : you see all the jobs on cal1 running or waiting
    - command ```scontrol show job JOBID``` : JOBID is the first item on squeue, you have all the informations about your job while it is waiting or running
    - command ```scancel JOBID``` : cancel the job
 
### Job submission on the command line

You can sum up all the infos in the job header into one single line of code : 

```
srun -n 1 --time=00:10:00 --mem=20000 --account=fortran YOURSCRIPT
```
 
### Job submission in a script

Set up a script job.ksh for instance in which the header must have the informations :

```
#!/bin/bash
#SBATCH -J cdfcurl_medwest
#SBATCH -n 1                       # nb of nodes, but only one is available on cal1
#SBATCH --ntasks=3                 # nb of tasks >1 if you have a parallelized script
#SBATCH -o cdfcurl_medwest_%J.out
#SBATCH -e cdfcurl_medwest_%J.err
#SBATCH --time=00:31:00            # hh:mm:ss
#SBATCH --mem=5000                 # memory = 5Gb
#SBATCH --account=fortran

Your script
```

An example of [sequential job](https://github.com/meom-group/tutos/blob/master/cal1/jobs/job_seq_compute_vorticity_MEDWEST60.ksh) and [parallel job](https://github.com/meom-group/tutos/blob/master/cal1/jobs/job_par_compute_vorticity_density_MEDWEST60.ksh).

You submit this script with the command ```sbatch job.ksh```

### Jupyter notebooks

  - load your conda environment in which jupyter is available (like the one defined [here](https://github.com/meom-group/tutos/blob/master/cal1/2020-03-20-AA-demo-dask-dashboard-xarray-on-cal1.ipynb) )
  - launch jupyter without browser with a job submission command : ```srun -n 1 --time=00:10:00 --mem=20000 --account=python jupyter notebook --no-browser --port 1234``` (be careful if port 1234 is not available, another one will be attributed)
  - in another terminal, make a tunnel to cal1 : ```ssh -NL 1234:localhost:1234 alberta@ige-meom-cal1.u-ga.fr``` (replace 1234 by the port given to you at the previous stage)
  - in your local machine, open your browser and look for : localhost:1234 and enter the token or copy paste the adress from the output of the jupyter notebook command

