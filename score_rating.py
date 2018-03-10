def convert_to_numeric(score):
    """Function that converts all types of scores into floating point numbers.
    This was my choise because later we will have to calculate an average,
    and it will be a floating point number.
    """
    return float(score)

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """Function that takes 5 scores, deletes the outliers and sums the
    three central values.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1+score2+score3+score4+score5-max_score-min_score
    return sum
    
def score_to_rating_string(average_score):
    """This function returns the rating depending on the average score given.
    """
    if 0 <= average_score < 1:
        rating = "Terrible"
    elif 1 <= average_score < 2:
        rating = "Bad"
    elif 2<= average_score < 3:
        rating = "OK"
    elif 3<= average_score <4:
        rating = "Good"
    elif 4<= average_score <=5:
        rating = "Excellent"
    else:
        rating = "An Error happened."
    return rating
        
def scores_to_rating(score1,score2,score3,score4,score5):
    """ This is a function that evaluates the scores given to some product
    and discard the outliers (higest and lowest values), and then returns
    the mean.
    
    """
    
    #1.- Read the input, transform it into a number
    ###Input: score as a string/float/int
    ###Output: score as a float or int
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score4 = convert_to_numeric(score5)   

    #2.- Discard outliers from the sample
    ###Input: 5 scores as a float or int
    ###Output: 3 scores (same numerical type)
    #We are finally doing this in one unique line in the step 3

    #3.- Calculate the mean
    ###Input: 3 scores as a float or int
    ###Output: 1 average score (float)
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5) / 3

    #4.- Choose the correct word dating for the average score
    ###Input: average score as a float
    ###Output: rating as a string
    rating = score_to_rating_string(average_score)

    return rating


