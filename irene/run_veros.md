# Run VEROS on Irene

[VEROS](https://veros.readthedocs.io/en/latest/index.html) is an ocean model written entirely in python and optimized with jax.

## Download Veros and dependencies

Irene does not have a direct access to internet so you need to do these steps on another machine with access to internet (dahu for instance) :

```
git clone https://github.com/team-ocean/veros.git -b main
python3 -m venv venv-veros
source venv-veros/bin/activate
pip install -e ./veros[jax]
```

Then scp both veros and venv-veros on Irene
