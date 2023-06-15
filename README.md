<br />
<p align="center">
  <a href="https://github.com/AmmarTaradifa/Capstone-Bangkit-2023-BoBy">
    <img src="https://www.linkpicture.com/q/logo_1.png" width='150dp' alt="Logo" >
  </a>

  <h1 align="center">BoBy (Body Balancy)</h1>
  <h2 align="center">
  Application which helps to manage your weight . Try it now!</h2>
  
  <p align="center">
  This is a project to fulfill the  <a href="https://grow.google/intl/id_id/bangkit/"><strong>Bangkit Academy led by Google, Tokopedia, Gojek, & Traveloka</strong></a>
   Program.
  
  <p align="center">
    © C23-PS183 Bangkit Capstone Team
  </p>
  </p>
</p>

# Team Members

## Team ID : C23-PS183

<br>

| Name                   | Student ID | Path                | University  |
| ---------------------- | ---------- | ------------------- |------------ |
| I Made Juniandika      | M368DSX2112| Machine Learning    |Universitas Udayana|
| Rizky Adha Hardiman    | M172DSX2182| Machine Learning    |Universitas Gunadarma |
| Arsya Alifian Widiatmoko  | A086DSX1091 | Android Development |Sekolah Tinggi Teknologi Bandung |
| Hieronimus Mao Putra Koban | A360DSX3391 | Android Development |Universitas Telkom|
| Ammar Taradifa         | C122DKX4571| Cloud Computing     |UIN Sunan Gunung Djati Bandung |
| Muhammad Reva Ferdiansyah | C309DSX0894| Cloud Computing     |Universitas Pendidikan Indonesia|

<br>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#app-overview">App Overview</a></li>
    <li>
      <a href="#documentation">Documentation</a>
      <ul>
        <li><a href="#machine-learning-development-documentation">Machine Learning Documentation</a></li>
        <li><a href="#mobile-development-documentation">Mobile Documentation</a></li>
        <li><a href="#cloud-computing-documentation">Cloud Computing Documentation</a></li>
      </ul>
    </li>
  </ol>
</details>


## About The Project

BoBy - Body Balancy is an application that is used to tell people if they are get overweight or they body just in ideal condition. 

This application also can recommend people what they need to do so they can get their ideal body

We want to overcome this health problem by providing an application to help people get their ideal body so they can be healthier and be more productive.

# App Overview

- **Prerequisites**

  1.  Android
  2.  Internet connection

- **Installation**

  1.  Download the APK
  2.  Install the APK

- **Usage**

  1. Register your email address
  2. Now you can use the app
 
# Documentation

## Machine Learning  Documentation
### Obesty Prediction

1. Load data from dataset : https://www.kaggle.com/datasets/tathagatbanerjee/obesity-dataset-uci-ml
2. Data Preprocessing
3. Model  : Decision Tree
4. Test accuracy model using test data
### Food Recommendation System

### Food Image Classification

1. Load  image data  from dataset : https://www.kaggle.com/datasets/imbikramsaha/food11
2. Image data Augmentation
3. Building model using deep learning
4. Test model using test data
## Mobile Development Documentation
  


## Cloud Computing Documentation

### Obesty Predict API 

  1.  Open Postman,and put this endpoint : https://obesty-model-fm5o2c5urq-et.a.run.app/predict
  2.  Request on POST and Body Type on x-www-form-urlencoded
  3.  Fill the key and value,for example

<br>
  <img src="https://www.linkpicture.com/q/obesty.png" width='700dp' height='500dp' alt="obesty" >
      
 
### Food Classification API

1.  Open Postman,and put this endpoint : https://obesty-model-fm5o2c5urq-et.a.run.app/predict
2.  Request on POST and Body Type on form-data
3.  Fill the key is 'file' and value from your computer,for example:
4.  We recommend to test this api with image in [here](https://github.com/AmmarTaradifa/Capstone-Bangkit-2023-BoBy/tree/main/food11/train) for correct predict
   
<br>
  <img src="https://www.linkpicture.com/q/gambar.png" width='700dp' height='500dp' alt="gambar" >

### Food Recomendation API

1.  Open Postman,and put this endpoint : https://food-model-fm5o2c5urq-et.a.run.app/predict
2.  Request on POST and Body Type on x-www-form-urlencoded
3.  Fill the key and value,for example

<br>
  <img src="https://www.linkpicture.com/q/recommend.png" width='700dp' height='500dp' alt="recommend" >
