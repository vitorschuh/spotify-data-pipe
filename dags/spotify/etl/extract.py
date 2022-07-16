from os.path import join

import pandas as pd
import spotipy
from spotify.etl.utils import playlists, templates
from spotipy.oauth2 import SpotifyClientCredentials


def extract(client_id: str, client_secret: str, path: str) -> None:

    client_credendials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )

    sp = spotipy.Spotify(client_credentials_manager=client_credendials_manager)

    raw_tracks = []

    for playlist in playlists.links.values():
        playlist_uri = playlist.split("/")[-1].split("?")[0]

        for track in sp.playlist_tracks(playlist_uri)["items"]:
            raw_tracks.append(track)

    clean_tracks = pd.json_normalize(raw_tracks, sep="_")
    clean_tracks.to_csv(
        path_or_buf=join(path, templates.generate()),
        sep=";",
        index=False,
        header=True,
    )
