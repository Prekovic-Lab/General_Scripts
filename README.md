
# General Scripts

All the general scripts for handling omics data used in our lab.

## [Cram_To_Bam_Shell_Script_All_Files](General_Genomics_Scripts/convert_all.sh)
#### A simple script to convert all cram files to bam files and then index the bam



**To use the script:**

1. Download and place it in the folder where you want to run it.
2. Make it executable using the following command:

   ```bash
   chmod +x convert_all.sh
   ```
3. Execute the script in the directory with the `.cram` files:
   ```bash
   ./convert_all.sh
   ```
4. Ensure the `REFERENCE` variable within the script points to the appropriate reference genome file for your CRAM files.
5. The script will process each `.cram` file in the current directory, converting it to `.bam` and creating the corresponding `.bai` index.

**Use the appropriate REFERENCE file (examples):**

- **Human**:
  - [Reference Files](https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/)
    - Homo_sapiens.GRCh38.dna.primary_assembly.fa
    - Homo_sapiens.GRCh38.dna.primary_assembly.fa.fai

- **Mouse**:
  - [Reference Files](https://ftp.ensembl.org/pub/release-110/fasta/mus_musculus/dna/)

**Check if the process is running:**

To see if the conversion script is active, use:
```bash
ps aux | grep convert_all.sh
```
