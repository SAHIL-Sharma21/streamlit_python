# layout in streamlit 
import streamlit as st

st.title("Layout in stremlit")

col_1, col_2 = st.columns(2)

with col_1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/1872900/pexels-photo-1872900.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", width=200)
    vote_one = st.button("Vote Masala chai")

with col_2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/1638280/pexels-photo-1638280.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", width=200)
    vote_two = st.button("Vote Adrak Chai")

if vote_one:
    st.success("Thanks for voting Masala chai")
elif vote_two:
    st.success("Thanks for voting Adrak Chai")

# sidebar
name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "Kesar", "Adrak"])

st.write(f"Welcome {name} your {tea} is ready!")

with st.expander("Show Chai Making Instruction"):
    st.write('''
    1. Boil Water with tea leaves
    2. Add milk and spices
    3. Serve hot
    ''')

# write markdown
st.markdown('### Welcome to my blogs')
st.markdown('> Blockquote')