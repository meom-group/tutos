# Data analysis software used in MEOM group and how to learn it.

authors : Julien Le Sommer, Aurélie Albert and Redouane Lguensat (MEOM group, IGE)

*This page provides a curated list of software used for data analysis in the MEOM group, online resources on how to use it and general advice on how to proceed with ocean data analysis. Please, keep in mind that (i) this list is not exhaustive and that (ii) it may evolve with time.*

## General advice

A nice mental picture for understanding most of our data analysis tasks is the **notion of data analysis pipeline**. Our data analyses generally combine several steps, all corresponding to individual pieces of software. Our data flows through the pipeline and gets transformed at each step by a particular piece of software. Ideally these pipelines shoud be as **automated** as possible so that our work is easily **reproducible**. 


A key principle for building data analysis pipelines is to try to **rely as much as possible on pre-existing software**. In practice, most of the steps in an analysis pipeline are very generic (as eg. reading/writing/plotting data) so that we can just use preexisting code. So a large fraction of our work just involves glueing together existing pieces of code. This is why modern software is now made as modular as possible. 

If you need to write new code, it should **focus in priority on what is specific** to your analysis. Some building-blocks of your data analysis pipeline are indeed more specific to your needs than others. For these key specific steps, you might have to write a dedicated module, but you should always first wonder if someone has already implemented something close to what you need. 

Knowing what is currently feasible with your sofware environment is therefore key for designing your own analyses. This requires your keeping **a routine curiosity for software**. In practice, this requires your spending time going through online videos and tutorials (because you learn better through examples). This also requires your being aware of minimal [good practices](https://arxiv.org/abs/1609.00037) in scientific computing. 

In this page, you will find a **curated list of software**, tutorials and examples that we hope will improve your awareness of your technological environment. Do not hesitate to suggest new links and update to this page.


## Recommanded base configuration
To work with the MEOM group, you will need this minimal software configuration and set-up: 

 -  install [anaconda](https://docs.continuum.io/anaconda/) (python distribution and package manager) and learn how to use it
   - learn how to manage [conda environments](http://conda.pydata.org/docs/using/envs.html)
 - install [git](https://git-scm.com/) (software version control manager), create a [github](https://github.com/) account and learn how to use it : 
  - [cloning] (https://help.github.com/articles/importing-a-git-repository-using-the-command-line/) a repository
  - using [gist](https://help.github.com/articles/creating-gists/)
  - using [pull requests](https://help.github.com/articles/using-pull-requests/) (**advanced**)
  

Caution : you may need to configure git to work through our network proxy.



## Software engineering
Resources on *how to better interact with your computer* (**basic**). 

 * unix operating system: [software carpentry tutorial](http://swcarpentry.github.io/shell-novice/)
 * automation and make : [software carpentry tutorial](http://swcarpentry.github.io/make-novice/), [SCons](http://scons.org/)
 * version control with git: [software carpentry tutorial](http://swcarpentry.github.io/git-novice/), [becoming a git guru](https://www.atlassian.com/git/tutorials/)

Resources on *how to build and distribute software* (**advanced**): 

 * packaging and distrubuting python projects : [user guide](https://packaging.python.org/ ), [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
 * testing and continuous integration : [software carpentry tutorial](http://katyhuff.github.io/python-testing/), [travis-ci](https://travis-ci.org/)
 * documenting your projects : A guide to python documentation with [numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt), [readthedocs](https://readthedocs.org/), write the docs [community](http://www.writethedocs.org/)
 * a blog post of [templates for python command line scripts](https://zduey.github.io/tips/the-funnel-method/)

## Jupyter notebooks
Jupyter notebooks are great for sharing your work because they allow to mix code, text and visualization in the same document. Because Jupyter notebooks can understand code in different languages, they are also great for building an complex data analysis pipelines.
**We therefore strongly recommend using Jupyter Notebooks**.

  * official [documentation](https://jupyter.readthedocs.io/en/latest/index.html)
  * using the [ipython](http://nbviewer.jupyter.org/github/ipython/ipython/blob/4.0.x/examples/IPython%20Kernel/Index.ipynb) kernel
  * sharing notebooks with [nbviewer](http://nbviewer.jupyter.org/)
  * recommanded [best practices](https://www.youtube.com/watch?v=JI1HWUAyJHE) with Jupyter notebooks
  * Jupyter notebooks [tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
  * examples from [the Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks), and from [the group](https://github.com/lesommer/notebooks)
 * building reproducible analysis pipelines with [nbflow](https://www.youtube.com/watch?v=Fc2W930NJs8) (**advanced**)
 * diffing and merging notebooks with [nbdime](http://nbdime.readthedocs.io/)
 
## Python language

### Basic scientific python 
For people who have never used python before : 

  * Introduction to python through examples : 
    * [software carpentry tutorial](http://swcarpentry.github.io/python-novice-inflammation/)
    * [mode analytics lessons](https://community.modeanalytics.com/python/)
  * [numpy](http://www.numpy.org/) is the fundamental package for scientific computing with Python : [tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html). Here is a [collection of resources](https://community.modeanalytics.com/python/libraries/numpy/) on numpy. [From python to numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/) includes a lot of examples [codes](https://github.com/ocefpaf/from-python-to-numpy/blob/master/README.md) and links to [tutorials](http://www.labri.fr/perso/nrougier/from-python-to-numpy/#tutorials)
  * [scipy](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)  is a Python library used for scientific computing and statistical analysis. Here is a [collection of resources](https://community.modeanalytics.com/python/libraries/scipy/) on scipy.
  * more python examples :  from the [Python Data Science HandBook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/code_listings), from [earthpy website](http://earthpy.org/), see also the [scipy lecture notes](http://www.scipy-lectures.org/)


### Geoscientific data analysis in python :

*We strongly recommand using the following packages.*

  * There are several interfaces for handling  netcdf files in python. Here is a tutorial to [NetCDF4](http://unidata.github.io/netcdf4-python/) interface.
  * [pandas](http://pandas.pydata.org/pandas-docs/stable/) is a great package for handing time series and labelled data in python, here is a [10min tour](http://vimeo.com/59324550) to pandas. See also this [example](http://earthpy.org/time_series_analysis_with_pandas_part_2.html) . Here is a [collection of resources](https://community.modeanalytics.com/python/libraries/pandas/) on pandas. See also this [brief introduction](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python). Example of [timeseries analysis with pandas](http://earthpy.org/pandas-basics.html)
  *  [xarray](http://xarray.pydata.org/) implements a N-dimensional variants of the core pandas data structures.  In practice, xarray provides an in-memory representation of the content of a collection of netCDF files.
    * official [documentation](http://xarray.pydata.org/en/stable/) (with interesting links to videos and tutorials) : 
    * xarray tutorials [by S. Hoyer](https://gist.github.com/shoyer/d462cc3b2aeb87bbb78cc6f8207851c6#file-xarray-tutorial-with-answers-ipynb) and [by N. Fauchereau](http://nbviewer.jupyter.org/github/nicolasfauchereau/metocean/blob/master/notebooks/xray.ipynb)

  * [Dask](http://dask.pydata.org) is a flexible parallel computing library for analytic computing in python.
    * official [documentation](http://dask.pydata.org/en/latest/)
    * a good [introduction](https://www.youtube.com/watch?v=1kkFZ4P-XHg)
    * a [video](https://youtu.be/EEfI-11itn0?list=PLGVZCDnMOq0qLoYpkeySVtfdbQg1A_GiB) on parallel and distributed computing with dask 
    * some [examples](https://github.com/jorisvandenbossche/SWSC2016-pandas-dask)
    * slides on [visualizing parrallel computation](http://matthewrocklin.com/slides/plotcon-2016.html#/)
    * combining [xarray and dask](https://www.continuum.io/content/xray-dask-out-core-labeled-arrays-python)
    * QuickStart with [Dask.distributed](https://distributed.readthedocs.io/en/latest/)

  * [oocgcm](http://oocgcm.readthedocs.io/en/latest/) is a project that provides tools for processing and analysing output of general circulation models and gridded satellite data in the field of Earth system science.

### Machine Learning with python :
Recently, machine learning (ML) methods are leading to impressive performances in signal/image/vision fields, in particular, neural networks made a strong come-back thanks to a technique called deep learning (DL) [(Nature paper)](https://www.nature.com/articles/nature14539). Maybe you heard about AlphaGo the algorithm that beat the world champion in the game Go [(story)](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol), or you heard about the Microsoft team that developed an algorithm able to surpass Human-Level performance on classification of ImageNet a popular image dataset [(paper)](https://arxiv.org/abs/1502.01852). These are just a glimpse of what DL is doing right now, for more information, you can take a look at these excellent articles [1](https://www.technologyreview.com/s/513696/deep-learning/),[2](http://fortune.com/ai-artificial-intelligence-deep-machine-learning/). In our group we are starting to investigate the possibility of transferring the knowledge gained in the machine learning community to tackle ocean related inverse problems.

For newcomers into ML we strongly recommend Andrew Ng's ML [course](https://www.coursera.org/learn/machine-learning) (It's an old course so it still uses Matlab). Then the DL specialization suggested by Andrew Ng (again) is a great introduction to DL [(course)](https://www.coursera.org/specializations/deep-learning) (2017, so it's Python time!).

The following packages are mainly used by our team for ML:
  * [scikit-learn](http://scikit-learn.org/stable/): Built on top of NumPy, SciPy, and matplotlib, scikit-learn is the standard package used by industry and education for machine learning with Python. [Tutorials](http://scikit-learn.org/stable/tutorial/index.html) (FYI: It's first released version was done by INRIA researchers)
  * [Tensorflow](https://www.tensorflow.org): Developed by Google, TF is currently the most used Python library for DL according to Github pull requests history and Google trends and other metrics. Other libraries for DL in Python exist like [*Theano*](http://deeplearning.net/software/theano/) (historical library developed by MILA lab but stopped this year, R.I.P), [*Caffe*](http://caffe.berkeleyvision.org), [*CNTK*](https://docs.microsoft.com/fr-fr/cognitive-toolkit/) (developed by Microsoft), [*MXNET*](https://mxnet.incubator.apache.org) (Amazon) and finally [*PyTorch*](http://pytorch.org) (developed by Facebook) which is gaining ground and can be considered as a strong concurrent to TF.
  * [Keras](https://keras.io): Keras is a high-level neural networks API, that can run on top of TensorFlow. That means that's it's more "user friendly" than Tensorflow (allows easier prototyping, basically classical layers are ready-to-use with minimum code). In our group we rely on Keras since our work is about using existing techniques and adapting them to our applications. Some tutorials could be found [here](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/).
  
Some other useful links and material for further reading:
  * Course materials for the Data Science at Scale Specialization at Coursera https://github.com/AlessandroMozzato/datasci_course_materials
  * (French) Stéphane Mallat - Apprentissage par invariants en grande dimension https://www.youtube.com/watch?v=kgicutzlq50
  * Machine learning with sklearn, lecture https://www.youtube.com/watch?v=Cte8FYCpylk
  * Machine learning for time series data in Python https://www.youtube.com/watch?v=ZgHGCfwExw0
  * Machine Learning for Analyzing Complex Time Series https://www.youtube.com/watch?v=UxJB_5PyKTI
  * Jupyter notebooks for the code samples of the book "Deep Learning with Python" https://github.com/fchollet/deep-learning-with-python-notebooks

### Data visualization with python :
There are currently too many libraries for visualizing data with python (see this [python data vizualization tour](https://dansaber.wordpress.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/)), this may seem exciting or overwhelming depending on the point of view... In practice, you should distinguish libraries that focus on *interactive data visualization* (great for investigating your datasets in Jupyter notebooks) and libraries that focus on *static data visualization* (needed for writing papers and reports). Several of the more recent visualization libraries in python
implement concepts from the [*Grammar of graphics*](http://www.springer.com/us/book/9780387245447). 

  * **General purpose visualization:** 
 	 * *static visualization* : 
      * [matplotlib](http://www.matplotlib.org/) is the standard 2D and 3D plotting library for python. See this [tutorial](http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)
      * [seaborn](http://seaborn.pydata.org/) is a great to matplotlib for statistical data vizualisation with python (default plots look good with seaborn) : [tutorial](http://seaborn.pydata.org/tutorial.html), [examples](http://seaborn.pydata.org/examples/index.html), here is a nice [collection of ressources](https://community.modeanalytics.com/python/libraries/seaborn/). (note that seaborn is well integrated in holoviews)
      * [ggplot](http://ggplot.yhathq.com/) is a plotting system for Python based on R's ggplot2 and the Grammar of Graphics. see also this [video](www.youtube.com/watch?v=pHrwqLhAaMw)
      * [altair](https://github.com/ellisonbg/altair) is a new declarative statistical visualization library : [documentation](https://github.com/ellisonbg/altair), [tutorial notebook](https://github.com/ellisonbg/altair/blob/master/altair/notebooks/01-Index.ipynb)

    * *interactive visualization (within Jupyter notebooks)*
      * [HoloViews](http://holoviews.org/)  lets you store your data in an annotated format that is instantly visualizable, with immediate access to both the numeric data and its visualization : [video demo](https://www.youtube.com/watch?v=0jhUivliNSo), [video demo](https://www.youtube.com/watch?v=hNsR2H7Lrg0), [example notebooks](https://github.com/ioam/holoviews-contrib), list [holoviews elements](http://holoviews.org/Tutorials/Elements.html), holoview for visualizing [distribution data](http://holoviews.org/Tutorials/Pandas_Seaborn.html).
      * [Bokeh](http://bokeh.pydata.org/en/latest/) is an interactive data visualization library that implements the grammar of graphics : [example gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html#gallery), [notebook gallery](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/index.ipynb), [video demo](https://www.youtube.com/watch?v=c9CgHHz_iYk) [](http://www.pyvideo.org/video/1224/bokeh-an-extensible-implementation-of-the-gramma)
      * [bqplot](https://github.com/bloomberg/bqplot) is a Grammar of Graphics-based interactive plotting framework for the Jupyter notebook. 
      * plotly is another interactive visualization library, probably more oriented to making charts and dashboard for companies: [documentation](https://plot.ly/python/offline/), [examples](https://plot.ly/python/)

  * **Visualizing geographical data** :
 	 * *static visualization* : 
      * [Basemap](http://matplotlib.org/basemap/) is an extension to matplotlib that allows to plot geographical data:  [documentation](https://basemaptutorial.readthedocs.io/en/latest/)
      * [Cartopy](http://scitools.org.uk/cartopy/) provides cartographic tools for python (developped by the MetOffice) : [documentation](http://scitools.org.uk/cartopy/docs/latest/index.html)

   * *interactive vizualization (within Jupyter notebooks)* :
      * [GeoViews](http://geo.holoviews.org/)  (*recommended*) is built on HoloViews. It allows to explore and visualize geographical  data interactively. Works nicely with xarray : [demo](https://www.continuum.io/blog/developer-blog/introducing-geoviews),  [examples](http://geo.holoviews.org/index.html), see also how to work with gridded data with geoviews [part 1](http://geo.holoviews.org/Gridded_Datasets_I.html) and [part 2](http://geo.holoviews.org/Gridded_Datasets_II.html)

  * **How to choose a colormap**: 
   * see this resourtce on [perceptually uniform colormaps](http://peterkovesi.com/projects/colourmaps/), 
   * see this discussion for a [better default colormap for matplotlib](http://bids.github.io/colormap/)
   * check out these useful colormaps : [colorcet](https://github.com/bokeh/colorcet), [cmoceans](https://plot.ly/python/cmocean-colorscales/)
   * see also this discussion colorbar manipulation for [bathymetry](http://pyhogs.github.io/colormap-bathymetry.html)
   * seaborn [color palette tutorial](http://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial)


### Optimizing python codes
Python is great for fast prototyping of production code. It also has the reputation of being rather slow as compared to other languages (as for instance Fortran, C or C++). There are therefore a lot of options for accelerating python code, with classical solutions generally involving  interfacing python code with faster languages. This is the general idea behind [f2py](http://www.f2py.com/), [Weave](https://docs.scipy.org/doc/scipy/reference/tutorial/weave.html), [Cython](http://cython.org/).  Although some of theses solutions can be very helpful for interfacing pre-existing legacy code, we here promote the use of [numba](http://numba.pydata.org/). Numba indeed gives you the power to speed up your applications with a few annotations  without having to switch languages or Python interpreters.


  * see this discussion on how to [optimize python code with numba, cython and fortran in jupyter notebooks with magics](https://ocefpaf.github.io/python4oceanographers/blog/2015/10/05/isosurfaces/)
  * see this blog post on the [optimization of non-uniform fourier transforms](https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/)
  * see this blog post on [accelerating python code with numba](https://www.continuum.io/blog/developer/accelerating-python-libraries-numba-part-1)
  * and this series of videos on numba  : [video1](https://www.youtube.com/watch?v=QpaapVaL8Fw), [video2](https://www.youtube.com/watch?v=eYIPEDnp5C4), [video3](https://www.youtube.com/watch?v=COglHpt7KSs)


### Other useful python packages and jupyter notebooks
  * Statistics in python with [statsmodels](https://github.com/statsmodels/statsmodels) : [documentation](http://statsmodels.sourceforge.net/stable/), [examples](http://www.statsmodels.org/stable/examples/index.html) 
  * [Image processing with python](http://www.scipy-lectures.org/advanced/image_processing/)
  * [Filtering and time series analysis with scipy.signal](https://docs.scipy.org/doc/scipy/reference/tutorial/signal.html)
  * [Python for probability, statistics and machine learning](http://nbviewer.jupyter.org/github/unpingco/Python-for-Probability-Statistics-and-Machine-Learning/tree/master/)
  * [Python for signal processing](http://nbviewer.jupyter.org/github/unpingco/Python-for-Signal-Processing/tree/master/)
  * [Machine learning with TensorFlow](https://github.com/BinRoot/TensorFlow-Book)
  * [PyMC3](https://github.com/pymc-devs/pymc3) Probabilistic modelling in python 
  * managing dates and time intervals [arrow](https://arrow.readthedocs.io/en/latest/).
 
## Other software used in MEOM group
(*section under construction*)

  * CDFTOOLS : https://github.com/meom-group/CDFTOOLS
  * DCM : https://servforge.legi.grenoble-inp.fr/projects/DCM
  * mkmov
  


