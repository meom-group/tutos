#!/bin/bash
#MSUB -r  name                    # Request name                     
#MSUB -n  48                    # Number of tasks to run            
#MSUB -N  1                   # Number of nodes to use          
#MSUB -T 100                      # Elapsed time limit in seconds   
#MSUB -o zssh_<MBR>.o%I            # Standard output. %I is the job id
#MSUB -e zssh_<MBR>.e%I            # Error output. %I is the job id   
#MSUB -q rome                       # queue name                                   
#MSUB -A gen12020                  # Project ID       
#MSUB -m store,work,scratch
#MSUB -x



CONFIG=ORCA025.L75
CASE=OCCITENS

mbr=<MBR>
freq=5d
CONFCASE=${CONFIG}-${CASE}.$mbr

ROOTDIR=/ccc/store/cont003/gen0727/molines/bessierl_store

mkdir -p  $DDIR/${CONFCASE}-S/$mbr

DTADIR=$ROOTDIR/${CONFIG}/${CONFCASE}-S/$freq
TGTDIR=$DDIR/${CONFCASE}-S/$mbr

mkdir -p $TGTDIR

cd  $TGTDIR
n=0

for f in $DTADIR/${CONFCASE}y????.$freq.tar ; do
  tar --wildcards '*ORCA025.L75-OCCITENS*_gridT.nc' -xf $f  &
  n=$(( n + 1 ))
  if [ $n == 48 ] ; then 
    n=0
    wait
  fi
done

wait
