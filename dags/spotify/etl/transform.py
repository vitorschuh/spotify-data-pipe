from os import path

import pandas as pd
from spotify.etl.utils import templates


def transform(raw_path: str, processed_path: str) -> None:
    df = pd.read_csv(
        filepath_or_buffer=path.join(raw_path, templates.generate()), sep=";"
    )
    df = df[
        [
            "track_uri",
            "track_name",
            "track_artists",
            "track_album_name",
            "track_popularity",
        ]
    ]
    df.columns = [
        "uri",
        "name",
        "artists",
        "album_name",
        "popularity"
    ]
    df.to_csv(
        path_or_buf=path.join(processed_path, templates.generate(processed=True)),
        sep=";",
        index=False,
        header=True,
    )
