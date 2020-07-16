#!/bin/bash
# MOAB/Torque submission script for SciNet GPC (ethernet)
#
#PBS -l nodes=8:ppn=8,walltime=8:00
#PBS -N AHF_1024

# SUBMIT LARGE AMIGA HALO FINDING JOBS

# Switch to run directory
cd /scratch/p/pen/mwiner/gadget/gadg_0512_3e-5_dm/output/

#Run AHF 
mpirun -np 8 /home/p/pen/mwiner/ahf-v1.0-067/bin/AHF-v1.0-067 AHF.input

