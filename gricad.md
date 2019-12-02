## Perseus account

* First go and create a Perseus account https://perseus.ujf-grenoble.fr
* Then create a new project or ask to be included in an already existing project (for example data-ocean was created by Julien and myself).
* contact sos-calcul-gricad@univ-grenoble-alpes.fr for any question

## Access to Dahu (for CPU and GPU use)

```
ssh lguensar@access-rr-ciment.imag.fr (((replace lguensar by your username)))
ssh f-dahu
source /applis/environments/conda.sh
```
Then you can start a job (here example of a GPU job)
```
oarsub -t gpu -I -l /nodes=1/core=32,walltime=12:00:00 --project data-ocean
```
## Use jupyter notebooks
You need to launch jupyter notebook from your terminal connected to dahu, then open a new terminal and use a SSH tunnel
```
ssh -fNL 8889:bigfoot3:8888 dahu.ciment ((((8889 is your port, 8888 is the port of the machine where the notebooks are active))))
```

## See availablity of Dahu nodes

https://ciment-grid.univ-grenoble-alpes.fr/clusters/dahu/drawgantt/drawgantt.php
