#!/bin/bash

# Path to the reference genome
REFERENCE="Homo_sapiens.GRCh38.dna.primary_assembly.fa"

# Loop through each CRAM file in the current directory
for cram in *.cram; do
    # Convert CRAM to BAM
    bam="${cram%.cram}.bam"
    samtools view -b -T "$REFERENCE" -o "$bam" "$cram"
    
    # Index the BAM file
    samtools index "$bam"
done