import matplotlib.pyplot as plt

def visualize_gc_content(gc_content_file):
    sequences = []
    gc_contents = []

    with open(gc_content_file, 'r') as f:
        for line in f:
            seq_id, gc_content = line.strip().split("\t")
            sequences.append(seq_id)
            gc_contents.append(float(gc_content.strip('%')))

    plt.figure(figsize=(10, 5))
    plt.bar(sequences, gc_contents, color='green')
    plt.xlabel('Sequence ID')
    plt.ylabel('GC Content (%)')
    plt.title('GC Content per Sequence')
    plt.show()
