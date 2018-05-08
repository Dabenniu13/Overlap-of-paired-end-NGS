# Overlap-of-paired-end-NGS
to pick out the completely base paired overlap part from the fastq files of paired-end NGS

Next generation sequencing technology can produce many sequencing errors which could come from the amplification or sequencing stages.
If we do paired-end sequencing, then some short segments of sequences will have a overlap part. 
If there is a sequencing error on the overlap part, the chance for the error to happen on both of the reads in opposite directions is very low.
This program is to pick out the completely base paired overlap part, if there is, from the two reads aiming to reduce the sequencing errors.
To run it, you need to provide the two fastq files. It will produce a new fastq file which only contains the completely base paired overlap sequence, and a test file providing more information about the process.
