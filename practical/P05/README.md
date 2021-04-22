# Practical Session 05

## Requirements

* Setting up your computer with a Linux or macOS operating system (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install Conda (see [course repository](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics))
* Install pandas, pyVCF (see below)
* Complete the practical sessions 01 to 04.

## To begin

In this session, we will start working with sequence variation data using Python.

All Python concepts from previous sessions are needed, so please review them before coming to the session. It is an excellent idea to review these critical concepts by revisiting the Python tutorial:

- [Python basic tutorial](https://www.tutorialspoint.com/python/index.htm)

To start the session, you'll need the files inside the P05 folder in this repository. To do that is better to have the full repository cloned in your computer:

On your terminal, navigate to a location where you want to download the course repository and execute:

```
git clone https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics.git
```
This command will create a folder named "Introduction-to-Bioinformatics" containing the full repository at its latest version.

Navigate to the Practical Session 05 directory:

```
cd Introduction-to-Bioinformatics/practical/P05
```

And open the Jupyter notebook inside this folder:

```
jupyter-notebook 05-WorkingWithVariationData.ipynb
```

After that, you'll need to configurate and install a number python modules (if not already installed) typing the below commands into your terminal (if conda does not work, try pip instead):

```
sudo apt-get update -y
```

```
sudo apt-get install -y tabix
```

```
conda config --add channels bioconda
```

```
conda install tabix pyvcf
```

```
conda install -c anaconda pandas
```
```
conda install numpy
```
```
conda install -c bioconda pyvcf
```

```
pip install https://github.com/khramts/assocplots/archive/master.zip
```
The content of this notebook can also be consulted at the following link:

[05-WorkingWithVariationData.ipynb](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/blob/main/practical/P05/05-WorkingWithVariationData.ipynb)

