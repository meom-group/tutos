# Script running on cal1

## Running a python code:

For a python code, for e.g. code.py, you want to launch, these different options exist:

- ```python code.py```
  - Launches the python code (your job). You will see the output, for example printing some message, appear below. If you launch it like this, you will not be able to do anything else on this terminal tab until the code finishes running.

- ```python code.py```
  - Puts the process in the background, so that you can continue to use the same terminal tab. A number will appear when you do this, allowing you to identify this job when you do top.  If you code has any outputs, they will continue to appear just below.
  
- ```nohup python code.py```
  - In the above options if you logout of your session, or it suddenly closes due to connection problems, your job will stop. nohup is a way to stop this from happening. 

- ```nohup python code.py > nohup.out &```
  - In the above option the outputs of your job will still appear below. This option writes any outputs in a file, nohup.out in this case.  Recall outputs don’t refer to any figures the code generates, but can be any errors in your code.
  
- ```nohup python -u code.py > nohup.out &```
    - Avoids output buffering, i.e. make sure the output of your code is written in near real time.
    
- ```nohup python -c 'import code; code(input1, "input2")' > nohup.out &```
  - If your code is a function, and you need to give some input variables, a number or an array (input1) or a string ("input2")

**If necessary, remember to activate your environment before doing this!** (for example ```source activate venv_01```)
