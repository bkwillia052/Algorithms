#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):

    cache = {i: 0 for i in range(n+1)}
    cache[0] = 1
    jumps = [1,2,3]

    for jump in jumps:

        for step in range(jump, len(cache)):
            diff = step - jump
            if step >= 3: 
                cache[step] = cache[step-1] + cache[step-2] + cache[step-3]
            else:
                cache[step] += cache[diff]
    print(cache)
    return cache[n]
        


   


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')