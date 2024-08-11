version 1.0

workflow Covid19Analysis {

  input {
    File fastq1
    File fastq2
    File reference_fasta
    String sample_name
  }

  # Step 1: Quality Control using FastQC
  call FastQC {
    input:
      fastq1 = fastq1,
      fastq2 = fastq2
  }

  # Step 2: Alignment using BWA
  call BWA {
    input:
      fastq1 = fastq1,
      fastq2 = fastq2,
      reference_fasta = reference_fasta
  }

  # Step 3: Variant Calling using GATK
  call GATK {
    input:
      bam = BWA.bam,
      reference_fasta = reference_fasta,
      sample_name = sample_name
  }

  output {
    File fastqc_report_1 = FastQC.report1
    File fastqc_report_2 = FastQC.report2
    File aligned_bam = BWA.bam
    File variants_vcf = GATK.vcf
  }
}

task FastQC {
  input {
    File fastq1
    File fastq2
  }

  command {
    fastqc ${fastq1}
    fastqc ${fastq2}
  }

  output {
    File report1 = "${basename(fastq1, ".fastq")}_fastqc.zip"
    File report2 = "${basename(fastq2, ".fastq")}_fastqc.zip"
  }

  runtime {
    docker: "biocontainers/fastqc:v0.11.9_cv8"
  }
}

task BWA {
  input {
    File fastq1
    File fastq2
    File reference_fasta
  }

  command {
    bwa mem ${reference_fasta} ${fastq1} ${fastq2} > aligned.sam
    samtools view -bS aligned.sam > aligned.bam
    samtools sort aligned.bam -o sorted.bam
    samtools index sorted.bam
  }

  output {
    File bam = "sorted.bam"
  }

  runtime {
    docker: "biocontainers/bwa:v0.7.17_cv1"
  }
}

task GATK {
  input {
    File bam
    File reference_fasta
    String sample_name
  }

  command {
    gatk HaplotypeCaller -R ${reference_fasta} -I ${bam} -O ${sample_name}.vcf
  }

  output {
    File vcf = "${sample_name}.vcf"
  }

  runtime {
    docker: "broadinstitute/gatk:4.2.0.0"
  }
}
