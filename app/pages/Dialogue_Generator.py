import pandas as pd
import markovify
import streamlit as st

# Header
st.title("Dialogue Generator using Markov Chains")

def load_data():
    df = pd.read_csv("data/dataset/The_Office_lines.csv", index_col='id')
    df.drop(['scene'], axis = 1, inplace=True)
    df.rename({'line_text': 'line'}, axis=1, inplace=True)
    return(df)

df = load_data()

speakers = ('Michael',
            'Dwight',
            'Jim',
            'Pam',
            'Andy',
            'Kevin',
            'Angela',
            'Oscar',
            'Erin',
            'Ryan',
            'Darryl',
            'Phyllis',
            'Kelly',
            'Jan',
            'Toby',
            'Stanley',
            'Meredith',
            'Holly',
            'Nellie',
            'Creed')

# Defining the function
def dialogue_generator(speaker):
    # Get raw text as string.
    with open(f"data/character_lines/{speaker}_lines.txt", "r") as f:
        text = f.read()

    # Build the model.
    markov_model = markovify.NewlineText(text)
    
    return(markov_model.make_short_sentence(110))

# Taking user input
speaker = st.selectbox(label="Select a Character", options=speakers)
ok = st.button("Generate Dialogue")

# Generating dialogue
if ok == True:
    st.subheader(dialogue_generator(speaker))