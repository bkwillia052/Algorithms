#!/usr/bin/python

import sys

def making_change(amount, denominations):

    ways = 0
    way_pairs = {}
    if amount == 0:
      return 0
    for value in denominations:
        way_pairs[value] = []
        if amount % value == 0:
          way_pairs[value] = [value]
          """ print("Single denom:",value) """
          ways += 1

    for i in range(len(denominations)-1, -1, -1):
         
         """ print(denominations[i]) """
         for value in denominations:
             """ print("Values:", denominations[i], value) """
             if denominations[i] == amount:
                pass 
             elif amount - denominations[i] < 0:
                pass
             elif (amount - denominations[i]) % value == 0:
                if not value in way_pairs[denominations[i]]:
                    way_pairs[denominations[i]].append(value)
                    ways += 1
    print(747 % 38)          
    return ways


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