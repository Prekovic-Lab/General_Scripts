# General Scripts

All the general scripts for handling omics data used in our lab.


## [Cram_To_Bam_Shell_Script_All_Files](General_Genomics_Scripts/convert_all.sh)
#### a simple script ot convert all cram files to bam files and then index the bam

**To use the script:**

- Download and put in the folder that you want to run it in.
- Make it executable: chmod +x convert_all.sh.
- Execute it in the directory with the .cram files: ./convert_all.sh.
- Ensure the REFERENCE variable points to the appropriate reference genome file for your CRAM files.
- This script will process each .cram file in the current directory, converting it to .bam and creating the corresponding .bai index.

**Use the appropriate REFERENCE file (example):**

- [human](https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/)
  - Homo_sapiens.GRCh38.dna.primary_assembly.fa
  - Homo_sapiens.GRCh38.dna.primary_assembly.fa.fai

- [mouse](https://ftp.ensembl.org/pub/release-110/fasta/mus_musculus/dna/)


**Check if the process is running:**
- ps aux | grep convert_all.sh
