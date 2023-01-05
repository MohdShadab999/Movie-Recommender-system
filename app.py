import streamlit as st
import pickle
import pandas as pd
import requests

similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e7a67a1a99b1a8baae0175623b1c67cf&language=en-US'.format(movie_id))
    data=response.json()
    return 'http://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):

        movie_index = new_df[new_df['title'] == movie].index[0]
        dist = similarity[movie_index]
        movies = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
        rec_movie=[]
        rec_poster=[]
        for i in movies:
            movie_id=new_df.iloc[i[0]].movie_id
            rec_movie.append(new_df.iloc[i[0]].title)
            rec_poster.append(fetch_poster(movie_id))
        return rec_movie,rec_poster
st.title("Movie recommender system")

movies_titles=pickle.load(open('movies_title_dict.pkl','rb'))
new_df=pd.DataFrame(movies_titles)

selected_movie = st.selectbox(
    'Select a movie',
    (new_df['title']))


if st.button('Recommend'):
    rec_movie,poster=recommend(selected_movie)


    col1, col2, col3, col4, col5=st.columns(5)

    with col1:
        st.text(rec_movie[0])
        st.image(poster[0])

    with col2:
        st.text(rec_movie[1])
        st.image(poster[1])

    with col3:
        st.text(rec_movie[2])
        st.image(poster[2])

    with col4:
        st.text(rec_movie[3])
        st.image(poster[3])

    with col5:
        st.text(rec_movie[4])
        st.image(poster[4])
