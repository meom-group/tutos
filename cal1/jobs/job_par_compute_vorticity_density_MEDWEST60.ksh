#!/bin/bash
#SBATCH -J cdfcurl_medwest
#SBATCH -n 1 
#SBATCH --ntasks=2
#SBATCH -o cdfcurl_medwest_%J.out
#SBATCH -e cdfcurl_medwest_%J.err
#SBATCH --time=00:31:00
#SBATCH --mem=8000
#SBATCH --account=fortran

NBPROCS=2

runcode() { srun --mpi=pmi2 -m cyclic -n $@ ; }
liste=''

fileu=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridU_20100206-20100206_pp.nc
filev=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridV_20100206-20100206_pp.nc

echo $fileu $filev

echo 'cd /mnt/meom/workdir/alberta/post-process-MEDWEST; ./script_compute_vorticity.ksh '$fileu' vozocrtx '$filev' vomecrty' >> tmp1.ksh
chmod +x tmp1.ksh
liste="$liste ./tmp1.ksh"

filet=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridT_20100206-20100206_pp.nc
files=/mnt/meom/workdir/alberta/post-process-MEDWEST/files/001MEDWEST60-GSL19-ens01_1h_20100206_20100215_gridS_20100206-20100206_pp.nc

echo '/mnt/meom/workdir/alberta/post-process-MEDWEST; ./script_compute_density.ksh '$filet' '$files' votemper vosaline' >> tmp2.ksh
chmod +x tmp2.ksh
liste="$liste ./tmp2.ksh"

runcode $NBPROCS /mnt/meom/workdir/molines/MEOLKERG/molines/DEV/DMONTOOLS/MPI_TOOLS/mpi_shell $liste
