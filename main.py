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

        # create another dataframe containing the Team numbers of each game
        teams = data.select_dtypes(include=np.number)

        score = pd.DataFrame()
        score[["Left 1", "Right 1"]] = data["Score Court 1"].str.split("-", expand=True)
        score[["Left 2", "Right 2"]] = data["Score Court 2"].str.split("-", expand=True)
        print(score)
    except FileNotFoundError:
        print("Error: The file was not found. Please check the path and try again.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")


if __name__ == "__main__":
    main()
