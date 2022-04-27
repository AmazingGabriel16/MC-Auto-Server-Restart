import subprocess

# This function runs the actual server
# This smol script was made by Gabrel Tobing in 2022
# I hope this helps you :)

# Lost your batch script?
# Here's a copy!

# @echo off
# java -Xmx12000M -Xms12000M -jar paper.jar nogui
# goto :eof

def runServer ():
    subprocess.call('.\start.bat')

def msg (msg_in):
   print('[Python Server Handler]: ' + msg_in)

# Change to True or False if you would like the server to auto-restart when closed
auto_restart = True
msg('Auto-restart: ' + str(auto_restart))

msg('Starting server!')
while auto_restart == True:
    msg('Server auto-restarting!')
    runServer()

if input('[Python Server Handler]: Start server? [Y/N]: ').upper() == 'Y'.upper():
    runServer()