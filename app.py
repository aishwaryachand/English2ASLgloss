import streamlit as st
from transformers import AutoTokenizer, T5ForConditionalGeneration

@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("final_t5_gloss_model")
    tokenizer = AutoTokenizer.from_pretrained("final_t5_gloss_model")
    return model, tokenizer

model, tokenizer = load_model()

def translate_to_gloss(text):
    input_text = "translate English to Gloss: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    output_ids = model.generate(input_ids, max_length=64)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

st.title("English to ASL Gloss Translator")
user_input = st.text_area("Enter an English sentence:")

if st.button("Translate"):
    if user_input.strip():
        gloss = translate_to_gloss(user_input)
        st.success(f"Gloss Output: {gloss}")
    else:
        st.warning("Please enter a sentence.")
