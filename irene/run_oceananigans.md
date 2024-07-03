# Run oceananigans on Irene

[Oceananigans](https://github.com/CliMA/Oceananigans.jl) is a julia software that simulates incompressible fluid dynamics in Cartesian and spherical shell domains on CPUs and GPUs.


## To be done once

Irene does not have a direct access to internet so the julia environment needed to run oceananigans is provided via a docker image.

The docker image is stored at ```/ccc/work/cont003/gen12020/gen12020/oceananigans.tar``` so anyone in the gen12020 group should be able to access it.

The steps are : 
  - import the docker image : ```pcocc-rs image import docker-archive:/ccc/work/cont003/gen12020/gen12020/oceananigans.tar oceananigans```
  - check if the image is there : ```pcocc-rs image list```, you should get this answer :

![](docker.png)

  - copy the .julia stored in ```/ccc/work/cont003/gen12020/gen12020/juliadot.tar```in your homedir

## Everytime you wan to use oceananigans

  - In the interactive way : run the docker image with ```pcocc-rs run oceananigans```, this should launch a julia prompt in which you can run oceananigans following [this tutorial](https://github.com/CliMA/Oceananigans.jl?tab=readme-ov-file#running-your-first-model)
  - with a script : run your hello_world.jl script inside the docker image with ```pcocc-rs run oceananigans "hello_world.jl"```
