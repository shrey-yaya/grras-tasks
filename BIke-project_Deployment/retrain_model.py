import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv('Used_Bikes.csv')

# Drop bike_name
df = df.drop('bike_name', axis=1)

# Cast age
df['age'] = df['age'].astype(int)

# Map owner
dic = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth Owner Or More': 4}
df['owner'] = df['owner'].map(dic)

# Filter cities with at least 10 bikes
city_name = [
    'Delhi', 'Bangalore', 'Mumbai', 'Hyderabad', 'Pune', 'Chennai', 'Lucknow', 'Jaipur',
    'Ghaziabad', 'Ahmedabad', 'Noida', 'Bhopal', 'Gautam Buddha Nagar', 'Kanchipuram',
    'Jodhpur', 'Karnal', 'Allahabad', 'Rupnagar', 'Gurgaon', 'Godhara', 'Faridabad',
    'Perumbavoor', 'Kadapa', 'Ludhiana', 'Kolkata', 'Thane', 'Jhansi', 'Vadodara',
    'Surat', 'Jalandhar', 'Chandigarh', 'Rajkot', 'Indore', 'Dehradun', 'Patna',
    'Navi Mumbai', 'Nagpur', 'Coimbatore', 'Guwahati', 'Tiruvallur', 'Bhubaneshwar',
    'Howrah', 'Kanpur', 'Aurangabad', 'Cuttack', 'Visakhapatnam', 'Alibag', 'Alipore',
    'Nashik', 'Ranchi', 'Kalyan', 'Rohtak', 'Udaipur', 'Gorakhpur', 'Agra', 'Kota',
    '24 Pargana', 'Meerut', 'Gandhinagar', 'Ernakulam'
]
maxc_ten_bike = df[df['city'].isin(city_name)]

# Filter brands with at least 10 bikes
bikes_name = df['brand'].value_counts()
most_available_bikes = bikes_name[bikes_name > 10].keys()
greater_than_ten_bike = maxc_ten_bike[maxc_ten_bike['brand'].isin(most_available_bikes)]

# Map brand
bike_encoding_dict = {
    'Bajaj': 3, 'Hero': 16, 'Royal Enfield': 1, 'Yamaha': 5, 'Honda': 6, 'Suzuki': 7,
    'TVS': 8, 'KTM': 2, 'Harley-Davidson': 4, 'Kawasaki': 9, 'Hyosung': 10, 'Benelli': 11,
    'Mahindra': 12, 'Triumph': 13, 'Ducati': 14, 'BMW': 15
}
greater_than_ten_bike['brand'] = greater_than_ten_bike['brand'].map(bike_encoding_dict)

df2 = greater_than_ten_bike

# Remove outliers using IQR
numerical_data = df2.select_dtypes(exclude='O')
lower_limit = dict()
uper_limit = dict()

for colum in numerical_data.columns:
    q1, q3 = df2[colum].quantile([.25, .75])
    IQR = q3 - q1
    LL = q1 - (1.5 * IQR)
    UL = q3 + (1.5 * IQR)
    lower_limit[colum] = LL
    uper_limit[colum] = UL

for lower_upper_pairs in list(zip(uper_limit.items(), lower_limit.items())):
    df2 = df2[(df2[lower_upper_pairs[0][0]] >= lower_upper_pairs[1][1]) & (df2[lower_upper_pairs[0][0]] <= lower_upper_pairs[0][1])]

# Drop city
df2 = df2.drop('city', axis=1)

# Separate features and target
x = df2.drop('price', axis=1)
y = df2[['price']]

# Train test split (using same random state as notebook)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
rdf = RandomForestRegressor(random_state=42)
rdf.fit(x_train, y_train.values.ravel())

# Evaluate
print("Training accuracy:", rdf.score(x_train, y_train))
print("Testing accuracy:", rdf.score(x_test, y_test))

# Save model
joblib.dump(rdf, 'updated_model.lb')
print("Model saved to updated_model.lb successfully!")
