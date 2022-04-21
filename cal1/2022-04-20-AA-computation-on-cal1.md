# How to compute on cal1

ige-meom-cal1.u-ga.fr is a virtual machine on which you can make small computations (10 cores, 32.6Gb memory) and store data (300Tb)

To prevent a user from using all the cores and/or all the memory, a job submission system has recently been set up.

## Useful commands

 - Always indicate ```--account=fortran``` or ```--account=python``` depending on your type of scripts (bash scripts, nco commands are fortran-like ...)
 - When your job has been submitted :
    - command ```squeue```  : you see all the jobs on cal1 running or waiting
    - command ```scontrol show job JOBID``` : JOBID is the first item on squeue, you have all the informations about your job while it is waiting or running
    - command ```scancel JOBID``` : cancel the job
      
## Job submission in a script

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

## Job submission on the command line

You can sum up all the infos in the job header into one single line of code : 

```
srun -n 1 --time=00:10:00 --mem=20000 --account=fortran YOURSCRIPT
```


## Jupyter notebooks

  - load your conda environment in which jupyter is available (like the one defined [here](https://github.com/meom-group/tutos/blob/master/cal1/2020-03-20-AA-demo-dask-dashboard-xarray-on-cal1.ipynb)
  - launch jupyter without browser with a job submission command : ```srun -n 1 --time=00:10:00 --mem=20000 --account=python jupyter notebook --no-browser --port 1234```
  - in another terminal, make a tunnel to cal1 : ```ssh -NL 1234:localhost:1234 -L 8787:localhost:8787 alberta@ige-meom-cal1.u-ga.fr```
  - in your local machine, open your browser and look for : localhost:1234
  - enter the token given in cal1 (or copy paste the address)

