# cromwell_runner/visualizer.py
import matplotlib.pyplot as plt

def visualize_gc_content(gc_content_file):
    """
    Visualizes the GC content from the output file.

    :param gc_content_file: Path to the GC content output file.
    """
    try:
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

    except Exception as e:
        print(f"An error occurred during visualization: {str(e)}")

