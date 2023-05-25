import matplotlib.pyplot as plt
import xarray as xr
from scipy.ndimage import gaussian_filter
import numpy as np

ds = xr.open_dataset('/home/jacqhugo/scripts/simu_alex/MEAN_T/NO_DELETE/MEAN_FIELDS.nc')
ds_sst =  xr.open_dataset('/home/jacqhugo/WORKDIR/Alex_suite/AGHHR.1.T07h.004.nc')
# Data is 3D field of wind, dx=dy=50m, dz is variable.
# Size of the fields : (Z,Y,X)=(162,902,602), physical domain : (160,900,600)
# Halo = 1 (virtuals points used in the atmospheric code)


nj_coupe = 550 
edge = 1		# Data halo
leftni = 0		# left of the visualisation window
rightni = 599		# right of the visualisation window
figsize = (6,5)		# in inches
GAUSS_FILTER = True	# switch to see large scale or not
sigmax = 100		# here is the scale of filtered field (in indices), is also the size of the gaussian filter window
sigmaz = 1
jumpx,jumpz = 10,2	# jump to not see all arrows
cmap = 'rainbow'
dpi = 150

Z = ds.level[edge:-edge].values	# Altitude
X = ds.ni[edge:-edge].values	# Lat
Y = ds.nj[edge:-edge].values	# Lon
WindU_SS = ds.UT[edge:-edge,edge:-edge,edge:-edge].values # U wind full field
WindW_SS = ds.WT[edge:-edge,edge:-edge,edge:-edge].values # V wind full field
mean_U = ds.UT[edge:-edge,edge:-edge,edge:-edge].mean(axis=(1,2)).values # Horizontal mean of U
THTV = ( ds.THT[edge:-edge,edge:-edge,edge:-edge].values * 
				(1+0.61*ds.RVT[edge:-edge,edge:-edge,edge:-edge].values) )
# setting up the plot
fig, ax = plt.subplots(2,1,figsize = figsize,constrained_layout=True,dpi=dpi, gridspec_kw={'height_ratios': [3,1]}) # here first ax is 3/4 of the full height.

# filtering the windfield
U,V = np.zeros((Z.shape[0],X.shape[0])),np.zeros((Z.shape[0],X.shape[0]))
temp1= np.zeros(WindU_SS.shape)
if GAUSS_FILTER:
	for z in range(Z.shape[0]):
			temp1[z] = WindU_SS[z,nj_coupe] - mean_U[z] # Here we look only at deviation from mean wind
	U = gaussian_filter(temp1[:,nj_coupe,:],[sigmaz,sigmax])
	V = gaussian_filter(WindW_SS[:,nj_coupe,:],[sigmaz,sigmax])
else:
	for z in range(Z.shape[0]):
		U[z:] = WindU_SS[z,nj_coupe,:] - mean_U[z]
	V = WindW_SS[:,nj_coupe,:]

"""1rst plot"""
s = ax[0].pcolormesh(X[leftni:rightni]/1000,Z,WindW_SS[:,nj_coupe,leftni:rightni],cmap = 'bwr',vmin=-0.1,vmax=0.1) # Background is unfiltered vertical velocity
plt.colorbar(s,ax=ax[0])
# Arrows are filtered vertical velocity (= large scale wind)
# 	headlength and scale are set with trial and error.
#	V is x100 for visualisation, beware of reference arrow orientation.
Q = ax[0].quiver(X[leftni+jumpx:rightni:jumpx]/1000,Z[::jumpz],
			U[::jumpz,leftni+jumpx:rightni:jumpx],
			V[::jumpz,leftni+jumpx:rightni:jumpx]*100,
			angles='xy',pivot='mid',headlength=4.5,scale=100)
"""2nd plot"""
ax[1].plot(X[leftni:rightni]/1000,ds_sst['SST'][edge+nj_coupe,edge+leftni:edge+rightni]-273.15,color='k',label=r'SST (°C)')
ax[1].plot(X[leftni:rightni]/1000,ds.THTv[edge+1,edge+nj_coupe,edge+leftni:edge+rightni]-273.15,color='grey',label=r'$\theta_{v0}$ (°C)') # Potential temperature at first level

# Plot infos
ax[0].quiverkey(Q, 0.75, 0.03, 2, r'$\Delta Wind$=$2 m/s$', labelpos='E',coordinates='figure',angle=0) # Reference arrow
ax[1].set_xlabel('X (km)')
ax[0].set_ylabel('Altitude (m)')
ax[0].set_title('large scale wind and vertical velocity (m/s)')
ax[1].legend()
ax[0].tick_params(axis='both',top=True,right=True, labelbottom=False) # Turn off some tick labels
ax[1].tick_params(axis='both',top=True)
ax[0].set_ylim([0,800])
ax[1].set_xlim([X[leftni]/1000,X[rightni]/1000])
fig.savefig('LS_wind_and_WT_Y.png')
