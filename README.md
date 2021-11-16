# 1-Introduction

This repository contains files and example notebooks used during the [Groundater Modelling module of the Symple School of Hydrogeological Modelling](https://hydrosymple.com/en/programme/#module-3). Exercises are designed to be accompanied by the recorded lectures available through the Symple school. 

The repository covers three topics:
 - Introduction to Flopy
 - Model setup in complicated settings using MFSetup
 - Facilitating calibration and uncertainty analysis with pyEMU

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
 - Next, type "conda env create -f environment.yml". This will create an anaconda environment called "symple" and install the python dependencies required for this course. It may take a while. Should you wish, you can inspect the *environment.yml* file in the repo folder to see what dependecies are being installed.

**Start jupyter notebook**
You will need to do this step any time you wish to open one of the course notebooks.
 - In Windows, open the Anaconda prompt. In Mac/Linux, open a terminal. Then, type "conda activate symple"
 - Next, in the Anaconda prompt or terminal, navigate to the course materials reposiotry folder and type "jupyter notebook". A jupyter notebook instance should start within the course repo flder. Using the browser, you can now navigate to the "notebooks" folder and open one.
 
 
# 2-Introduction to Flopy

This course provides a gentle introduction to Flopy. It is far from being a comprehensive course on all the intricacies and capabilities of the software. Rather, 
the course aims to provide the fundamental tools and knowledge to get you started. 

The course is broken up into several exercises. Each exercise has its own jupyter notebook and accompanying video. Jupyter notebooks are in the "notebooks" folder of this repository. During the videos each of the exercises is completed. Completed versions of the notebooks can be found in the repository folder (these are the notebooks with "_completed" in the filename). 
 
All exercises will employ MODFLOW 6 models. Although other MODFLOW variants are supported by Flopy, each has slightly different syntax. 
To keep things simple for the course, we will focus on MOFLOW 6. Once the you are familiar with Flopy, it should not be too chalenging to apply the same principles to other MODFLOW variants.

## Exercises
1)	Ex01 – build, run and postprocess a simple model
2)	Ex02 – load and edit an existing model
3)	Ex03 – handling scalar data
4)	Ex04 – handling array data
5)	Ex05 – handling list data
6)	Ex06 – using the OBS utility
7)	Ex07 – transient simulations and using time-series input
8)	Ex08 – build a real world flow model
9)	Ex09 – adding a transport model
10)	Ex10 – creating a prediction model
 
# 3-MFSetup
 ...scripts and notebooks are found in the folder ..\notebooks\mfsetup
 ...
 
# 4-pyEMU
 ...scripts and notebooks are found in the folder ..\notebooks\pstfrom
 ...
