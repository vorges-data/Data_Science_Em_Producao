# Rossmann Sales Predict
#### This project has academic purposes.


![](graph-gc6fdabf68_1280.jpg)

# 1. Business Problem.

Rossmann it's a big European drugstore. Some store managers call me for help in predicting sales for the next six weeks.
The root cause is a demand from the CFO, discussed at the weekly meeting: he needs to plan store renovations, and for that, the budget needs to be in line with each store's sales.
Therefore, the principal stakeholder is the CFO, but from which all store managers will benefit.


# 2. Business Assunptions.

All data got taken from the company's internal sales base, with a horizon of 18 months. Any data before this would be seriously affected by external events (biased).
Several details were found, such as type of store, variety of products offered and competition proximity. Other variable info such as customers per day and sales per day, holidays, marketing promotions was available too.

However, it was necessary to assume some things. See bellow.

- **Conmpetition proximity**: Was expressed in meters but, sometimes it was zero. So, 'Zero Competition Distance' it's same as 'No Competition Proximity'. But, for ML Algorithms this input is a bias. In this case, I assumed a fixed value (100,000 m) higher than the highest value in the dataset.
- **Assortment**: I assumed there is a hierarchy between types. So, stores with Assortment Type C must first offer Types A and B. 
- **Store Open**: I removed all the lines that indicate Store Closed, as we also had Zero sales on the same day. For ML purposes, this will be reviewed in the next CRISP cycle. 
- **Sales Prediction**: In agreement with the CFO, I assumed they would provide the total sales at the end of the sixth week.



My strategy to solve this challenge was based in CRISP-DM Cycle:

**00. Understand the Problem:** _The most important step for correct plan entire solution_.

**01. Data Description:** My goal is to use statistics metrics to identify data outside the scope of business.

**02. Data Filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.

**03. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.

**04. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

**05. Data Preparation:** Prepare the data so that the Machine Learning models can learn the specific behavior.

**06. Feature Selection:** Selection of the most significant attributes for training the model.

**07. Machine Learning Modelling:** Machine Learning model training

**08. Hyperparameter Fine Tunning:** Choose the best values for each of the parameters of the model selected from the previous step.

**09. Convert Model Performance to Business Values:** Convert the performance of the Machine Learning model into a business result.

**10. Deploy Model to Production:** Publish the model to a cloud environment so that other people or services can use the results to improve the business decision. _In this particular case, the model is accessible from a Telegram Bot_.







|       Model Name          |        MAE CV       |     MAPE CV    |      RMSE CV       |
|:-------------------------:|:-------------------:|:--------------:|:------------------:|
| Linear Regression         |  2082.46 +/- 295.78 | 30.26 +/- 1.66 | 2950.11 +/- 468.88 |
| Lasso Regression          |  2116.65 +/- 341.58 | 29.2  +/- 1.18 | 3056.56 +/- 504.44 |
| Random Forest Regressor   |  837.7   +/- 219.23 | 11.61 +/- 2.32 | 1256.59 +/- 320.26 |
| XGBoost Regressor         |  2889.54 +/- 343.25 | 34.54 +/- 1.39 | 3714.69 +/- 456.1  |








     Model Name               MAE           MAPE%          RMSE
|:--------------------:|:------------:|:-----------:|:--------------:|
|  XGBoost Regressor   |   764.9756   |   11.4861   |   1,100.7251   |







 	  store 	predictions 	worst_scenario 	best_scenario 	MAE     	MAPE
291 	292 	108,359.7891 	104,977.6086 	111,741.9695 	3,382.1804 	60.2768
908 	909 	220,300.0781 	212,395.1411 	228,205.0152 	7,904.9371 	51.8675
875 	876 	194,060.8125 	189,924.5347 	198,197.0903 	4,136.2778 	33.7730
169 	170 	201,541.6875 	200,194.4216 	202,888.9534 	1,347.2659 	33.2923
748 	749 	206,800.9531 	205,789.1920 	207,812.7142 	1,011.7611 	28.3049


 	Scenario 	      Values
0 	predictions 	$ 286,435,616.00
1 	worst_scenario 	$ 285,579,535.55
2 	best_scenario 	$ 287,291,675.73



