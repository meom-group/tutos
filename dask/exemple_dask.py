# 15/03/23
# Hugo Jacquet
# Script exemple d'une utilisation de dask
# 	pour appliquer une fonction utilisateur
#	à un fichier lourd.
#
#
# Lancer le script avec : python3 Script_exemple_dask.py
#
# Pour une utilisation en notebook, enlever les "print"
# 	et la mesure du temps peut se faire avec %%time
#

import pandas as pd, numpy as np
import numpy as np
import time

import dask.array as da
from dask.diagnostics import ProgressBar
import xarray as xr
import dask
from dask.distributed import Client, LocalCluster


		
def T_to_Theta_ufonc(T,P): 
	#Renvoie la température potentielle en K
	#IN : Température (K)
	#     Pression (Pa)
	#OUT : Theta (K)	
	R=287 #J.K-1.kg-1
	P0=100000 #Pa
	Cp=1004.5 #J.K-1.kg-1
	return T*(P0/P)**(R/Cp) # K
	
@dask.delayed # Nécessaire pour utiliser .compute() de dask
def T_to_Theta(T,P): 
	return xr.apply_ufunc(
		T_to_Theta_ufonc,
		T,
		P,
		dask="parallelized",
		output_dtypes=[float],
	)
		
if __name__ == "__main__":	# Nécessaire pour exécuter un script en //. Je ne sais pas si c'est nécessaire en notebook

	# Dask progress bar
	# 	fonctionne bien en jupyter notebook mais pas en script
	if False:
		

		a = da.random.normal(size=(10000, 10000), chunks=(1000, 1000))
		res = a.dot(a.T).mean(axis=0)

		with ProgressBar():
		    out = res.compute()

	# Test Dask sur fonction de conversion T to Theta    
	if False:
		#=============== User Input =================#
		P=1			# 0 : sans dask, 1 : avec dask
		Generate_Data = False
		# size,Nc_shape_xy,Nc_shape_t,times = 200,50,1000,100000 
		#	=> fichier de 64Go, attention à la ram dispo de votre ordi
		size=200
		Nc_shape_xy=50
		Nc_shape_t=1000
		times=100000
		
		name = "test_file_3.nc" # Nom du fichier test
		shape=(size,size)
		n_workers=8		# A changer selon la machine
		#============================================#
		
		
		if Generate_Data:
			# On construit des données factices
			space=[i for i in range(size)]
			Coords_time = pd.date_range("1900-01-01", periods=times)
			
			# On génère un volume 3D de température 20°C, sur times pas de temps
			T = xr.DataArray(283*np.ones((times,size,size)),
					name='T',
					coords=[Coords_time,space,space],
					dims=['time','x','y'])
			# On génère un volume 3D de pression 500Hpa (5500m), sur times pas de temps
			Pr = xr.DataArray(500*100*np.ones((times,size,size)),
					name='P',
					coords=[Coords_time,space,space],
					dims=['time','x','y'])
			print(T)
			print(Pr)
			ds = xr.merge([T,Pr])	# on combine les 2 variables
			ds.to_netcdf(name)	# Ecriture du fichier
		if P==0:
			# Sans dask
			# 227s file_test3
			start_time = time.time()
			ds = xr.open_dataset(name)
			print('* taille fichier %.3f GB' % (ds['T'].data.nbytes / 1e9 *2))	#  taille en GB
			Theta = T_to_Theta_ufonc(ds['T'],ds['P'])				# Ici on charge tout en mémoire
			print('* Temps de calcul sans dask =',time.time()-start_time,'s')	
			
		elif P==1:
			# avec dask et cluster sans persist
			# 12s test_file3
			start_time = time.time()
			# Démarrer un cluster local
			# On peut observer la charge des workers par le dask status : 
			# 	http://localhost:8787/status par défaut si machine locale
			cluster = LocalCluster(n_workers=n_workers) 
			client = Client(cluster)							# explicitly connect to the cluster we just created
			print(client)									# Affiche l'adresse du dask status si utilisé en notebook
			
			ds = xr.open_dataset("test_file.nc", 
					chunks={"time": Nc_shape_t,"x":Nc_shape_xy,'y':Nc_shape_xy})	# ici on découpe en temps ET en espace, c'est la que dask est introduit
			Theta = T_to_Theta(ds['T'],ds['P']) 						# Rien n'est calculé
			out = Theta.compute() 								# C'est ici que ca calcul
			print('Temps de calcul avec dask =',time.time()-start_time,'s')
		else:
			print('')	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
