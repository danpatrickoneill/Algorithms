#!/usr/bin/python
import argparse
import math


def find_max_profit(prices):
    buying_price = prices[0]
    profit = prices[1] - prices[0]
    for price in prices[1:]:
        # if a lower price is found, assign it to buying_price
        # could also move this below profit check, which eliminates need for continue
        if price < buying_price:
            if (price - buying_price) > profit:
                profit = price - buying_price
            buying_price = price
            # if price has been updated this round, don't need to check profit
            continue
        # if selling at current price results in greater profit, update profit
        if (price - buying_price) > profit:
            profit = price - buying_price
    return profit


if __name__ == '__main__':
    print(find_max_profit([10, 7, 5, 8, 11, 9]))
    print(find_max_profit([100, 90, 80, 50, 20, 15]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
