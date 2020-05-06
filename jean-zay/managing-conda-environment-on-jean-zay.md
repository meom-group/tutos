# How to manage conda environments on jean-zay

 - If you only deal with one project, same as usual, no specific problem.

 - If you deal with several projects (only one login)
    - you may want to use a conda environments built in one project in another project
    - but since the $WORK variable is relative to the project you are currently working in, you can get the error message : ```Could not find conda environment````
    - to solve this, the solution is to copy the file environments.txt from ```$WORK_of_the_project_where_you_build_the_env/.conda``` to ```$WORK_of_the_project_where_you_want_to_use_it/.conda```, alternatively you also have the environments.txt file on your $HOME.
    
    
