# SmartHomeCam

Face and object recognition using Artificial Intelligence (AI) and Internet Protocol (IP) cameras.

### Requirements

* Python 3.11 (tested under Python 3.11.3)

:warning: To verify that you've installed Python successfully on your machine, run `py -3 --version`.

### Installation

Create a virtual environment in the workspace folder.
Run the following commands:

```sh
# create virtual environment 
py -3 -m venv .venv
# activate virtual environment 
./.venv/Scripts/Activate.ps1
```




py -m venv .venv

./.venv/Scripts/Activate.ps1


python 3.11.3



\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.

if Get-ExecutionPolicy - RestrictedSet

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force



pip freeze > requirements.txt

pip install -r requirements.txt