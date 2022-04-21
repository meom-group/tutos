#!/bin/bash
#SBATCH -J cdfcurl_medwest_seq
#SBATCH -n 1          
#SBATCH -o cdfcurl_medwest_%J.out
#SBATCH -e cdfcurl_medwest_%J.err
#SBATCH --time=00:31:00
#SBATCH --mem=14000
#SBATCH --account=fortran

fileu=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridU_20100206-20100206_pp.nc
filev=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridV_20100206-20100206_pp.nc

echo $fileu $filev
cd /mnt/meom/workdir/alberta/post-process-MEDWEST
./script_compute_vorticity.ksh $fileu vozocrtx $filev vomecrty
