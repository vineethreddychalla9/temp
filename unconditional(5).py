import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/KMITDS/CS601PC/main/individual.csv")
print(df.head(10))
print("P(recreation=golf)=",df[(df.recreation=='golf')].shape[0] / df.shape[0])
res = df[(df.status=="single") & (df.cw=="medRisk")].shape[0] / df[(df.cw=="medRisk")].shape[0]
print("(status=single/creditworthiness=medRisk) = ",res)
'''
Output:
P(recreation=golf) = 0.4
P(status=single/creditworthiness=medRisk)= 0.6666666666666666

'''
