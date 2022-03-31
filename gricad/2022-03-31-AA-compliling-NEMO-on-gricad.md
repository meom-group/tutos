# Compiling NEMO on Gricad

In your bashrc :
```
source /applis/site/nix_nur.sh
source /home/mchekki/.nix-profile/bin/iccvars.sh -arch intel64

. /home/mchekki/LibGlace/versions/modules/modules_rev4401cc7d_gnu6.3.0/init/bash
export MODULEPATH="/home/mchekki/LibGlace/modulefiles:$MODULEPATH"

module load netcdf/netcdf-4.6.1_intel18_hdf5_MPIO
module load nco/nco-4.7.6_intel18
#module load xios/xios-2.0
module load xios/xios-2.5_rev1907
```

The arch-dahu.fcm :
```
%NCDF_HOME           $NETCDF_DIR
%HDF5_HOME           $HDF5_DIR
%XIOS_HOME           $XIOS_DIR
%OASIS_HOME          /not/defiled

%NCDF_INC            -I%NCDF_HOME/include
%NCDF_LIB            -L%NCDF_HOME/lib -lnetcdff -lnetcdf -L%HDF5_HOME/lib -lhdf5_hl -lhdf5 -lhdf5
%XIOS_INC            -I%XIOS_HOME/include
%XIOS_LIB            -L%XIOS_HOME/lib -lxios -lstdc++
%OASIS_INC           -I%OASIS_HOME/build/lib/mct -I%OASIS_HOME/build/lib/psmile.MPI1
%OASIS_LIB           -L%OASIS_HOME/lib -lpsmile.MPI1 -lmct -lmpeu -lscrip

%CPP                 cpp -Dkey_iomput
%FC                  mpiifort -c -cpp
%FCFLAGS             -i4 -r8 -O3 -fp-model precise -fno-alias
%FFLAGS              %FCFLAGS
%LD                  mpiifort
%LDFLAGS
%FPPFLAGS            -P -traditional
%AR                  ar
%ARFLAGS             rs
%MK                  make
%USER_INC            %XIOS_INC %OASIS_INC %NCDF_INC
%USER_LIB            %XIOS_LIB %OASIS_LIB %NCDF_LIB

%CC                  cc
%CFLAGS              -O0
```
