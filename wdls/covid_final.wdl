version 1.0

workflow CoronavirusAnalysis {
  input {
    File fasta_file
    File sequence_length_script
    File gc_content_script
    File pipfile
    File pipfile_lock
  }

  call SequenceLength {
    input:
      fasta_file = fasta_file,
      script = sequence_length_script,
      pipfile = pipfile,
      pipfile_lock = pipfile_lock
  }

  call GCContent {
    input:
      fasta_file = fasta_file,
      script = gc_content_script,
      pipfile = pipfile,
      pipfile_lock = pipfile_lock
  }

  call CombineResults {
    input:
      sequence_length_file = SequenceLength.output_file,
      gc_content_file = GCContent.output_file
  }

  output {
    File combined_results = CombineResults.combined_file
  }
}

task SequenceLength {
  input {
    File fasta_file
    File script
    File pipfile
    File pipfile_lock
  }

  command {
    pip install pipenv
    cp ${pipfile} Pipfile
    cp ${pipfile_lock} Pipfile.lock
    pipenv install --deploy --ignore-pipfile
    pipenv run python ${script} ${fasta_file}
  }

  output {
    File output_file = "sequence_length.txt"
  }

  runtime {
    docker: "python:3.11-slim"
  }
}

task GCContent {
  input {
    File fasta_file
    File script
    File pipfile
    File pipfile_lock
  }

  command {
    pip install pipenv
    cp ${pipfile} Pipfile
    cp ${pipfile_lock} Pipfile.lock
    pipenv install --deploy --ignore-pipfile
    pipenv run python ${script} ${fasta_file}
  }

  output {
    File output_file = "gc_content.txt"
  }

  runtime {
    docker: "python:3.11-slim"
  }
}

task CombineResults {
  input {
    File sequence_length_file
    File gc_content_file
  }

  command {
    echo "Sequence Length Results:" > combined_results.txt
    cat ${sequence_length_file} >> combined_results.txt
    echo "" >> combined_results.txt
    echo "GC Content Results:" >> combined_results.txt
    cat ${gc_content_file} >> combined_results.txt
  }

  output {
    File combined_file = "combined_results.txt"
  }

  runtime {
    docker: "ubuntu:latest"
  }
}
