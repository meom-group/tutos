# Installation of jupyter notebooks on a personnal computer

## Installation of conda

We recommend the installation of [miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links), choose the isntaller according to your machine specification and then launch it (no need for root priviledges).

Make sur the path to conda bin is exported (```export PATH="/mnt/meom/workdir/albert/anaconda2/bin:$PATH"``` in your .bashrc for instance)

## Conda environment

Create a conda environment, activate it and install all the libraries you will need : 
```
conda create --name jupyter
conda activate jupyter
conda install numpy matplotlib netCDF4 jupyter jupyterlab xarray pandas dask ipykernel 
``` 

Check the [software page](https://github.com/meom-group/tutos/blob/master/software.md) to see what library could fit your needs.

Anytime you need a new library, do :

```
conda activate jupyter
conda install newlib
```

You can create as many environment as you need, for different python version for instance :
```
conda create --name python36
conda activate python36
conda install python=3.6 numpy matplotlib netCDF4 jupyter jupyterlab xarray pandas dask ipykernel 
``` 

## Turn your conda environment into a jupyter kernel

Install the kernel in jupyter relative to the conda environment :


```
python -m ipykernel install --user --name jupyter --display-name jupyter
```

Go to your python scripts or notebooks repository and launch jupyter :


```
jupyter notebook 

```

it will open a browser window and you will see the scripts of your repository.
You can open an existing notebook and select ```Noyau/Changer de noyau``` or ```Kernel/Switch Kernel``` and select jupyter as a kernel.

Now you can execute your notebook.

## Add a personnal library to python scripts or notebooks


Add the path to your module :

```
import sys
YOUR_MODULE_PATH = '/path/to/your/module'
sys.path.append(YOUR_MODULE_PATH)
import yourmodule
```
