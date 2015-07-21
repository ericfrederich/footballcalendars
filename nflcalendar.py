#!/usr/bin/env python

import sys
import requests
import os
import re
from bs4 import BeautifulSoup
import datetime

YEAR = datetime.datetime.now().year

TEAMS =  [
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
        'Cowboys'   ,
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
]

def make_calendar(team, data):
    with open(os.path.join('calendars', str(YEAR), team + '.ics'), 'w') as fout:

        print >> fout, 'BEGIN:VCALENDAR'
        print >> fout, 'VERSION:1.0'

        #for desc, year, month, day, hour, minute, title, network in data:
        for week, month, day, hour, minute, networks, at_vs, opponent in data:

            month = {'Sep':9,'Oct':10,'Nov':11,'Dec':12,'Jan':1}[month]
            day     = int(day)
            hour    = int(hour)
            minute  = int(minute)
            year = YEAR
            if month < 9:
                year += 1

            print >> fout, 'BEGIN:VEVENT'
            print >> fout, 'DTSTART:%s'          % '%04d%02d%02dT%02d%02d00' % (YEAR, month, day, hour+12, minute)
            print >> fout, 'DTEND:%s'            % '%04d%02d%02dT%02d%02d00' % (YEAR, month, day, hour+15, minute)
            print >> fout, 'SUMMARY:%s %s %s'    % (team, at_vs, opponent)
            print >> fout, 'LOCATION:%s'         % networks
            print >> fout, 'DESCRIPTION:Game %s' % week
            print >> fout, 'PRIORITY:3'
            print >> fout, 'END:VEVENT'

        print >> fout, 'END:VCALENDAR'


if __name__ == '__main__':
    if not os.path.isdir('html'     ): os.mkdir('html'     )
    if not os.path.isdir(os.path.join('calendars', str(YEAR))): os.mkdir(os.path.join('calendars', str(YEAR)))

    teams = sys.argv[1:]
    if not teams:
        teams = TEAMS

    for team in teams:

        fname = os.path.join('html', team)
        if not os.path.isfile(fname):
            print "don't have file %s... requesting" % team
            r = requests.get('http://www.nfl.com/schedules/' + str(YEAR) + '/REG/' + team)
            with open(fname, 'w') as fout:
                fout.write(r.text)

        soup = BeautifulSoup(open(fname), 'lxml')
        print '---', team, '---'
        games = soup.find_all('div', class_='schedules-list-hd pre')
        data = []
        for game in games:
            month, day   = game.find(class_='date').text.split()
            week         = int(game.find(class_='week').text)
            hour, minute = game.find(class_='time').text.split(':')
            opponent     = game.find(class_=re.compile(r'^team-name.*')).text
            networks     = ' / '.join([s['title'] for s in game.find(class_='list-matchup-row-tv').find_all('span')])
            at_vs        = 'vs' if 'away' in game.find_all(class_=re.compile(r'^team-name.*'))[0]['class'] else 'at'

            print '%2d' % week, month, day, '%2s:%2s' % (hour, minute), '%-20s' % networks, '%-4s' % at_vs, opponent
            data.append((week, month, day, hour, minute, networks, at_vs, opponent))

        make_calendar(team, data)
