# Introduction to Bioinformatics

## Welcome to the course!

This page is the official repository for the course "Introduction to Bioinformatics" of the Bachelor's Degree in Biomedical Science (Biomedicine) at the UIC.

The repository contains the material created or adapted from other (referred) sources for a first introduction to the field of Bioinformatics, using Python and R programming languages.

## Getting started

To work in Bioinformatics means to work with computers. As a necessary step, you'll need to learn how to use computers to get insight from biological data. By "use computers," we mean to grasp the full potential that computers can offer to assist you in gathering, creating, and analyzing data. These tasks are achievable at their best by learning to write your own programs, so they will suit the specific needs to answer your scientific questions. We will learn how to make small scripts along with the content of the course. However, most programming learning will be part of your own effort; programming is a language, we can show you how it works, but it is up to you how you learn it, "speak" it, and put it to good use.

### Preparing the tools

Before we start with the course's practical session, you must have everything set up and ready to work. Our primary language will be Python, a general programming language every day more ubiquitous. Many platforms can host a Python interpreter, but since this is not the only application we will use in the course, we will need a shared operating system among all the course attendants. For this, we choose Linux since most scientific applications are developed for it.

Linux and macOS are very alike since both have similar architectures. Many Linux programs are also available for macOS users. So, you can use the terminal application in your MacOS to follow the course for most purposes.

There are several ways to install Linux. One way is using it as your primary operating system and do everything you usually do but now using Linux. We recommend Ubuntu:

[Get Ubuntu](https://ubuntu.com/)

Besides, there are ways of having more than one operating system in your personal computer that you can select at startup (when you turn on your computer). If you have a Windows computer, this could be an option:

[How to set up a computer with dual-booting](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/)

Finally, if you don't want a second operative system on your computer, you can set up a Linux virtual box:

[How to set up a Linux virtual machine for Windows with Hyper-V](https://www.thomasmaurer.ch/2019/06/how-to-create-an-ubuntu-vm-on-windows-10/)

If the Hyper-V option is not available to your Windows system (it is not available for Windows Home edition), then you can try with:

[How to set up a Linux virtual machine for Windows with VirtualBox](https://itsfoss.com/install-linux-in-virtualbox/)

### Installing the required programs

First, we will need to install the [Conda](https://docs.conda.io/en/latest/) package manager:

[Documentation for installing Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

After installing Conda, we will install several packages needed for our sessions. Open up a terminal on your [Linux](https://www.lifewire.com/ways-to-open-a-terminal-console-window-using-ubuntu-4075024) or [Mac](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) and execute the following:

* Install [jupyter notebooks](https://jupyter.org/install):
```
conda install jupyterlab
```
* Other required Python packages:
```
conda install numpy
conda install matplotlib
conda install biopython
```

* Install [Git](https://git-scm.com/)
```
conda install -c anaconda git
```

If you are using Mac OS X you may be interested in installing [GitHub Desktop](https://desktop.github.com) aswell.

That's it for now. Although, during the course, we will install and create other programming packages along we need them.

### Getting yourself ready

After setting up your computer, it is time to prepare yourself with some programming knowledge. If this is your first time using a console or terminal, you better read this tutorial to learn some basic bash language and how to operate a command-line based terminal (Note: macOS also uses bash language to operate its terminal):

[Basic Linux tutorial](https://ryanstutorials.net/linuxtutorial/)

If you have some experience and have already finished the Basic Linux tutorial, please read the following:

[Basic bash scripting tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)

Importantly, for Python, we ask you to read and familiarize yourself with at least the "Learn the Basics" entries in the following link:

[Python tutorial](https://www.learnpython.org/en/)

The deeper you go, the better programmer you'll become! A good programmer will go swiftly along "Introduction to Bioinformatics," not to mention that later you will be able to apply all this knowledge when delving into other professional problems. You can also find material developed in-house [here](https://github.com/Biocomputing-Teaching/Learning-Python-for-Biocomputing).

IMPORTANT: if you want to clone this repository on your computer (not needed, as you can download individual files), you can install [GitHub Desktop](https://desktop.github.com) to make it visually easy.

## Sessions

The course will be divided into theoretical, practical, and methodological cases. Here, you will find the necessary information for each one of those sessions. Please read the information within each appropriate link before you come to a particular session:

### Theoretical sessions

[T01 - Theoretical session 01](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/theoretical/T01)

[T02 - Theoretical session 02](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/theoretical/T02)

[T03 - Theoretical session 03](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/theoretical/T03)

### Practical Sessions

[P01 - Working with sequence data](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/practical/P01)


### Case Sessions

Happy programming!
