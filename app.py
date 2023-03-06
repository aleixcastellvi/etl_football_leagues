import sys
import argparse

from datetime import date
from etl.data_extract import *


def main():

	# Parser
	parser = argparse.ArgumentParser()
	parser.add_argument("--country", type = str, required = False, help = "use: Spain, England, France, Itlay or Germany")
	args = parser.parse_args()

	# Ask user input if not provided
	args.country = args.country if args.country is not None else input("country: ")

	# Obtain current date
	today = date.today()

	# Get df of url leagues
	df_leagues = get_urls()

	print("\nData is being obtained...\n")

	# Get the df statistics by league
	df = data_processing(df_leagues, args.country)

	print("-----------------------------------------")
	print("Soccer statistics of the country: {}".format(args.country))
	print("Results to date: {}".format(today))
	print("-----------------------------------------\n")

	print(df)


if __name__ == "__main__":
    main()
