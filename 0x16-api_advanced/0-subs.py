#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Pass an argument to be searched by subreddit.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
