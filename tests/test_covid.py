def test_coronavirus_analysis(wdl_runner):
    # Run the WDL workflow
    outputs = wdl_runner.run(
        wdl="CoronavirusAnalysis.wdl",
        inputs={"CoronavirusAnalysis.fasta_file": "test_data/coronavirus.fasta"},
    )

    # Validate outputs
    assert "SequenceLength.total_length" in outputs
    assert outputs["SequenceLength.total_length"] > 0

    assert "GCContent.output_file" in outputs
    assert outputs["GCContent.output_file"].exists()

    # Check content of GCContent output file
    with open(outputs["GCContent.output_file"], "r") as f:
        content = f.read()
        assert "GC" in content  # Replace this with appropriate checks for your case
