import os
import json
import datetime


def format_time(ms):
    delta = datetime.timedelta(milliseconds=ms)
    delta = delta - datetime.timedelta(microseconds=delta.microseconds)
    return str(delta)


tracks = {}
tracksByPlayTime = {}
tracksByPlays = {}
artistsByPlayTime = {}
artistsByPlays = {}

for filename in os.listdir('data'):
    if filename.startswith('StreamingHistory'):
        with open('data/%s' % filename) as json_file:
            listens = json.load(json_file)
            for listen in listens:
                trackKey = listen['artistName'] + ',' + listen['trackName']
                artistKey = listen['artistName']

                if trackKey not in tracks:
                    tracks[trackKey] = {'artistName': listen['artistName'], 'trackName': listen['trackName']}

                if trackKey not in tracksByPlayTime:
                    tracksByPlayTime[trackKey] = 0
                if trackKey not in tracksByPlays:
                    tracksByPlays[trackKey] = 0

                if artistKey not in artistsByPlayTime:
                    artistsByPlayTime[artistKey] = 0
                if artistKey not in artistsByPlays:
                    artistsByPlays[artistKey] = 0

                tracksByPlayTime[trackKey] += listen['msPlayed']
                tracksByPlays[trackKey] += 1

                artistsByPlayTime[artistKey] += listen['msPlayed']
                artistsByPlays[artistKey] += 1

tracksByPlayTime = dict(sorted(tracksByPlayTime.items(), key=lambda item: item[1], reverse=True))
tracksByPlays = dict(sorted(tracksByPlays.items(), key=lambda item: item[1], reverse=True))

artistsByPlayTime = dict(sorted(artistsByPlayTime.items(), key=lambda item: item[1], reverse=True))
artistsByPlays = dict(sorted(artistsByPlays.items(), key=lambda item: item[1], reverse=True))

print('Tracks by play time:')
for i, trackKey in enumerate(list(tracksByPlayTime)[0:10]):
    trackName = tracks[trackKey]['trackName']
    artistName = tracks[trackKey]['artistName']
    playTime = format_time(tracksByPlayTime[trackKey])
    print('{index}. [{trackName}] by [{artistName}]: {playTime}'.format(index=i + 1,
                                                                        trackName=trackName,
                                                                        artistName=artistName,
                                                                        playTime=playTime))

print('')

print('Tracks by plays:')
for i, trackKey in enumerate(list(tracksByPlays)[0:10]):
    trackName = tracks[trackKey]['trackName']
    artistName = tracks[trackKey]['artistName']
    plays = tracksByPlays[trackKey]
    print('{index}. [{trackName}] by [{artistName}]: {plays}'.format(index=i + 1,
                                                                     trackName=trackName,
                                                                     artistName=artistName,
                                                                     plays=plays))
print('')

print('Artists by play time:')
for i, artistKey in enumerate(list(artistsByPlayTime)[0:10]):
    playTime = format_time(artistsByPlayTime[artistKey])
    print('{index}. [{artistName}]: {playTime}'.format(index=i + 1,
                                                       artistName=artistKey,
                                                       playTime=playTime))

print('')

print('Artists by plays:')
for i, artistKey in enumerate(list(artistsByPlays)[0:10]):
    print('{index}. [{artistName}]: {plays}'.format(index=i + 1,
                                                    artistName=artistKey,
                                                    plays=artistsByPlays[artistKey]))

print('')
