## How to run a jupyter notebook in the visualization process

CINES offers a visualization tool in order to run for instance jupyter notebooks remotely on a dedicated node.

The steps are described here : https://www.cines.fr/calcul/materiels/visualisation/sessions-interactives-vnc/

Practically for us the steps will be :

  - log in visu.cines.fr (first to cal1 if you are at home)
  - type the command ```vizalloc -m vnc```, it will launch a job on the VISU nodes (not possible if you already have a job running ...), you can check it with the command vizqueue
  - a node has been allocated to you for instance visu2.cines.fr:1
  - log in to this node with ```ssh visu2.cines.fr```for instance, and there navigate to your directories and launch a ```jupyter notebook --no-browser```
  - in a separate terminal, log to cal1 and launch vncviewer
  - enter the node you have been granted, for instance visu2.cines.fr:5901, then your login and password, you now have access to a virtual desktop in which you can launch a browser (type firefox in a terminal)
  - in the browser enter the notebook address you were given when you launched it, no copy-paste allowed so be careful with the syntax of the token !!
 
## How to run a jupyter notebook directly on occigen

- 2 cases :
  - you have a fix PC with a fix IP -> you can connect directly to occigen, jupyter-notebooks will render smoothly
  - you have a portable PC with a variable IP -> you must connect to cal1 first then to occigen

- Make sure to add the options `-CX` (`-CXY` on MAC) when you ssh to cal1 and occigen, in order to have the pop-ups rendered (not only for notebooks but also ncview or display) or you can open a [VNC interactive session](https://www.cines.fr/en/supercomputing-2/hardwares/vizualisation/vnc-interactive-sessions/) for the pop up.

- When you are on occigen, you must know that `conda install` is not possible (the http server is blocked) and only `pip install` is available. There are 2 solutions:
  - Ask svp@cines.fr to install you a `conda` environment with a list of libraries, and each time you want a new library installed (make sure to ask for `jupyter` or `jupyterlab`!)
  - Use [`conda-pack`](https://conda.github.io/conda-pack/) to install a `conda` environment on your occigen account. For `conda-pack` to work, `conda` must be installed and be on your path. In order to set this up, first scp [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) for a Linux system to occigen and bash install `miniconda`. Now, pack your desired `conda` environment in a local Linux environment using `conda-pack` and then scp the packed tar file to `$SCRATCHDIR` on occigen. Once you've expanded the tar file, you can activate the `conda` environment running `$ source $SCRATCHDIR/my_env/bin/activate`. **Make sure the path of the Python packages points to where your `conda` environment is (`$SCRATCHDIR/my_env/bin/python`)**.

- You need firefox to render your jupyter notebook/lab: so in your .bashrc put the line `module load firefox`

- Look for the file `/home/albert7a/.jupyter/jupyter_notebook_config.py`in your occigen account and modify the lines:
  - Comment the line `c.NotebookApp.password = ...`.
  - Uncomment the line `c.NotebookApp.open_browser=True`.
  - Uncomment the line `c.NotebookApp.browser = ` and choose firefox as the browser.
  - Uncomment the line `c.NotebookApp.port = ...` and set a port number that you prefer so that the notebook always first tries to use the same port number.

- If you want to use [`dask-jobqueue`](https://jobqueue.dask.org/en/latest/) (to submit a SLURM job to get computational resources):
  - Install the `dask-jobqueue` library.
  - Copy the file `/home/albert7a/.config/dask/jobqueue.yaml` in your account.
  - The syntax of the commands to put in the notebook is described [here](https://github.com/auraoupa/Toolbox/blob/master/dask_ressources.ipynb).
