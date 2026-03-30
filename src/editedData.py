import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder,StandardScaler
 
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "..", "data", "heart.csv")
df = pd.read_csv(data_path)
# print(df.head())

#katagorik veriler
categorical_columns=['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope']

#label  ile bu kolonları sayısal hale çevirelim
le=LabelEncoder()
for column in categorical_columns:
    df[column]=le.fit_transform(df[column])

#kontrol edelim
# print(df.head())


#sayısal kolonları ölçeklendirelim 

numeric_columns=['Age','Cholesterol','RestingBP','FastingBS','MaxHR','Oldpeak','HeartDisease']
scaler=StandardScaler()
df[numeric_columns]=scaler.fit_transform(df[numeric_columns])

df.to_csv('arranged heart.csv',index=False)
print(df.head())