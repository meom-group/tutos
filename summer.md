# MEOM data storage

DATA_MEOM is a [summer](https://summer.univ-grenoble-alpes.fr/) storage unit where MEOM members and collaborators can store their data, access them from different servers, share them between each other and to the outside world.

## Access

It is accessible on different servers :
  - on [MEOM cal1 server](https://github.com/meom-group/tutos/blob/master/cal1/README.md), at the path ```/mnt/summer/DATA_MEOM```
  - on [IGE calcul1 server](https://github.com/IGE-numerique/ige-calcul/blob/main/schedulers/slurm/slurm.md) *waiting for approval*
  - on [GRICAD servers](https://github.com/meom-group/tutos/tree/master/gricad), at the path ```/summer/meom```

## Architecture

Different workspaces are available, some are personnal, other collaborative :
  - in ```workdir```, each active member or collaborator of MEOM can have a personnal workspace, for instance : ```/mnt/summer/DATA_MEOM/workdir/alberta```
    - you have to create it yourself the first time you connect to DATA_MEOM : ```cd workdir; mkdir mylogin```
    - it is recommended that you put reading rights to everyone but only you for writing and executing : ```chmod -R 744 mylogin```
    - if you are putting data in your workdir on cal1, make sure that the group associated to it is pr-data-ocean so that it can be accessible from GRICAD also : ```chown -R yourlogin:pr-data-ocean data```

![](https://github.com/meom-group/tutos/blob/master/pics/droits-dossiers.png)   
      
  - in ```DATA_SET```, useful datasets are gathered so that anyone can use it : click [here](https://github.com/meom-group/data-tools-inventory/tree/main#data-inventory) to see a catalog of available data
  - in ```MODEL_SET```, useful model outputs, grids and configuration files are gathered so that anyone can use it : click [here](https://github.com/meom-group/data-tools-inventory/tree/main#data-inventory) to see a catalog of it
  - in ```MEOM-OPENDAP```, users can make links to data they want to share via opendap, see [below](https://github.com/meom-group/tutos/blob/master/summer.md#sharing-data-via-opendap) for more informations

## Sharing data via opendap

Users can share selected data from DATA_MEOM to the outside world via an opendap server.

- You need to connect to the [cal1 server](https://github.com/meom-group/tutos/blob/master/cal1/README.md) to do the link between the data you want to share (from your workdir or DATA_SET or MODEL_SET)

- You create a sub-repository in ```/mnt/summer/DATA_MEOM/MEOM-OPENDAP``` with your login as a name, or a meaningful name (name of project or dataset)

- There you make a link with an absolute path to the required data, for instance :

```bash 
alberta@ige-meom-cal1:/mnt/summer/DATA_MEOM/MEOM-OPENDAP/eNATL60$ ln -sf /mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-I eNATL60-I
```

- The data stored in ```MEOM-OPENDAP``` are mirrored online at this adress : https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/catalog.html

- Users can share data by giving the link to a particular file or dataset to a collaborator, they can then download by clicking on the link then clicking on the HTTPServer link (it will start the download automatically) or they can download data via wget command, for instance : ```wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/eNATL60/eNATL60-I/mask_eNATL60_3.6.nc```
