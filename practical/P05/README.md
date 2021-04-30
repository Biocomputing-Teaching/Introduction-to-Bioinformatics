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

After that, you'll need to configurate and install a number python modules (if not already installed) typing the below commands into your terminal (if conda does not work, try pip instead - or brew for mac users):

If your OS is linux, please type the following two commands in your terminal:

```
sudo apt-get update -y
```

```
sudo apt-get install -y tabix
```

For both linux and mac users, please type the following commands in your terminal.

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
pip install PyVCF
```

```
pip install seaborn
```

```
conda install numpy
```

```
pip install ipywidgets
```

```
conda install -c bioconda pyvcf
```


```
pip install https://github.com/khramts/assocplots/archive/master.zip
```

## What if...?

If when installing the pyvcf module via the conda command ''conda install -c bioconda pyvcf'' you get an error message saying the following or similar:

```
UnsatisfiableError: The following specifications were found

to be incompatible with the existing python installation in your environment:

Specifications:

  - pyvcf -> python[version='2.7.*|3.4.*|3.5.*|3.6.*']

Your python: python=3.8

```

Please follow the below procedure:

Go to a new terminal window and create a new environment named "snakes" that contains for example Python 3.5:

```
conda create --name snakes python=3.5
```

When conda asks if you want to proceed, type "y" and press Enter.

Then, activate the new environment by typing:

```
conda activate snakes
```

Since you have activated a new environment called "snakes", now you will see that your command line will start with (snakes) rather than (base) 

Then you can try installing the pyvcf module by typing in the same terminal with the new environment:

```
conda install -c bioconda pyvcf
```

Be aware that since you are in a new environment, you will need to install again jupyter notebook and all modules needed for this assignment in your new environment. I copy them again below just in case:

``´
conda install jupyterlab
```

``´
conda config --add channels bioconda
```

```
conda install numpy
conda install matplotlib
conda install biopython
```
```
conda install -c anaconda git
```

```
conda install tabix pyvcf
```

```
conda install -c anaconda pandas
```

```
pip install PyVCF
```

```
pip install seaborn
```

```
pip install ipywidgets
```

Then you are good to go and initialise jupyter notebook from this new environment.

*****************

The content of this notebook can also be consulted at the following link:

[05-WorkingWithVariationData.ipynb](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/blob/main/practical/P05/05-WorkingWithVariationData.ipynb)

