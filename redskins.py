#!/usr/bin/env python

GAME_DATA = [

['Preseason game 1', 2013,  8,  8, 8, 00, 'Redskins @ Titans'    , ''           ],
['Preseason game 2', 2013,  8, 19, 8, 00, 'Redskins vs Steelers' , 'ESPN'       ],
['Preseason game 3', 2013,  8, 24, 4, 30, 'Redskins vs Bills'    , ''           ],
['Preseason game 4', 2013,  9, 29, 7, 30, 'Redskins @ Buccaneers', ''           ],
['Game 1'          , 2013,  9,  9, 7, 10, 'Redskins vs Eagles'   , 'ESPN'       ],
['Game 2'          , 2013,  9, 15, 1, 00, 'Redskins @ Packers'   , 'Fox'        ],
['Game 3'          , 2013,  9, 22, 1, 00, 'Redskins vs Lions'    , 'Fox'        ],
['Game 4'          , 2013,  9, 29, 4, 25, 'Redskins @ Raiders'   , 'Fox'        ],
# BYE WEEK
['Game 6'          , 2013, 10, 13, 8, 30, 'Redskins @ Cowboys'   , 'NBC'        ],
['Game 7'          , 2013, 10, 20, 1, 00, 'Redskins vs Bears'    , 'Fox'        ],
['Game 8'          , 2013, 10, 27, 4, 25, 'Redskins @ Broncos'   , 'Fox'        ],
['Game 9'          , 2013, 11,  3, 1, 00, 'Redskins vs Chargers' , 'CBS'        ],
['Game 10'         , 2013, 11,  7, 8, 25, 'Redskins @ Vikings'   , 'NFL Network'],
['Game 11'         , 2013, 11, 17, 1, 00, 'Redskins @ Eagles'    , 'Fox'        ],
['Game 12'         , 2013, 11, 25, 8, 40, 'Redskins vs 49ers'    , 'ESPN'       ],
['Game 13'         , 2013, 12,  1, 8, 30, 'Redskins vs Giants'   , 'NBC'        ],
['Game 14'         , 2013, 12,  8, 1, 00, 'Redskins vs Chiefs'   , 'CBS'        ],
['Game 15'         , 2013, 12, 15, 1, 00, 'Redskins @ Falcons'   , 'Fox'        ],
['Game 16'         , 2013, 12, 22, 1, 00, 'Redskins vs Cowboys'  , 'Fox'        ],
['Game 17'         , 2013, 12, 29, 1, 00, 'Redskins @ Giants'    , 'Fox'        ],

]

print 'BEGIN:VCALENDAR'
print 'VERSION:1.0'

for desc, year, month, day, hour, minute, title, network in GAME_DATA:
    print 'BEGIN:VEVENT'
    print 'DTSTART:%s'     % '%04d%02d%02dT%02d%02d00' % (year, month, day, hour+12, minute)
    print 'DTEND:%s'       % '%04d%02d%02dT%02d%02d00' % (year, month, day, hour+15, minute)
    print 'SUMMARY:%s'     % title
    print 'LOCATION:%s'    % network
    print 'DESCRIPTION:%s' % desc
    print 'PRIORITY:3'
    print 'END:VEVENT'

print 'END:VCALENDAR'
