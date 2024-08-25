version 1.0

workflow CoronavirusAnalysis {
  String fasta_file
  String sequence_length_script
  String gc_content_script

  input {
    File fasta_file
    File sequence_length_script
    File gc_content_script
  }

  call SequenceLength {
    input:
      fasta_file = fasta_file,
      script = sequence_length_script
  }

  call GCContent {
    input:
      fasta_file = fasta_file,
      script = gc_content_script
  }

  output {
    Int total_length = SequenceLength.total_length
    File gc_content_file = GCContent.output_file
  }
}

task SequenceLength {
  input {
    File fasta_file
    File script
  }

  command {
    python3 <<sequence_length>> fasta_file
  }

  output {
    Int total_length = read_int("output_length.txt")
  }

  runtime {
    docker: "python:3.9-slim"
  }
}

task GCContent {
  input {
    File fasta_file
    File script
  }

  command {
    python3 <<gc_content>> fasta_file
  }

  output {
    File output_file = "gc_content.txt"
  }

  runtime {
    docker: "python:3.9-slim"
  }
}
