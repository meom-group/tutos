# Script running on cal1

## Running a python code:

For a python code, for e.g. code.py, you want to launch, these different options exist:

- ```python code.py```
  - Launches the python code (your job). You will see the output, for example printing some message, appear below. If you launch it like this, you will not be able to do anything else on this terminal tab until the code finishes running.

- ```python code.py arg1 arg2 arg3```
  - If your script takes arguments, specify them after the script name. Carefull, the type of the argument is specified in the parsing function of your script. For instance, if arg1 is used as a string in your code, you must not write the  quotation marks.
  
- ```python code.py &```
  - Puts the process in the background, so that you can continue to use the same terminal tab. A number will appear when you do this, allowing you to identify this job when you do top.  If you code has any outputs, they will continue to appear just below.
  
- ```nohup python code.py```
  - In the above options if you logout of your session, or it suddenly closes due to connection problems, your job will stop. nohup is a way to stop this from happening. 

- ```OMP_NUM_THREADS=n python code.py```
  - To restrict the computation to n threads. n should be less that the total number of threads (10 on cal1). Indeed, sometimes, python libraries use different threads to perfom some computations (e.g. numpy), and it can troublesome for other users of the machine. 
  
- ```nohup python code.py > nohup.out &```
  - In the above option the outputs of your job will still appear below. This option writes any outputs in a file, nohup.out in this case.  Of course, you can use any name for the output file (for instance output_exp1.txt). Recall outputs don’t refer to any figures the code generates, but can be any text message (through the print function) in your code.

- ```nohup python code.py > nohup.out  2>&1 &```
  -  The ```2>&1``` option allow to redirect also the errors in the output file. 

- ```nohup python -u code.py > nohup.out &```
    - Avoids output buffering, i.e. make sure the output of your code is written in near real time.
    
- ```nohup python -c 'import code; code(input1, "input2")' > nohup.out &```
  - If your code is a function, and you need to give some input variables, a number or an array (input1) or a string ("input2")

**If necessary, remember to activate your environment before doing this!** (for example ```source activate venv_01```)


