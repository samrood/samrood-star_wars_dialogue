## Star Wars Text Generation
For project 4 I used NPL and Keras to generate new text for Star Wars movies 

## Contents: 
This directory has 3 notebooks and a flask app

## Notebook 1: getting_data
This notebook will: 
- get text data from 6 movie scripts 
- store data in mongodb
- organize the data by character and by movie

## Notebook 2: clustering
This notebook will:
- call the data from mongodb
- cluster the character dialogue by topic modeling
- save the text data for each character for each topic and save as a csv

## Notebook 3: text_generation 
This notebook will:
- read in the csv of the characters topic texts
- generate new lines of text for each topic for each character
- save new text lines created for flask app

## Flask app: star-wars-app
using the saved new lines of text created, the flask app will randomly choose and out put a line from character selected.

## Blog
My Medium blog for this project can be found [here](https://medium.com/@samantharood2/star-wars-text-generation-24093d752439)
