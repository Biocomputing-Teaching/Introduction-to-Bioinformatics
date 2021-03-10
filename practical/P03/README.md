# Practical Session 03

## Requirements

* Setting up your computer with a Linux or macOS operating system (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install Conda and Jupyter Lab (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install CD-HIT command-line program
* Install MAFFT command-line program
* Install BioPython library
* Complete the practical session 01 and 02

## To begin

In this session, we will work with command-line programs (i.e., executed from the terminal) for clustering sequences by similarity (CD-HIT), and to do multiple sequence alignments (MAFFT). Also, we will see how to open this programs directly from Python functions. Finally, we will integrate the analysis of multiple sequence alignments using the BioPython library.

All Python concepts from previous sessions are needed, so please review them before comming to the session. It is a good idea review this key concepts by revisiting the Python tutorial:

- [Python basic tutorial](https://www.tutorialspoint.com/python/index.htm)

To start the session, you'll need to install the CD-HIT and MAFFT programs:

```conda install -c bioconda cd-hit```

```conda install -c bioconda mafft```

 Also, you need to get the files inside the P03 folder in this repository. To do that is better to have the full repository cloned in your computer:

On your terminal, navigate to a location where you want to download the course repository. This location should be different than the one used to clone the repository of previous practical sessions. Go to another location and execute:

```
git clone https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics.git
```

This command will create a folder named "Introduction-to-Bioinformatics" containing the full repository at its latest version.

Navigate to the Practical Session 03 directory:

```
cd Introduction-to-Bioinformatics/practical/P03
```

And open the Jupyter notebook inside this folder:

```
jupyter-notebook 03-MultipleSequenceAlignment.ipynb
```

The content of this notebook can also be consulted at the following link:

[03-MultipleSequenceAlignment.ipynb](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/blob/main/practical/P03/03-MultipleSequenceAlignment.ipynb)
