import pickle

import pandas as pd
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e6320536119b96235dc12c43e5190b7d&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def fetch_url(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e6320536119b96235dc12c43e5190b7d&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    return data['homepage']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies_name = []
    recommended_movies_poster = []
    recommended_movies_urls = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_urls.append(fetch_url(movie_id))
        # fetch poster from
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name, recommended_movies_poster, recommended_movies_urls


with open('movies.pkl', 'rb') as f:
    movies = pd.read_pickle(f)
with open('similarity.pkl', 'rb') as f:
    similarity = pd.read_pickle(f)

st.title('World of Movies')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    names, poster, urls = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
        st.markdown("[Visit](%s)" % urls[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])
        st.markdown("[Visit](%s)" % urls[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
        st.markdown("[Visit](%s)" % urls[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])
        st.markdown("[Visit](%s)" % urls[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
        st.markdown("[Visit](%s)" % urls[4])



