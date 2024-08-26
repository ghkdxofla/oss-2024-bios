import sys

from Bio import SeqIO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sequence_length.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    total_length = 0

    for record in SeqIO.parse(fasta_file, "fasta"):
        total_length += len(record.seq)

    with open("sequence_length.txt", "w") as f:
        f.write(str(total_length))
