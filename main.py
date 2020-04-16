#/usr/bin/env/python3
import os, sys, time
from bot import client

if not __name__=="__main__":
    exit()

os.chdir(sys.path[0]) # change working dir as script dir to get fixed relative access to data
if not os.path.exists("data"): os.makedirs("data")

TOKEN = 'NjkyNzM2NzgxNTUyMTg5NTgx.XphjSg.1VxHBhvNhkqKZ8WdHEa1LtUU-28' #$os.environ["nalgang_TOKEN"]
client.run(TOKEN)
