import pandas as pd

data = {
    "Name": ['Ayush', 'Prateek', 'Drish'],
    "Age": [21,20,20],
    "City":["Bengaluru", "Bengaluru", "Delhi"]
}

df = pd.DataFrame(data)
print(df)