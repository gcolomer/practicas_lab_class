# Practice III Machine Learning

## By Gabriela Gutiérrez-Colomer Santos: g.gutierrezcolomer@cunef.edu

### https://github.com/gcolomer/practicas_lab_class
# <font color='Red'>Understanding how restaurants are rated using reviews and Predicting their status using Natural Language Processing (NLP)</font>
### The objective of the practice is: to understand how natural language processing is used in the feedback left by business customers. To develop a predictor that, using the words in the reviews, knows whether the restaurant will be good or bad. To understand how models are able to give context to words and interpret their connotation. 

### <font color='Red'>Important: The ``requirements.txt`` is located in the environment directory, please, check that you have all the packages and extensions before proceeding with this work.</font>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

#### practica_3 has the following structure: 
<i style="color:lightblue" class="fa fa-folder"></i> data
<i style="color:lightblue" class="fa fa-folder"></i> environment
<i style="color:lightblue" class="fa fa-folder"></i> html
<i style="color:lightblue" class="fa fa-folder"></i> images
<i style="color:lightblue" class="fa fa-folder"></i> models
<i style="color:lightblue" class="fa fa-folder"></i> notebooks





## The following practice is divided  in three different notebooks (notebooks directory): 
1. **Notebook 1: 0_EDA**
In Notebook 1 we will find: 
<ol style="font-size:12px; font-family: Arial">
  <li>Upload the business dataset.</li>
    <span style="color: red">Uploading the dataset to perform cleaning of the business.</span>
  <li>Define the problem.</li>
    <span style="color: red">We will focus only on business that are type restaurants or offer a similar service, pharmacies, groccery stores and supermarkets will be ignored.</span>
  <li>Studying the most reviewed USA state.</li>
    <span style="color: red">The state of Pennsylvania is the state with more reviews so we will be using it for the whole practice.</span>
  <li>Reviewing the restaurants.</li>
    <span style="color: red">We will study the best restaurants in Pennsylvania by looking at a very helpful feature called ``senti_polarity``.</span>
  <li>Reviewing the restaurants by type of food.</li>
    <span style="color: red">We will review the words used for the best restaurants in Pennsylvania but filtering by type of food.</span>
  <li>Restaurant Recomendation System.with map</li>
    <span style="color: red">Develop a restaurant filter to be able to access the restaurants in an easier way. The filter is able to represent the city in Pennsylvania and the restaurants related to the type of food desired. </span>
</ol>

2. **Notebook 2: 1_EDA_MODEL**
In Notebook 2 we will find: 
<ol style="font-size:12px; font-family: Arial">
  <li>Cleaning the Data.</li>
    <span style="color: red">In this section null values will be treated.</span>
  <li>Understanding the variables.</li>
    <span style="color: red">In this section the variables will be studied in case there is any important relationship we must take into account.</span>
  <li>Model Design.</li>
    <span style="color: red">The model chosen is a LinearSVM. We will be classifying business as top_experience or not_experience depending on the reviews.</span>
  <li>Model Results.</li>
    <span style="color: red">This is the part where results are discussed.</span>
</ol>

3. **Notebook 3: 2_INTERPRET**
In Notebook 3 we will find: 
We will deal with everything related to interpretability, for a better understanding we will divide the notebook in 3 parts:
<ol style="font-size:12px; font-family: Arial">
  <li>Mathematical interpretability of the model:</li>
    <span style="color: red">How is LinearSVC able to predict following a mathematical perspective? </span>
  <li>Interpretability of the predictions:</li>
    <span style="color: red"> Why does the model decide that this opinion is bad or good? How should a review be done to generate impact? Does the model give certain weight to words? Are some words more important?</span>
  <li>Graphs and other possible clustering options to better understand the opinions.</li>
  <span style="color: red"> Graphs using networkx are a very convenient way of arranging the data. </span>
</ol>