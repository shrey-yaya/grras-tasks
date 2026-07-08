import streamlit as st
import pickle
import pandas as pd

def recommend(restaurant_name):
    index = zomato_df[zomato_df['rest_name'] == restaurant_name].index[0]
    distances = similarity[index]
    restaurant_list = sorted(list(enumerate(distances)),key=lambda x:x[1],reverse=True)[1:6]
    
    recommended_restaurants = []
    urls = []
    for i in restaurant_list:
        recommended_restaurants.append(zomato_df.iloc[i[0]]['rest_name'])
        urls.append(zomato_df.iloc[i[0]]['rest_url'])

    return recommended_restaurants,urls     # it will return as a tuple


# IMPORTING various pickle files
# restaurants.pkl is actually zomato_df that we've exported from .ipynb file
zomato_df = pickle.load(open('restaurants.pkl','rb'))  
restaurants_list = zomato_df['rest_name'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(page_title='Recommendation-System')
st.title('Bangalore Restaurant Recommendation System👽')
selected_restaurant_name = st.selectbox('Select your preferred restaurant:-',restaurants_list)

if st.button('Recommend'):
    recommendations = recommend(selected_restaurant_name)
    
    restaurants = recommendations[0]
    url = recommendations[1]

    for i in range(5):
        st.subheader(restaurants[i])
        st.write(url[i])