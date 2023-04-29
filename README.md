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

Create a virtual environment in the workspace folder.
Run the following commands:

```sh
# create virtual environment 
py -3 -m venv .venv
# activate virtual environment 
./.venv/Scripts/Activate.ps1
```

Install all required modules:

```sh
pip install -r requirements.txt
```

:warning: To verify that you've installed Python successfully on your machine, run `py -3 --version`.



\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.

if Get-ExecutionPolicy - RestrictedSet

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force



pip freeze > requirements.txt

pip install -r requirements.txt