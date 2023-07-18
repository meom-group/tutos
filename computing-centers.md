

- scp to computing center through a tunnel :
  - in one local terminal : ```ssh -L 1234:adastra.cines.fr:22 alberta@ige-meom-cal1.u-ga.fr cat -```
  - in another terminal : ```scp -P 1234 u10_ERA5_surface_global_2017.nc aalbert@127.0.1:/lus/store/NAT/gda2307/aalbert/DATA_FORCING/ERA5/. ```
