# Rossmann Sales Predict
#### This project has academic purposes.


![](graph-gc6fdabf68_1280.jpg)

# 1. Business Problem.

Rossmann it's a big European drugstore. Some store managers call me for help in predicting sales for the next six weeks.
The root cause is a demand from the CFO, discussed at the weekly meeting: he needs to plan store renovations, and for that, the budget needs to be in line with each store's sales.
Therefore, the principal stakeholder is the CFO, but from which all store managers will benefit.


# 2. Business Assunptions.

All data got taken from the company's internal sales base, with a horizon of 18 months. Any data before this would be seriously affected by external events (biased).
Several details were found, such as type of store, variety of products offered in the store. Other info such as customers per day, sales per day and competition proximity was available too.

However, it was necessary to assume some things. See bellow.

- **This**:
- **That**:
- **Another This**:
- **Another That**:



My strategy to solve this challenge was:

**Step 01. Data Description:** My goal is to use statistics metrics to identify data outside the scope of business.

**Step 02. Data Filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.

**Step 03. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.

**Step 04. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

**Step 05. Data Preparation:** Prepare the data so that the Machine Learning models can learn the specific behavior.

**Step 06. Feature Selection:** Selection of the most significant attributes for training the model.

**Step 07. Machine Learning Modelling:** Machine Learning model training

**Step 08. Hyperparameter Fine Tunning:** Choose the best values for each of the parameters of the model selected from the previous step.

**Step 09. Convert Model Performance to Business Values:** Convert the performance of the Machine Learning model into a business result.

**Step 10. Deploy Model to Production:** Publish the model to a cloud environment so that other people or services can use the results to improve the business decision. In this particular case, the model is accessible from a Telegram Bot.



