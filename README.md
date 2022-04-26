# campvideo-data
Replication data for ["Automated Coding of Political Campaign Advertisement Videos: An Empirical Validation Study"]() by Alexander Tarr, June Hwang, and Kosuke Imai.

## Overview
Full replication of the results in the paper is a laborious process, involving significant setup and computation time on the part of the user. To simplify the procedure, we have split replication into two parts: [Feature Extraction](#Feature-Extraction) and [Validation](#Validation). For those seeking only to validate the results in the paper, it is **highly recommended** to ignore feature extraction and follow the steps for validation, which uses pre-computed features from the feature extraction step.

## Repository Layout
This repository is split into several folders: ``data``, ``figs``, ``results``, ``scripts`` and ``tables``.
- ``data``: This folder contains all data needed to perform both feature extraction and validation.
  * ``ids``: Numpy vectors for face encodings corresponding to Senate candidates in the 2012 and 2014 elections.
  * ``intermediate``: Extracted feature data for each YouTube video in the study. This data includes Numpy vectors for audio features, keyframe indices, auto-generated transcripts, and detected image text. Data in this folder is created in the [Feature Extraction](#Feature-Extraction) step.
  * ``mturk``: CSV files containing results from the Amazon Mechanical Turk studies.
  * ``validation``: CSV files results from the validation analyses given in the appendix.
  * ``videos``: MP4 files corresponding to YouTube videos used in the study. Data in this folder is used in the [Feature Extraction](#Feature-Extraction) step.
  * ``wmp``: DTA files containing WMP/CMAG data. Data in this folder is used in the [Validation](#Validation) step.
- ``figs``: PDFs for figures generated by the code that are displayed in the paper.
- ``results``: CSV files containing predicted labels for tasks studied in the paper. There are also raw text files showing general statistics about the performance of our methods that are discussed in the main text of the paper.
- ``scripts``: All code needed to generate data, extract features, validate results, and create figures and tables.
-  ``tables``: Raw text files showing confusion matrices corresponding to tables in the paper.

## Data
Replication relies on two datasets. [Feature Extraction](#Feature-Extraction) requires the collection of YouTube videos in MP4 format, while [Validation](#Validation) requires the human-coded labels provided by WMP. Unfortunately, neither of these datasets can be provided publicly.

- YouTube Videos: We provide a list of the YouTube Video IDs used in the study in <JUNE'S FILE: TBD>. Users able to obtain these videos should place them in the ``data\videos`` folder, with each video file titled ``<YouTubeID>.mp4``. ``<YouTubeID>`` is the unique YouTube video ID.
- WMP Data: The WMP data can be purchased [here](https://mediaproject.wesleyan.edu/dataaccess/). Our study used the 2012 Presidential, 2012 Non-Presidential, and 2014 data. The data is distributed across 7 Stata files, one for each year and race type (House, Senate, Governor, President). These files should be placed in the ``data\wmp`` folder.

## Validation

### Installation
Recreating all figures, tables and results in the [Validation](#Validation) step requires working installations of [Python](https://www.python.org/downloads/) and [R](https://cran.r-project.org/src/base/R-4/). All code in this repo was tested under Python version 3.9.7 and R version 4.0.5 on a Windows 10 machine. 

#### Python Dependencies
Most Python package dependencies can be installed by installing the project-related package, ``campvideo``, which is available on [TestPyPi package repository](https://test.pypi.org/project/campvideo/). This package can be installed within a Python environment via the command

    pip install -i https://test.pypi.org/simple/ campvideo

Additionally, the Python code depends on ``matplotlib, seaborn``, which can be installed via command line:

    pip install <PACKAGE_NAME>
    
#### R Dependencies
All R code uses the following packages: ``quanteda, readstata13, readtext, stringr, xtable``, which can be installed from within the R environment via via

    install.packages("<PACKAGE_NAME>")

#### spaCy Model Download
The ``spacy`` text modeling package requires downloading a model. After installing the Python packages, enter the following in the command line:

    python -m spacy download en_core_web_md
    
 

## Feature Extraction

## Additional Notes
