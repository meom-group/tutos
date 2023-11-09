# MEOM server cal1

## Description

cal1 is a server that allows you to access MEOM data and connect to other servers (like french super computers)

It is accessible from anywhere (IGE or your home) at the adress : ```ige-meom-cal1.u-ga.fr```

## Access and workspaces

As soon as you have an agalan account (IGE login), you can have an account there (ask [Aurélie](mailto:aurelie.albert@univ-grenoble-alpes.fr) to authorize your login) and you can connect via ssh : ```ssh -CX yourlogin@ige-meom-cal1.u-ga.fr```

It is recommended to implement a ssh key from anywhere you want to connect to it, so that you do not have to type your password everytime :
  - in your local machine type : ```ssh-keygen``` (unless you already have a key)
  - it will create a file .ssh/id_rsa.pub
  - copy it to cal1 via the command : ```ssh-copy-id yourlogin@ige-meom-cal1.u-ga.fr``` and type your password for the last time

You will have access to 2 personnal workspaces : ```/home/yourlogin``` (automatically created) and ```/mnt/summer/DATA_MEOM/workdir/yourlogin``` (you have to create it yourself with mkdir in /mnt/summer/DATA_MEOM/workdir), the first one is limited in space and you should only put scripts on it, the second is like a scratch where your temporary and results files should be stored.

You can see how much of these spaces are filled with the command ```df -h``` (look for /home and /mnt/summer/DATA_MEOM to see how much space is left)

You can transfer data from your computer to cal1 with the command ```scp myfile yourlogin@ige-meom-cal1.u-ga.fr:/mnt/summer/DATA_MEOM/workdir/yourlogin/where_you_want_it/myfile``` and you can download data from cal1 to your computer with the command : ```scp yourlogin@ige-meom-cal1.u-ga.fr:/mnt/summer/DATA_MEOM/workdir/yourlogin/path_to_your_file/myfile .```

[Here](https://github.com/meom-group/tutos/blob/master/summer.md) is the complete tutorial on how to use SUMMER storage to store and share your data.
