# Scripts For File downloads
## Batch downloads
### Introduction
Sometimes we find ourselves in situations where we need to download a number of files online. For example, if you have to download 100 files, it is going to be very mundane to download one file after the other. `batch_download.py` solves this problem by modifying the file url in an incremental pattern and uses `wget` to pull the file to a specified download location.

### Prerequisite
This is a python script so it is assumed that you have python (either 2 or 3) installed.
Install `wget` using the following command - `pip install wget`

### Execution
Execute the script with the command -  `python batch_download.py`
Also, note the directory you set as download location. The directory in which the script is run is considered as the starting directory.
