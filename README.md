# campvideo-data
Replication data for ["Automated Coding of Political Campaign Advertisement Videos: An Empirical Validation Study"]() by Alexander Tarr, June Hwang, and Kosuke Imai.

## Overview
Full replication of the results in the paper is a laborious process, involving significant setup and computation time on the part of the user. To simplify the procedure, we have split the replication process into two parts: [feature extraction](##-Feature Extraction) and [validation](##-Validation). For those seeking only to validate the results in the paper, it is highly recommended to ignore the feature extraction step and follow the steps for validation, which makes use of already-extracted features.

## Repository Layout
This repository is split into several folders: ``data``, ``figs``, ``results``, ``scripts`` and ``tables``.
- ``data``: This folder contains all data needed to perform both feature extraction and validation.
  * ``ids``
- ``figs``: PDFs for figures generated by the code that are displayed in the paper
- ``results``: CSV files containing predicted labels for tasks studied in the paper. There are also raw text files showing general statistics about the performance of our methods that are discussed in the main text of the paper.
- ``scripts``: All code needed to generate data, extract features, validate results, and create figures and tables
-  ``tables``: Raw text files showing confusion matrices corresponding to tables in the paper

## Validation

## Feature Extraction
