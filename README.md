# Welcome to the PublicHolidayFinder program!
## By Pontus Nordqvist <p.nordq@gmail.com>
This is for the IBM; Case Study - Data Engineering
All tasks have been completed!
I've made a notebook for all assignment steps, which can be found in the root
directory. Additionally, if you prefer scripts, I've kept them as script in the
script-folder.

## Requirements
- Python 3.9
- pip
- pandas==1.2.4
- holidays==0.11.1
- datefinder==0.7.1
- beautifulsoup4==4.9.3
- jupyternotebook (to open the notebooks)

## Installation
Install the requirements, excluding Python, as:
  >>pip install -r requirements.txt

## Docker
Why do the above when you can just use Docker?
Build the container by
  docker build -t python-phf .

And run the interactive container using
  >>docker run -t -i python-phf

## Using the Public Holiday Finder (app.py)
Start the program in docker or locally i.e
  >>python app.py

Follow the given instruction! There is lots of error handling, so no need to
worry from the user's side.

## The date
can be given as e.g 1 Jan 2021, 1/1 2018, January 1 2020. It can find the date
no matter what, unless multiple dates are given or if it's outside of the
datasets range.

## The country
can be given three/two digit ISO code or as just the name e.g Sweden. Not: not
case sensetive!

## Anything unclear?
Feel free to contact me!
