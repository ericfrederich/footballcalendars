#!/usr/bin/env python

import requests
import os
import re
from bs4 import BeautifulSoup

for team in [
# AFC
    # East
        'Bills'     ,
        'Dolphins'  ,
        'Patriots'  ,
        'Jets'      ,
    # North
        'Ravens'    ,
        'Bengals'   ,
        'Browns'    ,
        'Steelers'  ,
    # South
        'Texans'    ,
        'Colts'     ,
        'Jaguars'   ,
        'Titans'    ,
    # West
        'Broncos'   ,
        'Chiefs'    ,
        'Raiders'   ,
        'Chargers'  ,
# NFC
    # East
        'Cowbows'   ,
        'Giants'    ,
        'Eagles'    ,
        'Redskins'  ,
    # North
        'Bears'     ,
        'Lions'     ,
        'Packers'   ,
        'Vikings'   ,
    # South
        'Falcons'   ,
        'Panthers'  ,
        'Saints'    ,
        'Buccaneers',
    # West
        'Cardinals' ,
        'Rams'      ,
        '49ers'     ,
        'Seahawks'  ,
]:
    if not os.path.isdir('html'):
        os.mkdir('html')

    fname = os.path.join('html', team)
    if not os.path.isfile(fname):
        print "don't have file %s... requesting" % team
        r = requests.get('http://www.nfl.com/schedules/2014/REG/' + team)
        with open(fname, 'w') as fout:
            fout.write(r.text)

    soup = BeautifulSoup(open(fname))
    print '---', team, '---'
    games = soup.find_all('div', class_='schedules-list-hd pre')
    for game in games:
        date       = game.find(class_='date').text
        week       = int(game.find(class_='week').text)
        time       = game.find(class_='time').text
        opponent   = game.find(class_=re.compile(r'^team-name.*')).text
        networks   = ' / '.join([s['title'] for s in game.find(class_='list-matchup-row-tv').find_all('span')])
        at_vs      = 'vs' if 'away' in game.find_all(class_=re.compile(r'^team-name.*'))[0]['class'] else 'at'
        print '%2d' % week, date, time, '%-20s' % networks, '%-4s' % at_vs, opponent


try:
    import readline
except ImportError:
    print "Module readline not available."
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")