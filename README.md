# Introduction to Bioinformatics

## Welcome to the course!

This page is the official repository for the course "Introduction to Bioinformatics" of the Bachelor's Degree in Biomedical Science (Biomedicine) at the UIC.

The repository contains the material created or adapted from other (referred) sources for a first introduction to the field of Bioinformatics, using Python and R programming languages. 

## Getting started

To work in bioinformatics means to work with computers. As a necessary step, you'll need to learn how to use computers to get insight from biological data. By "use computers," we mean to grasp the full potential that computers can offer to assist you in gathering, creating, and analyzing data. These tasks are achievable at their best by learning to write your own programs, so they will suit the specific needs to answer your scientific questions. We will learn how to make small scripts along with the content of the course. However, most programming learning will be part of your own effort; programming is a language, we can show you how it works, but it is up to you how you learn it, speak it, and put it to good use.

### Preparing the tools

Before we start with the course's practical session, you must have everything set up and ready to work. Our primary language will be Python, a general programming language that is more ubiquitous by every day. Many platforms can host a python interpreter, but since this is not the only application we will use in this course, we will need a shared operating system among all the course attendants. For this, we choose Linux since most of the scientific applications are developed for it.

Linux and macOS are very similar since both have similar architectures. Many Linux programs are also available for macOS users...

There are several ways to install Linux. One way is using it as your primary operating system, doing everything you usually do but now using Linux.

[How to set up a computer with dual-booting](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/)

Also, there are ways of having more than one operating system in your personal computer that you can select at the startup menu (when you turn on your computer). If you have a Windows computer, this could be an option.

[How to set up a Linux virtual machine for Windows](https://www.thomasmaurer.ch/2019/06/how-to-create-an-ubuntu-vm-on-windows-10/)

Finally, if you don't want a second operative system on your computer, you can just set up a Linux virtual box. 

### Installing the required programs

We will need to install the [Conda](https://docs.conda.io/en/latest/) package manager:

[Documentation for installing Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

After installing Conda, we will install several packages needed for our sessions. Open up a terminal and execute the following:

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

That's it for now. Although, during the course, we will install and create other programming packages along we are needing them.


### Getting yourself ready

After setting up your computer, it is time to prepare yourself with some programming knowledge. If this is your first time using a console on a Linux computer, you better read this tutorial to learn some basic bash language and how to operate a command-line terminal (Note: macOS also uses bash language to operate its terminal):

[Basic Linux tutorial](https://ryanstutorials.net/linuxtutorial/)

If you have some experience and have already finished the Basic Linux tutorial, please read the following:

[Basic bash scripting tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)

For Python, we ask you reading at least the "Learn the Basics" entries in the following link:

[Python tutorial](https://www.learnpython.org/en/) 

The deeper you go, the better programmer you'll become! A good programmer will go swiftly along "Introduction to Bioinformatics", not to mention that later you could apply this knowledge when delving into any other professional problems. 

IMPORTANT: if you want to clone this repository on your computer (not needed, as you can download individual files), you can install [GitHub Desktop](https://desktop.github.com) to make it the easy way.

## Sessions

The course will be divided into theoretical, practical, and methodological cases. Here, you will find the necessary information for each one of those sessions:

### Theoretical sessions

[T01 - Theoretical session 01](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/theoretical/T01)

### Practical Sessions

[P01 - Working with sequence data](https://github.com/Biocomputing-Teaching/Introduction-to-Bioinformatics/tree/main/practical/P01)

### Case Sessions



