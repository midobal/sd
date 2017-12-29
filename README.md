# Statistical Dictionary #

This software translates a text using an statistical dictionary.

## Dependencies ##

To generate IBM Model 1 alignments, [mgiza](https://github.com/moses-smt/mgiza) is needed.

## Usage ##

### Alignments ###

```bash
IBM1Alignments.sh source_file target_file dest_dir
```

Where:

* **source_file** is the source from the parallel training data.
* **target_file** is the target from the parallel training data.
* **dest_dir** is the directory in which to save the alignments.

Note: the script expects a variable (*$GIZA*) pointing towards *mgiza*'s bin directory.

### Text translation ###

```bash
SD.py -t text_file -a alignments
```

Where:

* **text_file** if the text to translate.
* **alignments** is the file created at the alignments step (*dest_dir/alignmetns*).
