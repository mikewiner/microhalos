#Find the largest halos in AHF files

head -3 *_halos | gawk '{print $4, $5, $6*1000, $7*1000, $8*1000, $12*1000}'