# Jupyter on cal1

## How to run jupyter on cal1 and the notebook on a local machine

 - on cal1  :
   - create a conda environment for jupyter : 
      - conda create -name env-jup
      - conda activate env-jup
      - conda install python=3.6 jupyter jupyterlab ipykernel nodejs xarray dask netcdf4 scipy
   - install the kernel in jupyter relative to the conda environment
      - python -m ipykernel install --user --name env-jup --display-name env-jup
   - extra step to get the dask dashboard running in the jupyterlab :
      - pip install dask_labextension
      - jupyter labextension install dask_labextension
      - jupyter serverextension enable -py -sys-prefix dask_labextension
   - launch jupyter :
      - jupyter notebook --no-browser --port 8888
 - on your local machine :
   - make a tunnel to cal1 : ssh -NL 8888:localhost:8888 alberta@ige-meom-cal1.u-ga.fr
   - open your browser and look for : localhost:8888
   - enter the token given in cal1 (or copy paste the address)
   
   
## How to get dask dashboard running

  - in the browser address replace tree by lab
  - run the notebook demo
  - click on the dask icon and copy the address of the dashboard
  - click on the items you want to see : 
  - see your cores working !!
