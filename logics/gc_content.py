import sys

from Bio import SeqIO

fasta_file = sys.argv[1]
output_file = "gc_content.txt"

with open(output_file, "w") as f:
    for record in SeqIO.parse(fasta_file, "fasta"):
        gc_count = record.seq.count("G") + record.seq.count("C")
        gc_content = (gc_count / len(record.seq)) * 100
        f.write("{}\t{:.2f}%\n".format(record.id, gc_content))
