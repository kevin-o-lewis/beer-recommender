def load_data():
    '''
    Parameters:
    -------------
    None

    Returns:
    -------------
    beers_key,prediction_table,test,train

    '''
    import pandas as pd

    beers_key = pd.read_csv('https://raw.githubusercontent.com/kevin-o-lewis/beer-recommender/main/data/beers_key.csv', index_col=0)
    prediction_table = pd.read_csv('https://raw.githubusercontent.com/kevin-o-lewis/beer-recommender/main/data/beer_ids_for_prediction.csv', index_col=0)
    test = pd.read_csv('https://raw.githubusercontent.com/kevin-o-lewis/beer-recommender/main/data/test.csv', index_col=0)
    train = pd.read_csv('https://raw.githubusercontent.com/kevin-o-lewis/beer-recommender/main/data/train.csv', index_col=0)

    return beers_key,prediction_table,test,train


def fit_to_trainset(algo):
    '''
    Parameters:
    -------------
    algo: algorithm to fit 

    Returns:
    -------------
    fit model
    
    '''    

    from surprise import Reader
    
    reader = Reader(rating_scale=(1, 10))
    suprise_train = Dataset.load_from_df(train, reader)
    full_trainset = suprise_train.build_full_trainset()
    algo = algo.fit(full_trainset)
    print('Fit complete.')
    return algo


def recommend(algo, user):
    '''
    Parameters:
    -------------
    algo: prefit model
    user: str, username to make recommendations for

    Returns:
    -------------
    Top 5 recommended beers for that user
    
    ''' 

    if train['review_profilename'].value_counts()[user] < 10:
        print('This user has too few reviews to make a personalized recommendation. Try our most popular beers instead!')
        return pd.DataFrame(data={'Brewery': ['Brouwerij Westvleteren','The Alchemist','Kern River Brewing Company','Brouwerij Drie Fonteinen','Russian River Brewing Company'],
                   'Beer': ['Trappist Westvleteren 12','Heady Topper','Citra DIPA','Armand 4 Oude Geuze Lente','Pliny The Elder']})

    prediction_table['user'] = user
    
    for idx in prediction_table.index:
        prediction_table.loc[idx, ('predicted_rating')] = algo.predict(user, prediction_table['beer_id'][idx])[3]
    top_5 = prediction_table.sort_values(by='predicted_rating', ascending=False)[0:5]['beer_id']
    results = pd.DataFrame()
    for beer_id in top_5:
        results = results.append(beers_key[beers_key['beer_beerid']==beer_id])


    return results


def score(algo, testset):
    '''
    Parameters:
    -------------
    alog: pre-trained model
    testset: Pandas DataFrame of known ratings, columns must be userid, itemid, rating

    Returns:
    -------------
    Mean rating of the top recommendation for each user in the testset

    '''
    top_scores = []
    for user in testset['review_profilename'].unique():
        prediction_table['user'] = user
        for idx in prediction_table.index:
            prediction_table.loc[idx, ('predicted_rating')] = algo.predict(user, prediction_table['beer_id'][idx])[3]

        ranked_recommendations = prediction_table.sort_values(by='predicted_rating', ascending=False)
        user_test_scores = test[test['review_profilename']==user]
        num_scores = 1
        for beer_id in ranked_recommendations['beer_id'].values:
            if beer_id in list(user_test_scores['beer_beerid']):
                num_scores -= 1
                top_scores.append(int(user_test_scores.review_overall[user_test_scores['beer_beerid']==beer_id].values[0]))
                if num_scores == 0:
                    break
            else: continue

    return print('Average rating of top recommendations:', sum(top_scores)/len(top_scores))