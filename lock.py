#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# check whether script is already executing / bluehost cron job problem

# MODULES

import sys
import os
from time import sleep

# FUNCTIONS

def checkExec():
  if os.path.isfile('./lock.txt'):
    sys.exit('Process already executing.')
  open('./lock.txt', 'a').close()
  sleep(1)
  os.remove('./lock.txt')

# TEST

if __name__ == '__main__':
  checkExec()