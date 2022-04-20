# How to compute on cal1

ige-meom-cal1.u-ga.fr is a virtual machine on which you can make small computations (10 cores, 32.6Gb memory) and store data (300Tb)

To prevent a user from using all the cores and/or all the memory, a job submission system has recently been set up.

Always indicate ```--account=fortran``` or ```--account=python``` depending on your type of scripts (bash scripts, nco commands are fortran-like ...)

## Job submission on the command line

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

An example of sequential job and parallel job.

## Jupyter notebooks
