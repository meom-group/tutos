- 2 cases :
  - you have a fix PC with a fix IP -> you can connect directly to occigen, jupyter-notebooks will render smoothly
  - you have a portable PC with a variable IP -> you must connect to cal1 first then to occigen

- Make sure to add the options `-CX` (`-CXY` on MAC) when you ssh to cal1 and occigen, in order to have the pop-ups rendered (not only for notebooks but also ncview or display)

- When you are on occigen, you must know that `conda install` is not possible (the http server is blocked) only `pip install` is available. There are 2 solutions :
  - you ask svp@cines.fr to install you a conda environment with a list of libraries, and each time you want a new library (make sure to ask for jupyter !)
  - you use `conda-pack` to prepare you environment on your local machine and then export it on occigen via ssh
  
- You need firefox to render your jupyter notebook : so in your .bashrc put the line `module load firefox`

- Look for the file `/home/albert7a/.jupyter/jupyter_notebook_config.py`in your occigen account and modify the lines :
  - comment the line `c.NotebookApp.password = ...`
  - uncomment the line `c.NotebookApp.open_browser=True`
  
- If you want to use dask-jobqueue (you submit a job to get ressources)
  - you need to install the dask-jobqueue library
  - create a file like /home/albert7a/.config/dask/jobqueue.yaml where you write :
  
 ``` jobqueue:
   slurm:
     name: dask-worker
#     # Dask worker options
     cores: 28                 # Total number of cores per job
     memory: 20GB                # Total amount of memory per job
     processes: 28                # Number of Python processes per job
     interface: ib0             # Network interface to use like eth0 or ib0
     death-timeout: 60           # Number of seconds to wait if a worker can not find a scheduler
     local-directory: $SCRATCHDIR/daskjobqueue       # Location of fast local storage like /scratch or $TMPDIR
#     # SLURM resource manager options
     walltime: ‘00:30:00’
     job-extra: [--constraint=BDW28',--exclusive’]```

  - The syntaxe of the commands to put in the notebook is described here : https://github.com/auraoupa/Toolbox/blob/master/dask_ressources.ipynb
