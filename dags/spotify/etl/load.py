import time
from os.path import join

import pandas as pd
import psycopg2
from spotify.etl.utils import templates
from sqlalchemy import create_engine


def load(
    path: str, uri: str, db: str, user: str, password: str, verbose: bool = False
) -> None:
    start = time.time()
    data = pd.read_csv(
        filepath_or_buffer=join(path, templates.generate(processed=True)),
        sep=";",
    )
    url = f"postgresql+psycopg2://{user}:{password}@{uri}/{db}"
    engine = create_engine(url=url)
    with engine.connect() as conn:
        data.to_sql(name="spotify-tracks", con=conn, if_exists="replace", index=False)

    if verbose:
        elapsed = time.time() - start
        print(f"Load complete. Time elapsed ≈ {elapsed}.")
