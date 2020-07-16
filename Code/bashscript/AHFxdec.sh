#!/bin/bash
# MOAB/Torque submission script for SciNet GPC (ethernet)
#
#PBS -l nodes=32:ppn=8,walltime=30:00
#PBS -N AHF_xdec

# SUBMIT LARGE AMIGA HALO FINDING JOBS

# Switch to run directory
cd /scratch/p/pen/mwiner/gadget/gadg_0512_3e-5_dm_xdec5e7_new/AHF

#Run AHF 
mpirun -np 256 /home/p/pen/mwiner/ahf-v1.0-067/bin/AHF-v1.0-067 AHF.input

