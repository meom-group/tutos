# Jupyter on cal1

## How to run jupyter on cal1 and the notebook on a local machine

 - on cal1  :
   - create a conda environment for jupyter : 
      - conda create --name env-jup
      - conda activate env-jup
      - conda install python=3.6 jupyter jupyterlab ipykernel xarray dask netcdf4 matplotlib
      - conda install -c conda-forge/label/cf202003 nodejs
   - install the kernel in jupyter relative to the conda environment
      - python -m ipykernel install --user --name env-jup --display-name env-jup
   - extra step to get the dask dashboard running in the jupyterlab :
      - pip install dask_labextension
      - jupyter labextension install dask-labextension
      - jupyter serverextension enable --py --sys-prefix dask_labextension
   - launch jupyter :
      - jupyter notebook --no-browser --port 1234
 - on your local machine :
   - make a tunnel to cal1 : ssh -NL 1234:localhost:1234 -L 8787:localhost:8787 alberta@ige-meom-cal1.u-ga.fr
   - open your browser and look for : localhost:1234
   - enter the token given in cal1 (or copy paste the address)
   
   
## How to get dask dashboard running

  - in the browser address replace tree by lab
  - run the notebook demo : https://github.com/meom-group/tutos/blob/master/cal1/2020-03-20-AA-demo-dask-dashboard-xarray-on-cal1.ipynb
  - click on the dask icon and copy the address of the dashboard
  - click on the items you want to see : 
  - see your cores working !!
  
  
## Important note on the name of the port

As we are several users on cal1, it can happen that the port you request is already in use by someone else.

You can check on cal1 with the command : netstat -tnlp

If you see the line : `tcp        0      0 127.0.0.1:1234          0.0.0.0:*               LISTEN      5854/python3.6`it means that someone else uses 1234 for the his jupyter session and also `tcp        0      0 0.0.0.0:8787            0.0.0.0:*               LISTEN      -` means that the dashboard is already in use also.

So you need to choose a number that does not appear for both the notebook and the dash board and change the command `ssh -NL 1234:localhost:1234 -L 8787:localhost:8787 alberta@ige-meom-cal1.u-ga.fr`accordingly.

Finally, when you create a dask cluster, you need to specify the dashboard_adress as follows : cluster = LocalCluster(n_workers=2, threads_per_worker=2,dashboard_address=':8888') and you report the correct address in the dask tool to get the dashboard active.
