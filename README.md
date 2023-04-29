# SmartHomeCam

Face and object recognition using Python AI and IP Cams

### Requirements

Running `danger-python` requires:

* Python 3.11 (tested under Python 3.11.3)

:warning: To verify that you've installed Python successfully on your machine, run `py -3 --version`.

### Installation

In order to test the script please run the following commands:

```sh
# install danger-js
npm install -g danger
# install danger-python
pip install danger-python
# run danger-python
danger-python pr https://github.com/microsoft/TypeScript/pull/34806
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