# Introduction to Flopy

This course provides a gentle introduction to Flopy. It is far from being a comprehensive course on all the intricacies and capacilities of the software. Rather, 
the course aims to provide the fundamental tools and knowledge to get you started. 

All exercises will employ MODFLOW 6 models. Although other MODFLOW variants are supported by Flopy, each has slightly different syntax. 
To keep things simple for the course, we will focsu on MOFLOW 6. Once the you are familiar with Flopy, it should not be too chalenging to apply the same principles to other MODFLOW variants.

## What will be covered
 - Installation
 - Basics of creating, running and displaying a very simple flow model
 - Setting up time-varying packages
 - Visualizing and post-processing model outputs.
 - A real-world case:
   - DISV grids and GRIDGEN
   - using external files during model construction (i.e. grid, BC locations, etc.)
   - the OBS package
   - loading and editing an existing model
   - adding a transport model
 - Some additional topics:
   - setting up the BUY package for density-coupled flow and transport
   - configuring multilayer wells with the MAW package

## Pre-requisites
 - Basic understanding of Python 
 - Basic understanding of Jupyter Notebooks
 - Basic understanding of MODFLOW 6
 - Basic understanding of common GIS file formats

Familiarity with git would be a bonus, but not fundamental.

## Installation Instructions

**Download the course repository:**

You can do this in one of two ways. 
 - (1) (easier) Download the repo as a zip file from here [https://github.com/rhugman/symple_flopy/archive/refs/heads/main.zip](https://github.com/rhugman/symple_flopy/archive/refs/heads/main.zip). Unzip the folder and work from there.
 - (2) (recommended; requires familiarity with git). Install git following directions here: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Sign-up for a git-hub account, then clone the repo [https://github.com/rhugman/symple_flopy](https://github.com/rhugman/symple_flopy).

**Install Python and dependencies:**
 - If you have already installed Python using Anaconda, you can skip this step. If not, install Anaconda https://www.anaconda.com/products/individual (or Miniconda, if you prefer https://docs.conda.io/en/latest/miniconda.html)
 - If you are using Windows: go to the start menu and open "Anaconda prompt". An anaconda command lline window will open. Navigate to the course repo folder on your machine. You can accomplish this by typing "cd *your folder path*" and pressing <enter>. Replace *your folder path* with the  path to the course material repo folder on your computer.
 - Next, type "conda env create -f environment.yml". This will create an anaconda environment called "symple" and install the python dependencies required for this course. It may take a while. Should you wish, you can inspect the **environment.yml** file in the repo folder to see what dependecies are being installed.

**Start jupyter notebook**
You will need to do this step any time you wish to open one of the course notebooks.
 - In Windows, open the Anaconda prompt. In Mac/Linux, open a terminal. Then, type "conda activate symple"
 - Next, navigate to the course materials reposiotry folder and type "jupyter notebook". A jupyter notebook instance should start within the course repo flder. You can now navigate to the "notebooks" folder and open one.
 
 
