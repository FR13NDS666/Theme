import os, sys, time, datetime
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)
tik()
