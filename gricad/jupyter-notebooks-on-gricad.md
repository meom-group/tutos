# Running jupyter notebooks on gricad

# Get an account (do it once)
 - read documentation : https://gricad-doc.univ-grenoble-alpes.fr/
 - account management : https://perseus.univ-grenoble-alpes.fr/

# Log in easily (do it once)
 - follow the procedure described here : https://gricad-doc.univ-grenoble-alpes.fr/hpc/connexion/, the rest of the tuto will not work if you don't !
 
# Conda environment (do it once)

 - wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
 - sh Miniconda2-latest-Linux-x86_64.sh
 - . ~/.bashrc
 - conda info
 - conda create --name pangeo python=3.7
 - conda activate pangeo
 - conda install xarray dask scipy zarr netcdf4 ipython jupyter matplotlib pandas numba ipykernel nodejs (example of librairies for pangeo environment + jupyter kernel + dask extension in jupyterlab)
 - conda install cartopy (separately from the others otherwise it messes up ...)
 - conda install -c conda-forge papermill (running notebooks like scripts)
 - conda install -c conda-forge cmocean (beautiful oceanic colors on your plots)
 - python -m ipykernel install --user --name pangeo --display-name pangeo
### For dask dashboard in jupyter lab
 - jupyter labextension install dask-labextension
 - jupyter serverextension enable --py --sys-prefix dask_labextension
 
# Run the jupyter notebook (on the first time)
 - follow the instructions : https://gricad-doc.univ-grenoble-alpes.fr/notebook/hpcnb/
 
 # Run the jupyter notebook with conda environment (everytime)
 
  - in the first terminal :
     - login : ssh f-dahu.ciment
     - oarsub -I --project data-ocean -l /core=10,walltime=2:00:00 -> it will log automatically on a login node dahuX
     - conda activate pangeo
     - jupyter notebook/lab
  - in a second terminal :
     - ssh -fNL 8888:dahuX:8888  [ -L 8686:dahuX:8686 for the dashboard] dahu.ciment (see the notebook https://github.com/meom-group/tutos/blob/master/notebook/2020-04-15-AA-gricad-20-workers.ipynb for how to define the cluster )
  - on your laptop in a browser: http://localhost:8888/?token=... (see the result of the jupyter notebook command)
  - when you're done liberate the listening ports :
     - lsof -ti:8888 and 8686 to get the number of the process then kill it
