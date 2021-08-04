
# Beer Recommender

## EDA
**Dataset consists of:**

- 1,586,614 reviews
- 13 features
- 66,055 unique beers (from 5,840 breweries)
- 33,387 unique users


**Features:**
1. Brewery ID
2. Brewery Name
3. Review Timestamp
4. Overall Score
5. Aroma Score
6. Appearance Score
7. Reviewer Username
8. Beer Style
9. Palate Score
10. Taste Score
11. Beer Name
12. Beer ABV
13. Beer ID


**Distribution Information:**\
Reviews per user: 
- Average: 47.4
- Max: 5817
- Min: 1

Reviews per beer:
- Average: 24.0
- Max: 3290
- Min: 1


## Data Cleaning
![Screen Shot 2021-08-02 at 11 50 29 AM](https://user-images.githubusercontent.com/83669741/127909450-9a2e6eb5-a2d3-49d0-a054-c5bda71a780d.png)

The column with the most null values is Beer ABV, affecting 67,785 reviews and 14,110 beers. Until I can determine the significance of this feature, I will remove all nulls. Once I have a working model I will determine the best way to reintroduce the beers that were removed.

I separated the dataset into a training and holdout set with 25% of the reviews reserved for holdout testing.

## Initial Models
I used the Surprise library to produce some quick initial collaborative models, with results below. All models were performed on the same train-test-split of the training set.
|Model|RMSE|
|-----|----|
|Normal Predictor|1.9884|
|KNN with means|1.2622|
|SVD|1.2476|
|SlopeOne|1.2345|
