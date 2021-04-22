#!/bin/bash


# num_figs_patients="$1"; shift
# num_figs_control="$1"; shift


rm RMS*.txt

#for (( e = 1; e <= num_figs_patients; e = e+1 ))		
for i in *.jpg
do  
  #convert n${e}.jpg -resize 650×650! n${e}.jpg
  convert ${i} -resize 500x500! ${i}
done

# for (( e = 1; e <= num_figs_control; e = e+1 ))		
# do  
#   #convert n${e}.jpg -resize 650×650! n${e}.jpg
#   convert n${e}.jpg -resize 500x500! n${e}.jpg
# done
