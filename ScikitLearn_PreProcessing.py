import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

## Import Dataset
data_df = pd.read_csv("cereal.csv")

## Data Imputation (Missing Data Replacement)
for col in data_df.columns :
    missing_data = data_df[col].isna().sum()
    missing_percent = missing_data/len(data_df)*100
    print(f"Column: {col} has {missing_percent}% missing data")

fig, ax = plt.subplots(figsize =(8, 5))
sns.heatmap(data_df.isna(), cmap="Blues", cbar=False, yticklabels=False)
plt.show()

x = data_df.iloc[:,0 : 3].values
y = data_df.iloc[:,3:4].values

from sklearn.impute import SimpleImputer
#Create an instance of Class SimpleImputer : np.nan is the empty value in the dataset
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1 : 3])
x[:, 1 : 3] = imputer.transform(x[:, 1 : 3])

## Encode Categorical Data
# *Step 1 : Encode Independent variable (X)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [('encode', OneHotEncoder(), [0])], remainder="passthrough")
x = ct.fit_transform(x)

# *Step 2 : Encode Dependent variable (Y)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

## Splitting the dataset(X-data, Y-output) into the Training set and Test set
from sklearn.model_selection import train_test_split
np.random.seed(42)
x_train, x_test , y_train, y_test = train_test_split(x, y, test_size=0.2)

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
print(x_test)
