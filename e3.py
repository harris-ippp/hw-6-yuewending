
years = []
with open("election_year_id.txt", "r") as f:
    items = f.read().split('\n')
    for item in items:
        if item!= "":
            years.append(item.split()[0])
        
years.reverse()
        
import pandas as pd

data = {}
counties = ["Accomack County","Albemarle County","Alexandria City","Alleghany County"]

for county in counties:
    data[county] = { "Year" : [], "Share" : []}

for year in years:
    
    filename = "year_" + year + ".csv"
    header = pd.read_csv(filename, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
        
    df = pd.read_csv(filename, index_col = 0,
                   thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = int(year)
    df["Share"]= df["Republican"] / df["Total Votes Cast"]
    
    for county in counties:
        if county not in df.index:
            continue
        
        data[county]["Year"].append(int(year))
        data[county]["Share"].append(df.loc[county]['Share'])

        
for county in counties:
    
    df = pd.DataFrame(data[county])
    ax = df.plot(x="Year", y="Share")
    ax.figure.savefig(county.lower().replace(" ","_") + ".pdf")
    