from collections import defaultdict

from codebase import nsfg

# reading the dataset from file and saving in dataframe variable
df = nsfg.ReadFemPreg()
print(df.describe())
