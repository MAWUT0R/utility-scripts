## Introduction
`health_check.py` is a script that checks and prints the summary of a system's main disk space and cpu usage average. It makes use the `shutil` and `psutil` python modules to access disk and cpu respectively. You can tweak the code and/or modify the arguments to suit your use case.

## Prerequisites
To execute the script, you will need:
- A machine running Windows, MacOS or Linux.
- Python installed on the machine. You can follow the tutorial [How To Install Python 3 and Set Up a Local Programming Environment on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-18-04) to install and set up Python on your local machine.
- Git installed on your machine. You can follow the tutorial [How To Contribute to Open Source: Getting Started with Git](https://www.digitalocean.com/community/tutorials/how-to-contribute-to-open-source-getting-started-with-git) to install and set up Git on your machine.

## Execution
To execute the script, you may follow the steps below:

### Step 1
In your terminal window, clone the `utility-scripts` repository:
```
git clone https://github.com/MAWUT0R/utility-scripts.git
```
By doing this, the whole repository including this script is made available locally on your machine.

### Step 2
Change directory into `sys-health-check`:
```
cd utility-scripts/sys-health-check/
```
Changing directory makes it for easy execution.

### Step 3
Make `health_check.py` executable:
```
chmod +x health_check.py
```
`chmod` is a system command that tells the system to change the access permissions of file objects. Here, we tell the system to that we want to execute the script without a preceding command.

### Step 4
Run the script:
```
./health_check.py
```
Your output should look similar to this:
```
```

## Conclusion
