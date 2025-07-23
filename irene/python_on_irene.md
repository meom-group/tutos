 - create a python env on Irene :

```bash
module load python3/3.10.6
python3 -m venv myNEMO --system-site-packages
source myNEMO/bin/activate
```

 - on another cluster (ex ige-calcul1) install same version of python and create myNEMO env the same way and download the libraries with : ```pip download inquirer``` it will download a bunch of whl files that you will copy to irene
 - on Irene install the libraries from the whl files with pip : ```pip install blessed-1.21.0-py2.py3-none-any.whl``` (attention l'ordre peut être important...)
 - attention à ne pas bouger le répertoire contenant l'environnement, il faudra tout réinstaller !

 
