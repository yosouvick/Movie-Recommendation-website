import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    #we apply a api to fetch thw poster of the mvie
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500"+poster_path
    return full_path
    

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:11]
    # movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies_name=[]
    recommended_movies_poster=[]
    for i in distances[0:10]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        #fetching the poster through api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name,recommended_movies_poster

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")

selected_movie_name=st.selectbox(
    "want to watch a movie?",
    movies['title'].values
)

if st.button("Recommend movies"):
    names,posters=recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    # with col6:
    #     st.text(names[5])
    #     st.image(posters[5])
    # with col7:
    #     st.text(names[6])
    #     st.image(posters[6])
    # with col8:
    #     st.text(names[7])
    #     st.image(posters[7])
    # with col9:
    #     st.text(names[8])
    #     st.image(posters[8])
    # with col10:
    #     st.text(names[9])
    #     st.image(posters[9])
