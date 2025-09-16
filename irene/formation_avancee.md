# Formation Avancée

## Docker

 - a docker deamon for each user inside a virtual machine (pcocc)

```bash
pcocc docker alloc -p rome -c 32 --time=02:00:00
docker load -i $FORMATION_RESSOURCES/whalesay.tar
docker image list
docker inspect imagename
```

 - Dans un Dockerfie combiner les RUN pour réduire la taille des images

 - Better use Red Hat based image since Irene cluster runs on Red Hat
 - On peut déactiverles ENTRYPOINT et CMD à l'éxécution du docker

## Pcocc

Une surcouche pour utiliser docker, fonctionne un peu comme slurm


