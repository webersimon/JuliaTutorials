#!/usr/bin/env python
# coding: utf-8

# # Creating a Jupyter book

# In this section, I cover briefly how to create (and publish) a jupyter book. These notes are based on the excellent introduction available here https://jupyterbook.org/start/your-first-book.html. 

# ## Installing Python
# The easiest way to install Python is to download Anaconda or Miniconda. 
# 
# ## Switching to Python 3.7
# Unfortunately, there are issues when building a jupyter book when using more recent versions of python. To avoid this, we will use an older version of Python (python 3.7). To easily switch between versions of python, we will create a specific environment which will contain python 3.7. To do this, we open the Anaconda Prompt and type
# ```
# conda create --name python37 python=3.7
# ```
# where "python37" is the name we give to that environment (could be anything). 
# To activate this envrionment, we open the Anaconda Prompt and type
# ``` 
# activate python37
# ```
# and to check the version of python being used
# ```
# python -V
# ```
# 
# ## Creating a GitHub repository for the book
# 1. Create an account on GitHub
# 2. Create a public repository for the book, for example "mynewbook"
# 3. Install GitHub desktop (useful to sync changes made to the book) and clone the book repository.
# 
# ## Creating the book
# 1. Open Anaconda Prompt and activate an environment containing python 3.7
# 2. Install Jupyter book
# ```
# pip install -U jupyter-book
# ```
# 3. Create the book 
# ``` 
# jupyter-book create mynewbook/
# ```
# This will create an example book with a basic structure that we can then edit to our liking. 
# 
# 4. Locate the book files that have just been created and move them to the GitHub repository. We can now edit these files (that is, write the book) and push any changes to the main branch of our Github repository.
# 
# ## Building the book in HTML format
# To build the book (in an environment with python 3.7), we run
# ```
# jupyter-book build path_to_book
# ```
# 
# 
