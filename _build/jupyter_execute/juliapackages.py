#!/usr/bin/env python
# coding: utf-8

# # Creating a Julia package

# In this section, I cover briefly how to create a Julia package (along with using GitHub). These notes are based on the Pkg package documentation (https://pkgdocs.julialang.org/v1/).
# 
# ## Creating a GitHub repository for the package
# 1. Create an account on GitHub
# 2. Create a public or private repository for the package, for example "example"
# 3. Install GitHub desktop (useful to sync changes made to the book) and clone the package repository.
# 
# ## Installing Julia
# Julia can downloaded at https://julialang.org/. A good IDE for Julia is Visual Studio Code (https://code.visualstudio.com/)
# 
# ## Creating the package
# In the Julia terminal, type "]" to enter the Pkg REPL. To create the package "example", type
# ```
# generate example
# ```
# Locate the folder "example" and copy the files (a "Project.toml" file which contain some useful information about the package such as the name, ID, dependencies, etc and a "src" folder that contains a Julia file "example.jl") to the GitHub repository.
# 
# ## Editing the package
# We can now edit the "example.jl" file and add the following to it:
# ```
# module example
# 
# fun() = println("This is the example package!")
# 
# end
# ```
# 
# ## Installing the package
# Once the package files have been edited, we need to commit any changes to the main branch of the GitHub repository. To install the package, type
# ```
# using Pkg
# Pkg.add(path="path_to_package")
# ``` 
# alternatively 
# ```
# using Pkg
# Pkg.add(url="url_to_package")
# ``` 
# 
# Once the package is installed
# ```
# using example
# example.fun()
# ```
# should produce "This is the example package!".
# 
# ## Adding dependencies
# Let's add the following function in our example.jl main file:
# ```
# import Dates
# funtime() = println(Dates.now())
# ```
# The function "now()" will print the date and is part of the package "Dates". To add Dates as a dependency to the example package, enter the Pkh REPL and type
# ```
# activate path_to_package
# add Dates
# ```
# Commit all changes and reinstall the package with Pkg (we may need to restart Julia first). Then
# ```
# using example
# example.funtime()
# ```
# should produce the current date and time.
# 
# 
# 
# 
# 
# 
