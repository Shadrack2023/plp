import pandas as pd

data = {"Name": ["Shadrack", "Otieno", "Mwabe", "Melvin", "Tabitha"],
        "Department": ["Finance", "Marketing", "Software Development", "ICT", "Executive"],
        "Gross Salary": [300000,250000,850000,600000,1600000]
        }

print(f'Original Data frame')
pf = pd.DataFrame(data)
print(pf)

