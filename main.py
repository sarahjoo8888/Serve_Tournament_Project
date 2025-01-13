import pandas as pd
import numpy as np

def main():
    try:
        # ask for data path
        file_path = input("Please Enter the path to your CSV file: ")

        # read file into dp
        data = pd.read_csv(file_path)
        print("\nCSV file loaded!")
        print(data.head())  

        # number of teams at the tournament
        num_teams = int(input("Enter the number of teams: "))

    except FileNotFoundError:
        print("Error: The file was not found. Please check the path and try again.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")


if __name__ == "__main__":
    main()
