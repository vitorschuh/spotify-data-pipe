from datetime import date


def generate(processed: bool = False) -> str:
    if not processed:
        return f"spotify_dump_{date.today()}.csv"

    return f"spotify_dump_{date.today()}_transformed.csv"
