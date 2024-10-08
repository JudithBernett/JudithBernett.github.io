import pandas as pd

data = pd.read_csv("https://docs.google.com/spreadsheets/d/1QUIfIUywLN-Z-y6D"
                   "-xJdpJeTi3fVEU5dU7dRKnboKUk/export?gid=0&format=csv")

# transform Ankunftszeit (hh:mm) and Datum (dd.mm.yyyy) to one datetime column
data["Datum"] = pd.to_datetime(data["Datum"], format="%d.%m.%y")
data["Datum"] = pd.to_datetime(data["Datum"].dt.strftime("%Y-%m-%d") + " " + data["Ankunftszeit"],
                               format="%Y-%m-%d %H:%M")

# if the 3<=month<=5, write 🌷in the Jahreszeit column, if 6<=month<=8, write 🌞, if 9<=month<=11, write 🍂, else 🌨
data["Jahreszeit"] = data["Datum"].dt.month.apply(lambda x: "🌷" if 3 <= x <= 5 else "🌞" if 6 <= x <= 8 else "🍂" if 9 <= x <= 11 else "🌨")

# drop the original columns
data.drop(columns=["Ankunftszeit"], inplace=True)
# sort by Datum
data.sort_values(by="Datum", inplace=True)
# save as csv
data.to_csv("gym.csv", index=False)
