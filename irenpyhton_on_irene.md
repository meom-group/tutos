 - create a python env on Irene :

```bash
module load python3/3.10.6
python3 -m venv myNEMO --system-site-packages
source myNEMO/bin/activate
```

 - import source code of the module :

```bash
ssh -L 1234:irene-fr.ccc.cea.fr:22 alberta@ige-meom-cal1.u-ga.fr cat -
scp -P 1234 inquirer-3.4.0.tar.gz alberaur@127.0.0.1:/ccc/work/cont003/gen12020/alberaur/DEV/python-pckgs/. #in a different terminal, mv .ssh/known_hosts if need be
```
