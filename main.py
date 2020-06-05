import pandas
import brain as bs
from sklearn.preprocessing import LabelEncoder
boobydata = pandas.read_csv('booby_Data.csv')
x = boobydata.iloc[:,2:32].values
y = boobydata.iloc[:,1].values
label = LabelEncoder()
Y = label.fit_transform(y)
bs.brain.brain_processing(x,Y)