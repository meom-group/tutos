# Some informations on the occigen machine

In the following, I call tunnel machine the machine from which you connect to occigen (cal1 for MEOM people)

### Different workspaces

On occigen, there are 3 types of space :
  - your home (/home/abendinger), limited to 100G 30 000 files
  - your scratch (/scratch/cnt0024/ige2071/abendinger), common space between all memebers of ige2071 group, limited to 20,480 Tb 900 000files in total
  - your store ( /store/abendinger ), limitations on number of inodes depending on the project (it looks like it is not reinforced yet for we are way above the 9000 files limit ...
  - the `etat_projet` command allows user to know whether the quotas are exceeding and where
  - be careful not to be over quota, this will prevent all people in the group to submit jobs !

 
I recommend to put all the valuable scripts on your home, the working or temporary files on the scratch and for longer conservation on the store (make tar of files). Conda environments and git repo can have many files so it's better to put it on scratch.

https://www.cines.fr/calcul/organisation-des-espaces-de-donnees/espaces-de-donnees-quotas-disques-restaurations-de-fichiers/

### Computing environment

- `module list`to see what is already loaded and `module avail`to see what's available

I recommend putting the following lines in your .bashrc (also add the line `source $HOME/.bashrc in your .bash_profile`) :

```
module load intel
module load openmpi/intel/2.0.1
module load hdf5/1.8.17
module load netcdf/4.4.0_fortran-4.4.2
alias ncdump='/opt/software/occigen/libraries/netcdf/4.4.0_fortran-4.4.2/hdf5/1.8.17/intel/17.0/openmpi/intel/2.0.1/bin/ncdump'
alias ncview='/opt/software/occigen/graphics/ncview/2.1.2/hdf5/1.8.18/netcdf/4.4.0_fortran-4.4.2/intel/17.2/openmpi/intel/2.0.1/bin/ncview'
```

### Different nodes

There are two types of nodes on which to log in :
  - regular frontal node : `ssh -CX aalbert@occigen.cines.fr` (you end up on login0-1-2-3)
  - visualization node : `ssh -CX aalbert@visu.cines.fr` (login4) on which we can deploy a visualization session https://www.cines.fr/calcul/materiels/visualisation/sessions-interactives-vnc/ (see below for specific details for deploying jupyter notebooks)

### Submitting jobs


  - An example of job script using SLURM syntaxe :

```
#!/bin/bash

#SBATCH --nodes=5
#SBATCH --ntasks=108
#SBATCH -J mean1m-cal
#SBATCH -e mean1m-cal.e%j
#SBATCH -o mean1m-cal.o%j
#SBATCH --time=05:30:00
#SBATCH --exclusive
#SBATCH --constraint=HSW24
```

  - you must specify :
    - tasks : the number of proc you actually need, must be lower than number of node x 28 (28 cores per node)
    - you choose on which nodes (CPU  : HSW24 & BDW28 or VISU) you submit your job to by changing the line `#SBATCH --constraint=HSW24` 
    - 1 node and 6h max for VISU nodes
    - less than 24h for CPU nodes (<30mn jobs are running almost immediately)
  - You submit the job by typing : `sbatch your_job_script.ksh`
  - You check your job status by typing : `squeue -u your_login`


https://www.cines.fr/wp-content/uploads/2020/09/demarrer_sur_occigen.pdf

### Setting up conda on occigen

*Update* :
You can access conda by loading this module :
`module load /opt/software/alfred/spack-dev/modules/tools/linux-rhel7-x86_64/miniconda3/4.7.12.1-gcc-4.8.5`

then you install the librairies you need :

```
mkdir ${SCRATCHDIR}/MY_CONDA
conda install ipython xarray netcdf4 -p ${SCRATCHDIR}/MY_CONDA
```

Occigen do not allow conda installs directly but you can use pip.~

You can always ask svp@cines.fr to set up a conda environment for you with the list of libraries you need.

For more freedom here is a workflow to set up your own conda environment on occigen :

- On the tunnel machine :
  - install conda from installer :https://docs.conda.io/en/latest/miniconda.html
  - set up a conda environment with all librairies you want :
    - `conda create --name caledo`
    - `conda activate caledo
    - `conda install -c conda-forge netcdf4 xarray dask numpy seawater cartopy cmocean papermill jupyter conda-pack ipykernel seaborn`
  - `conda pack -n caledo`
  - `scp caledo.tar.gz aalbert@occigen.cines.fr:/scratch/cnt0024/ige2071/aalbert/conda/.`
  - `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
  - `scp Miniconda3-latest-Linux-x86_64.sh aalbert@occigen.cines.fr:/home/aalbert/.`
    
- On occigen :
  - `chmod +x Miniconda3-latest-Linux-x86_64.sh; ./Miniconda3-latest-Linux-x86_64.sh` (choose /scratch/cnt0024/ige2071/aalbert/conda/miniconda3 for where to install)
  - add in .bash_aliases `alias cond="export PATH='/scratch/cnt0024/ige2071/aalbert/conda/miniconda3/bin:$PATH'"`
  - `source .bash_aliases; cond`
  - `cd /scratch/cnt0024/ige2071/aalbert/conda/; mkdir caledo; tar -xzf caledo.tar.gz -C caledo`
  - `source caledo/bin/activate`
  - `python -m ipykernel install --user --name caledo --display-name caledo` (to make the libraries available in the jupyter notebooks, see below for deployment)

### Jupyter Notebook

On occigen you have the choice between :
  - running (smoothly) 6h on one out of 4 specific nodes with large memory when 1 is available (256Go) : the visu solution (needs vncviewer installed and port 5901 open on your login machine)
  - running (less smoothly except if you are directly on the tunnel machine) 30mn whenever you want with access to multiple CPU nodes (64/128Go) : the frontal solution
  
#### Running on visu node

Private access to one node of visu (28 cores, 256Go, 6h)

First terminal :
  - connect to visu : `ssh -CY aalbert@visu.cines.fr`
  - check if one visu is available : `vizqueue`, only 4 nodes visu1-4
  - book one node for maximum 6h : `vizalloc -m vnc -t 360`, one node is allocated to you
  
Second terminal :
  - connect to the visu node allocated to you : `ssh -CX aalbert@visu3.cines.fr`
  - got to your notebook repo (same architecture than on occigen) and launch jupyter notebook : `/scratch/cnt0024/ige2071/aalbert/conda/miniconda3/bin/jupyter-notebook --no-browser` (make an alias of it : add `alias jupnb="export PATH="/scratch/cnt0024/ige2071/aalbert/conda/miniconda3/bin:$PATH"; jupyter-notebook --no-browser"` in your .bash_aliases, `source /home/aalbert/.bash_aliases`)

Third terminal :
  - launch vncviewer on the tunnel machine
  - enter the name of the visu node you got in VNC server : `visu3.cines.fr:5901` , click on connect

<img src="https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/img/login-visu-vncviewer.png" width=50% height=50%>

  - enter login & passwd


<img src="https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/img/login-occigen-visu.png" width=50% height=50%>

  - a virtual machine is launching, slide up to get to the desktop


![](https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/img/vncviewer.png)

  - click on Applications/Outils Sytem/Terminal
  - `module load firefox; firefox` 
  - copy the adress output for jupyter command in the firefox terminal

![](https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/img/3terminals.png)

To access the ressources of the visu node with dask, in a cell  :
```
from dask.distributed import Client, LocalCluster
cluster = LocalCluster()
c = Client(cluster)
c
```

you should get access to the dask dashboard by clicking on the link :

![](https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/img/dask-dashboard-visu.png)

A complete notebook can be found here : https://github.com/auraoupa/scripts-occigen-for-Arne/blob/main/notebooks/visu/2021-02-25-AA-map-yearly-mean-surface-fields-caledo.ipynb

#### Running on frontal nodes

**Be careful not to compute directly on login nodes, always ask for CPU ressources first with dask-jobqueue**

Job submitted inside the notebook to access the CPU nodes (28 cores, 64/128Go, 30mn)

We need two different terminals because firefox and the jupyter notebooks cannot be run together (not sure why, because of conda I guess)

First terminal :
  - connect to occigen : `ssh -CY aalbert@occigen.cines.fr`
  - got to your notebooks repo and launch jupyter notebook : `/scratch/cnt0024/ige2071/aalbert/conda/miniconda3/bin/jupyter-notebook --no-browser` (make an alias of it)

Second terminal :
  - log to occigen and do it until you get the same login node (login0-1-2-3)
  - `module load firefox;firefox &`
  - copy the adress output for jupyter command in the firefox terminal

To access the ressources from CPU nodes with dask-jobqueue :
  - first submit a job inside the notebook (example for one node) :
```
ask_workers=28
memory='120GB'
from dask_jobqueue import SLURMCluster 
from dask.distributed import Client 
  
cluster = SLURMCluster(cores=28,name='pangeo',walltime='00:30:00',
                       job_extra=['--constraint=HSW24','--exclusive',
                                  '--nodes=1'],memory=memory,
                       interface='ib0') 
cluster.scale(ask_workers)
c= Client(cluster)
c
```
  - wait for the job to be running (check with squeue the status)
  - check in the notebook how many workers are running :
```
from dask.utils import ensure_dict, format_bytes
    
wk = c.scheduler_info()["workers"]

text="Workers= " + str(len(wk))
memory = [w["memory_limit"] for w in wk.values()]
cores = sum(w["nthreads"] for w in wk.values())
text += ", Cores=" + str(cores)
if all(memory):
    text += ", Memory=" + format_bytes(sum(memory))
print(text)
```

  - for this particular example, the answer should be : `Workers= 28, Cores=28, Memory=120.12 GB` before you can proceed with your computation
  - for examples with more nodes involved, see https://github.com/AurelieAlbert/perf-pangeo-deployments/blob/master/notebooks/occigen/2020-12-10-AA-temp-mean-zarr-2node-HSW24-test1.ipynb and other notebooks in https://github.com/AurelieAlbert/perf-pangeo-deployments/blob/master/notebooks/occigen

