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
![Screen Shot 2021-08-02 at 11 30 04 AM](https://user-images.githubusercontent.com/83669741/127907367-6243185d-639f-4436-9d3a-6a0686e59c31.png)

The column with the most null values is Beer ABV, affecting 67,785 reviews and 14,110 beers. Until I can determine the significance of this feature, I will remove all nulls. Once I have a working model I will determine the best way to reintroduce the beers that were removed. 
