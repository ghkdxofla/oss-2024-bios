version 1.0

workflow CoronavirusAnalysis {
  input {
    File fasta_file
    File sequence_length_script
    File gc_content_script
    File transcription_script
    File pipfile
    File pipfile_lock
  }

  call SequenceLength {
    input:
      fasta_file = fasta_file,
      script = sequence_length_script,
      pipfile = pipfile,
      pipfile_lock = pipfile_lock,
  }

  call GCContent {
    input:
      fasta_file = fasta_file,
      script = gc_content_script,
      pipfile = pipfile,
      pipfile_lock = pipfile_lock,
  }

  call TranscribeRNA {
    input:
      fasta_file = fasta_file,
      script = transcription_script,
      pipfile = pipfile,
      pipfile_lock = pipfile_lock,
  }

  output {
    File sequence_length_file = SequenceLength.output_file
    File gc_content_file = GCContent.output_file
    File transcription_file = TranscribeRNA.output_file
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

task TranscribeRNA {
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
    pipenv run python ${script} ${fasta_file} > transcribed_sequences.txt
  }

  output {
    File output_file = "transcribed_sequences.txt"
  }

  runtime {
    docker: "python:3.11-slim"
  }
}
