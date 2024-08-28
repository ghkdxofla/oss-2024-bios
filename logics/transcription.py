import sys

from Bio import SeqIO


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe_sequences.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    output_file = "transcribed_sequences.txt"

    with open(output_file, "w") as f:
        for record in SeqIO.parse(fasta_file, "fasta"):
            # DNA 시퀀스를 RNA 시퀀스로 전사
            rna_seq = record.seq.transcribe()
            f.write(">{}\n{}\n".format(record.id, rna_seq))
