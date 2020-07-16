#!/bin/bash
# MOAB/Torque submission script for SciNet GPC (ethernet)
#
#PBS -l nodes=16:ppn=8,walltime=30:00
#PBS -N AHF_1024

# SUBMIT LARGE AMIGA HALO FINDING JOBS

# Switch to run directory
cd /scratch2/p/pen/mwiner/AHF/gadg_1024_3e-5_dm/

#Run AHF 
mpirun -np 128 /home/p/pen/mwiner/ahf-v1.0-067/bin/AHF-v1.0-067 AHF.input

