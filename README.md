# SmartHomeCam

Face and object recognition using Artificial Intelligence (AI) and Internet Protocol (IP) cameras.

### Requirements

* Python 3.11 (tested under Python 3.11.3)

:warning: To verify that you've installed Python successfully on your machine, run `py -3 --version`.

### Installation

First of all, check your PowerShell execution policy:

```sh
Get-ExecutionPolicy
```

If it returns `Restricted` then run the following command:

```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
```

Next, сreate a virtual environment in the workspace folder.
Run the following commands:

```sh
# create virtual environment 
py -3 -m venv .venv
# activate virtual environment 
./.venv/Scripts/Activate.ps1
```

Finally, install all required modules:

```sh
pip install -r requirements.txt
```

:warning: Don't forget to update the requirements file after installing a new module in the project.
Do it by running the following command:

```sh
pip freeze > requirements.txt
```
