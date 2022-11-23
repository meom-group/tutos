#!/bin/bash
# Name   : restore_occi.sh
# Purpose : Rehydrate occiput tar files and submit extracting job
# Method : Loop on members. Rehydrate all files for a member in a while loop 
#          once rehydrated launch a job for this member based on a generic template.

## Information on configuration
CONFIG=ORCA025.L75
CASE=OCCITENS
freq=5d
ROOTDIR=/ccc/store/cont003/gen0727/molines/bessierl_store
ROOTCTL=/ccc/cont003/home/gen0727/molines/RUNS/

CTLDIR=$ROOTCTL/RUN_${CONFIG}/${CONFIG}-${CASE}/CTL

for mbr in {037..050} ; do     # Loop on members

   CONFCASE=${CONFIG}-${CASE}.$mbr
   DTADIR=$ROOTDIR/${CONFIG}/${CONFCASE}-S/$freq
   TGTDIR=$DDIR/${CONFCASE}-S/$mbr

   nr=1        # released file counter, initialized to 1 to start the process
   cd $DTADIR
   while [ $nr != 0 ] ; do  # loop till there are released files
      nr=0
      # Loop on targetted tar files to rehydrate
      for f in ${CONFCASE}y????.${freq}.tar ; do
         lfs hsm_state $f | grep -q released  # check if they are released
         if [ $? = 0 ] ; then
            lfs hsm_restore $f   # restore if they are released
            nr=$(( nr + 1 ))     # increment counter of released files
         fi
      done
      echo " NR = " $nr
      if [ $nr != 0 ] ; then sleep 120 ; fi  #  wait 2 mn before retrying
   done
   # at this point, all tar files for mbr are on line

   cd $CTLDIR  # create batch script from template for member mbr
   cat xtractSSH_tmp.sh | sed -e "s/<MBR>/$mbr/g" > xtractSSH_$mbr.sh
   ccc_msub xtractSSH_$mbr.sh    # submit job

done  # next member
   
