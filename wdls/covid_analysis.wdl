version 1.0

workflow CoronavirusAnalysis {
  input {
    File fasta_file
    File sequence_length_script
    File gc_content_script
    File pipfile
    File pipfile_lock
    String output_file
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
      gc_content_file = GCContent.output_file,
      output_file = output_file
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
    pipenv run python ${script} ${fasta_file} > sequence_length.txt
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
    pipenv run python ${script} ${fasta_file} > gc_content.txt
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
    String output_file
  }

  command {
    echo "Sequence Length Results:" > "${output_file}"
    cat ${sequence_length_file} >> "${output_file}"
    echo "" >> output_file
    echo "GC Content Results:" >> "${output_file}"
    cat ${gc_content_file} >> "${output_file}"
  }

  output {
    File combined_file = "${output_file}"
  }

  runtime {
    docker: "ubuntu:latest"
  }
}
