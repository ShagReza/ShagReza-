# make mock data
import pandas as pd
# Load your dataframe
df = pd.read_parquet("WDR91.parquet", columns=['LABEL','ECFP4','ECFP6','MACCS','TOPTOR'], engine='pyarrow')
df['LABEL'] = df['LABEL'].astype(int)
df.to_parquet("WDR91_fixed.parquet", index=False)

df_0 = df[df['LABEL'] == 0].sample(n=100)
df_1 = df[df['LABEL'] == 1].sample(n=1000)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TrainFiles\sampled_data_train_1.parquet", index=False)  

df_0 = df[df['LABEL'] == 0].sample(n=200)
df_1 = df[df['LABEL'] == 1].sample(n=2000)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TrainFiles\sampled_data_train_2.parquet", index=False)  


df_0 = df[df['LABEL'] == 0].sample(n=300)
df_1 = df[df['LABEL'] == 1].sample(n=3000)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TrainFiles\sampled_data_train_3.parquet", index=False) 



df_0 = df[df['LABEL'] == 0].sample(n=10)
df_1 = df[df['LABEL'] == 1].sample(n=100)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TestFiles\sampled_data_test_1.parquet", index=False) 



df_0 = df[df['LABEL'] == 0].sample(n=20)
df_1 = df[df['LABEL'] == 1].sample(n=200)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TestFiles\sampled_data_test_2.parquet", index=False) 

df_0 = df[df['LABEL'] == 0].sample(n=200)
df_1 = df[df['LABEL'] == 1].sample(n=200)
df_sampled = pd.concat([df_0, df_1], ignore_index=True)
df_sampled.to_parquet("Data\TestFiles\sampled_data_test_3.parquet", index=False) 