# Software used  in MEOM and how to learn it

Here are some useful hints on how to process your data in order to produce science.
The main idea is that we learn a tool more easily with examples.
Also when you want to do something, someone somewhere faced the same issue and maybe already found an answer to it.
So before reinventing the wheel, let's have a look at what others came up with.


## Unix / software engineering
* unix : http://swcarpentry.github.io/shell-novice/
* git version control : http://swcarpentry.github.io/git-novice/

## Fortran

## Bash

## Python

### Python basics 
For people who have never used python or a refreshment for people that have ...

  * Introduction through examples : http://swcarpentry.github.io/python-novice-inflammation/
  * Examples from the Python Data Science HandBook : https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/code_listings

### Optimizing python
  * numba
  * cython

### Advanced python for geosciences :

  * handling netcdf files
  * xarray : 
    * official documentation with interesting links to videos and tutorials inside : http://xarray.pydata.org/en/stable/
    * github repository : https://gist.github.com/shoyer/d462cc3b2aeb87bbb78cc6f8207851c6
  * dask :
    * official documentation : http://dask.pydata.org/en/latest/
    * a good introduction : https://www.youtube.com/watch?v=1kkFZ4P-XHg
  * combining xarray and dask :
    * https://www.continuum.io/content/xray-dask-out-core-labeled-arrays-python

* Plotting libraries :
  * non geosciences oriented : https://dansaber.wordpress.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/
    * matplotlib
    * plotly
    * seaborn
  * geosciences :
    * basemap : https://basemaptutorial.readthedocs.io/en/latest/
    * cartopy : http://scitools.org.uk/cartopy/docs/latest/index.html
    * holoviews
    * geoviews : https://www.continuum.io/blog/developer-blog/introducing-geoviews

* Home python tools
  * oocgcm : http://oocgcm.readthedocs.io/en/latest/

* Distribution & packaging of tools : continuous integration, conda, yml, documentation, numpydoc, travis CI : http://katyhuff.github.io/python-testing/

## Jupyter
Useful tool to tell a computational story from your data, or to produce publishable code.

  * Official documentation : https://jupyter.readthedocs.io/en/latest/index.html
  * Some notebooks from the team : https://github.com/lesommer/notebooks
  * How to install it at MEOM : https://github.com/auraoupa/personnal_tutos/blob/master/jupyter.md

## Other useful tools/links
  * CDFTOOLS : https://github.com/meom-group/CDFTOOLS
  * DCM : https://servforge.legi.grenoble-inp.fr/projects/DCM
  


## practical informations when joining MEOM
  * proxy
  * install of tools
