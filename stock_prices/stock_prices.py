#!/usr/bin/python

import argparse

def find_max_profit(prices):

    price_profits = []
    buy_index = 0
    sell_index = buy_index + 1

    while buy_index < (len(prices) -1):

      if sell_index < len(prices):
        price_profits.append(prices[sell_index] - prices[buy_index])
        sell_index +=1

      else:
        buy_index +=1
        sell_index = buy_index + 1

    return max(price_profits)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
