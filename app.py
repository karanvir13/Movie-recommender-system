import pickle
import streamlit as st
import pandas as pd



def set_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4")


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:10]
    recommended_movie_name=[]
    for i in distances[1:10]:
        recommended_movie_name.append(movies.iloc[i[0]].title)

    return recommended_movie_name


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_name= recommend(selected_movie)
    # col1, col2,col3,col4 = st.columns(4)
    # with col1:
    st.text("1."+recommended_movie_name[0])
    # with col2:

    st.text("2. "+recommended_movie_name[1])
    # with col3:
    st.text("3. "+recommended_movie_name[2])
    # with col4:
    st.text("4. "+recommended_movie_name[3])
        # col5, col6,col7,col8 = st.columns(4)
    # with col1:
    st.text("5."+recommended_movie_name[4])
    # with col2:

    st.text("6. "+recommended_movie_name[5])
    # with col3:
    st.text("7. "+recommended_movie_name[6])
    # with col4:
    st.text("8. "+recommended_movie_name[7])

