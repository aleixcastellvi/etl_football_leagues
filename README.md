# ETL Football Leagues

## Description

ETL Football Leagues

With this application, you will be able to obtain the soccer statistics of the 5 main leagues in Europe.

The first step will be to indicate by command line, the country of the first league that you want to analyze. The options are: Spain, England, France, Italy and Germany.

If no country is specified on the command line, the application will generate a prompt to enter the country.

After indicating the country, the application, internally, will go to www.espn.com to obtain the data of interest with a web scraping process

These obtained data will be processed and transformed to generate a complete and clean dataframe.

The last action of the application will be to show the statistics of the league of interest through the terminal.

## Step by step installation and program execution process

### Prerequisites

- python
- pip

### Get code

A zip file with the code is attached. It must be saved and unzipped in the working path with the desired name (for example: etl_football_leagues)

### Create a virtualenv for the project

```sh
$ pip install virtualenv
$ cd etl_football_leagues
$ virtualenv venv
$ source venv/bin/activate
$ pip install pandas
$ pip install lxml
```

## Execute project

```
$ python3 app.py --country=[ARG]
```

IMPORTANT:

- ARG must be one of the following countries: Spain, England, France, Italy or Germany. It doesn't matter how you write it. If no ARG is inserted, the following command line will prompt for input

Example: 

```
$ python3 app.py --country=FRANCE
```

## Output program

In this example, the output will be the statistics of the first French soccer league up to the current date.
