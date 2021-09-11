**Source file split**

The repository contains pythin script that splits big csv files to smaller chunks.

**Setup:**
Libraries to install:
1. pandas

Above can be installed using:

_pip3 install pandas_

**Running the utility:**
The script takes input as destination path to save the chunks of the big file provided as input. It reads the source path for csv file(s) and breaks it into smaller sizes.

How to run:
from CLI type:
```python src_file_split.py  <destination path>```

**Output:**
The final output is 100MB smaller chunks of the source file(s).
