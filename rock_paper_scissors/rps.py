#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  plays = ["rock", "paper", "scissors"]

  all_possible_plays = []

  if n < 1:
    return [all_possible_plays]

  if n == 1:
    for i in plays:
      all_possible_plays.append([i])
    return all_possible_plays
  

  if n == 2:
    for i in plays:
      for j in plays:
        all_possible_plays.append([i, j])
    return all_possible_plays

  if n == 3:
    for i in plays:
      for j in plays:
        for k in plays:
          all_possible_plays.append([i, j, k])
    return all_possible_plays

  if n == 4:
    for i in plays:
      for j in plays:
        for k in plays:
          for l in plays:
            all_possible_plays.append([i, j, k, l])
    return all_possible_plays

  if n == 5:
    for i in plays:
      for j in plays:
        for k in plays:
          for l in plays:
            for m in plays:
              all_possible_plays.append([i, j, k, l, m])
    return all_possible_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
