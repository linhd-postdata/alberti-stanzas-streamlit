import streamlit as st
from PIL import Image
from core import get_stanzas

st.set_page_config(
    page_title="Stanza type detection - POSTDATA",
    page_icon="🏷️",
)
image = Image.open('postdata-logo-2.png')
st.sidebar.image(image)
st.sidebar.write("""
This is a demo for the ALBERTI language model trained for stanza type detection.
ALBERTI is a set of two BERT-based multilingual model for poetry. 
One for verses and another one for stanzas. 
This model has been further trained with the PULPO corpus. 
Paste or write your own your own poem and click the button to try it.
Read more: https://huggingface.co/flax-community/alberti-bert-base-multilingual-cased""")
st.header('Stanza type detection with alBERTi model')
poem = st.text_area("Write your own poem", value="""Mientras por competir con tu cabello,
oro bruñido al sol relumbra en vano;
mientras con menosprecio en medio el llano
mira tu blanca frente el lilio bello;

mientras a cada labio, por cogello.
Siguen más ojos que al clavel temprano;
y mientras triunfa con desdén lozano
del luciente cristal tu gentil cuello""", height=320,
                    help="Make sure you split the stanzas propperly.")

if st.button("Detect stanzas type"):
    stanzas = get_stanzas(poem)
    st.table(stanzas.values())
