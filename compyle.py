import sys
import os

config = open('pages.config', 'r').readlines()
config = [i.strip() for i in config]

print(config)

print(sys.argv)