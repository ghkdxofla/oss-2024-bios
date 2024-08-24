version 1.0

workflow CoronavirusAnalysis {

  input {
    File fasta_file = "data/coronavirus.fasta"
  }

  call SequenceLength {
    input:
      fasta_file = fasta_file
  }

  call GCContent {
    input:
      fasta_file = fasta_file
  }

  output{
    Int total_length = SequenceLength.total_length
    File gc_content_file = GCContent.output_file
  }
}

task SequenceLength {
  input {
    File fasta_file
  }

  command {
    python3 sequence_length.py {fasta_file}
  }

  output {
    Int total_length = read_int(stdout())
  }

  runtime {
    docker: "biopython/biopython:latest"
  }
}

task GCContent {
  input {
    File fasta_file
  }

  command {
    python3 gc_content.py {fasta_file}
  }

  output {
    File output_file = "gc_content.txt"
  }

  runtime {
    docker: "biopython/biopython:latest"
  }
}
