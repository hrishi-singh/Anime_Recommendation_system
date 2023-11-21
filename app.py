import streamlit as st
import pickle
import pandas as pd
from PIL import Image


page_bg_img = '''
<style>
.e1g8pov65{
background-image: url("https://cdn.dribbble.com/users/642793/screenshots/17362730/media/c42f55137545c97f6214851614e1b9b1.png?compress=1&resize=768x576&vertical=top");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)





image = Image.open('char1.png')
image2 = Image.open('char2.png')

with open("style.css") as style:
    st.markdown(f"<style>{style.read()}</style>",unsafe_allow_html=True)
def recommend(anime):
    anime_index=animes[animes['title']==anime].index[0]
    distances=similarity[anime_index]
    animes_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_anime=[]
    for i in animes_list:
        recommend_anime.append(animes.iloc[i[0]].title)
    return recommend_anime


animes_dict=pickle.load(open('animes_dict.pkl','rb'))
animes=pd.DataFrame(animes_dict)

similarity=pickle.load(open('similar.pkl','rb'))


c1,c2,c3 = st.columns(3)



st.title('Anime Recommendation System')

selected_anime=st.selectbox("",animes['title'].values)

if st.button('Recommend'):
    rec=recommend(selected_anime)
    col0,col1, col2, col3,col4 = st.columns(5)
    cols=[col0,col1,col2,col3,col4]
    for i in rec:
        cols[rec.index(i)].write(f'{rec.index(i)+1}.\n{i}')