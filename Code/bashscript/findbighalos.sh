#Find the largest halos in AHF files

head -3 *_halos | gawk '{print $4, $5, $6, $7, $8, $12}'