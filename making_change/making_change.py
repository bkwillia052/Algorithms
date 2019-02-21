#!/usr/bin/python

import sys

def making_change(amount, denominations):
    cache = {x: 0 for x in range(amount + 1)} #+1 so that the values can be referenced based on their exact value; otherwise when referencing 370 you would have to use cache[369]
    cache[0] = 1 #set to 1 because not giving change counts as one way. LOL.
    print(cache)
    for coin in denominations:
    #for every coin, go through and tally how many ways 
    #it can make change for the amount of change
    
        for higher_amount in range(coin, amount + 1): 
        #A coin can only make change for an amount higher than it,
        #so start from the coin's value.
        #The goal is to count the total number of coin combinations
        #for EACH amount of change between 0 and the total amount.
        #This will allow you to simply add all of the different combinations
        #together in order to get the final number of combos for the total
        #amount
            diff = higher_amount - coin
            #subtracting the coin's value from the value of the 
            #of the current amount of change will allow you to reference
            #back to the last number you discovered with all of the combinations
            #for with the coin and just add that number of combinations to the
            # current number. 
            cache[higher_amount] += cache[diff]

    print(cache)
    return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")


    """ 
    NOTES:
    -Set a var for num of ways
    -You'll have to see how many times each denomination can go into the
    amount with % 0. 
    ^^these will each increment the 'ways' var by 1
    -Next you'll need to find the different combinations of coins that count as a way
    --For this, you will need to find ways to track how many pairs of matches there are.
    --You'll also need to find a ways to break down remainders into change pairs too. 
     """