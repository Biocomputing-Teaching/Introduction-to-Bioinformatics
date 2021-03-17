# Practical Session 03

## Requirements

* Setting up your computer with a Linux or macOS operating system (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install Conda (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install ete3, etetoolkit, and ete_toolchain (see below)
* Create a new CONDA environment called ete3 (see below)
* Reinstall several packages inside the ete3 conda environment (see below)

* Complete the practical sessions 01 to 03.

## To begin

conda create --name ete3
conda activate ete3
conda install -c etetoolkit ete3 ete_toolchain
pip install -I ete3
conda install -c anaconda jupyter
conda install -c anaconda requests
conda install -c conda-forge scrapy
conda install -c conda-forge matplotlib

This session will work with the ETE command-line program to create phylogenetic trees from a fasta file. We will work by accessing, visualizing, and adding data to our phylogenetic tree.

All Python concepts from previous sessions are needed, so please review them before coming to the session. It is an excellent idea to review these critical concepts by revisiting the Python tutorial:

- [Python basic tutorial](https://www.tutorialspoint.com/python/index.htm)

To start the session, you'll need to create a new Conda environment called ete3:

```conda create --name ete3```

Then, we need to change our CONDA environment to the newly created one:

```conda activate ete3```

Inside this CONDA environment, you need to install the ete3 library

```conda install -c etetoolkit ete3 ete_toolchain```

Then, you need to install the command-line application with pip:

```pip install -I ete3```

Finally, you need to install several Python packages again inside this new environment:

```pip install -I ete3```

```conda install -c anaconda jupyter```

```conda install -c anaconda requests```

```conda install -c conda-forge scrapy```

```conda install -c conda-forge matplotlib```


 Also, you need to get the files inside the P04 folder in this repository. To do that is better to have the entire repository cloned in your computer:

On your terminal, navigate to a location where you want to download the course repository. This location should be different than the one used to clone the repository of previous practice sessions. Go to another location and execute:

```
git clone https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics.git
```

This command will create a folder named "Introduction-to-Bioinformatics" containing the whole repository at its latest version.

Navigate to the Practical Session 04 directory:

```
cd Introduction-to-Bioinformatics/practical/P04
```

And open the Jupyter notebook inside this folder:

```
jupyter-notebook 04-PhylogeneticTrees.ipynb
```

You can also consult the content of this notebook at the following link:

[04-PhylogeneticTrees.ipynb](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/blob/main/practical/P04/04-PhylogeneticTrees.ipynb)
