# Python Notebook that traverses through the files

## Table of contents

* [Description](#description)
* [Technologies](#technologies)
* [Tools](#tools)
* [Installation](#installation)
* [Setup](#setup)
* [Maintainers](#maintainers)

## Description

This service is responsible to moniter input folder and logs all file entries into combined.csv

## Technologies

Project is created with:

* Python 3.8

## Tools

* Any IDE (for code editing)

## Installation

### python

With the command line open, type in the following command and press enter

```bash
python --version
```

Using the `--version` switch will show you the version that’s installed. Alternatively, you can use the `-V` switch

```bash
python -V
```

If python is not is not installed open a browser window and navigate to the Python.org and download setup file and install

## Setup

First of all clone this application

```bash
git clone
```

navigate to project folder

```bash
cd 
```

The virtualenv package is required to create virtual environments. You can install it with pip:

```bash
pip install virtualenv
```

To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘venv’, type the following:

```bash
virtualenv venv
```

You can activate the python environment by running the following command:

```bash
# ubuntu
source venv/bin/activate
```

```bash
# windows
.\\venv\\Scripts\\activate
```

After all required Installations and venv completed and activated, we need to execute this comment in terminal

```bash
pip install -r requirements.txt
```

once packages are installed we are free to start our application

```bash
# ubuntu
python3 run.py
```

```bash
# windows
python run.py
```

## Maintainers

1. Harnath Atmakuri (akvdkharnath@gmail.com)
