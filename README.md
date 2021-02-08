# spotify-wrapped

A simple script for a custom Spotify Wrapped you can get at any time.

## Steps

1. Request data at https://www.spotify.com/us/account/privacy
2. Wait for up to 30 days until they send you your data
3. Download your data and unzip it so that you get something like this in this directory:

```
data/
    StreamingHistory0.json
    StreamingHistory1.json
    StreamingHistory2.json
    StreamingHistory3.json
    ...
.gitignore
main.py
README.md
```

4. Run `python3 main.py` and get some fancy statistics

In the future there will be more statistics, but you can easily add your own.