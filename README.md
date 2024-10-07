# DNA Barcodes Generator

DNA Barcodes Generator is a Python package for creating unique DNA barcode sequences. It ensures the generated sequences meet specific criteria such as GC content, dissimilarity from other sequences, and absence from a reference genome database, for example bovine, human, mice, etc genomes.

## Features

- Generate DNA barcodes of specified length
- Control GC content of generated sequences
- Ensure minimum dissimilarity between generated sequences
- Check for sequence uniqueness against a local BLAST database
- Customizable parameters for sequence generation

## Installation

### Prerequisites

- Python 3.12 or higher
- NCBI BLAST+ (for local BLAST functionality)

To install NCBI BLAST+:

- On Ubuntu/Debian: `sudo apt-get install ncbi-blast+`
- On macOS with Homebrew: `brew install blast`
- On Windows: Download and install from the [NCBI website](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)

### Installing the package

1. Clone the repository:

   ```
   git clone https://github.com/JasperAugust/dna-barcodes.git
   cd dna-barcodes
   ```

2. Create a conda environment and install dependencies:

   ```
   conda env create -f environment.yml
   conda activate barcodes
   ```

3. Install the package:
   ```
   pip install -e .
   ```

## Usage

Here's a basic example of how to use the DNA Barcodes Generator:

```python
from dna_barcodes import BarcodesGenerator

generator = BarcodesGenerator(
desired_gc_content=0.50,
gc_tolerance=0.10,
sequence_length=16,
number_of_sequences=64,
min_dissimilarity=0.15
)

barcodes = generator.generate_barcodes()
generator.save_sequences(barcodes, "unique_sequences.txt")
```

## Configuration

You can customize the following parameters when initializing the `BarcodesGenerator`:

- `desired_gc_content`: Target GC content (default: 0.50)
- `gc_tolerance`: Allowed deviation from the target GC content (default: 0.10)
- `sequence_length`: Length of each barcode sequence (default: 16)
- `number_of_sequences`: Number of unique barcodes to generate (default: 64)
- `min_dissimilarity`: Minimum fraction of positions that must differ between sequences (default: 0.15)

## Local BLAST Database

To use the local BLAST functionality, you need to set up a BLAST database:

1. Prepare your reference genome(s) in FASTA format.
2. Create a BLAST database:
   ```
   makeblastdb -in your_genomes.fasta -dbtype nucl -out combined_genomes_db
   ```
3. Ensure the database name in the `local_blast_sequence` method matches your created database.

## Contributing

Contributions to the DNA Barcodes Generator are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Jasper August Tootsi - jasper.august.tootsi@ut.ee
