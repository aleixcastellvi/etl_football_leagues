import pandas as pd
import time
import random


def get_urls():

    # A dataframe with links of statistics per league is obtained
    return pd.read_csv('leagues/leagues.csv')


def get_data(league: str, url: str) -> pd.DataFrame:

    # Three different waits in seconds
    Standby_time = [2, 1, 3]
    # A wait is generated so as not to overload the web
    time.sleep(random.choice(Standby_time))

    # Web scraping
    df = pd.read_html(url)
    # The web scraping df is generated in two parts.
    df = pd.concat([df[0], df[1]], axis=1)

    # Define the names of the columns
    df.columns = ['Equipo', 'J', 'G', 'E', 'P', 'GF', 'GC', 'DIF', 'PTS']
    # New column with the league parameter is added
    df['Liga'] = league
    # Team name cleanup: 1BARBarcelona -> Barcelona ; 11GIRGerona -> Gerona
    df['Equipo'] = df['Equipo'].apply(lambda x: x[5:] if x[:2].isnumeric() == True else x[4:])

    # Reorder columns
    df = df[['Liga', 'Equipo', 'J', 'G', 'E', 'P', 'GF', 'GC', 'DIF', 'PTS']]

    return df


def data_processing(df: pd.DataFrame, league_input: str) -> pd.DataFrame:

    # Get a df per league

    spainDF = get_data(df['LIGA'][0], df['URL'][0])
    englandDF = get_data(df['LIGA'][1], df['URL'][1])
    franceDF = get_data(df['LIGA'][2], df['URL'][2])
    italyDF = get_data(df['LIGA'][3], df['URL'][3])
    germanyDF = get_data(df['LIGA'][4], df['URL'][4])

    # A single pdf is obatined

    df = pd.concat([spainDF, englandDF, franceDF, italyDF, germanyDF])

    # Returns a df of the selected league. Without league name column

    return df[['Equipo', 'J', 'G', 'E', 'P', 'GF', 'GC', 'DIF', 'PTS']][df['Liga'] == league_input.lower()]


