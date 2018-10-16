import pandas as pd


PATH = 'athlete_events.csv.zip'


def main():
    data = pd.read_csv(PATH)
    print(data[:5].columns)
    print(data.loc[data['Name'] == 'Dimitrios Loundras'])
    print(data.iloc[data.loc[data['Sex'] == 'M' & data['']]['Age'].idxmin()])
    print("------------------------")
    print(data.iloc[data.loc[data['Sex'] == 'F']['Age'].idxmin()])


if __name__ == "__main__":
    main()
