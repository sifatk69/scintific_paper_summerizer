from transformers import pipeline
from pathlib import Path
import streamlit as st
from transformers import LEDForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM
import torch


def _sanitize_path(self, relative_path):
    print(f"Relative Path: {relative_path}")  # <-- Add this line
    return Path(relative_path).resolve()


st.title("Summarize Text")
sentence = st.text_area('Please paste your article :', height=30)
button = st.button("Summarize")

with st.spinner("Generating Summary.."):
    if button and sentence:
        summarizer = pipeline("summarization", model="./model/falconsai")

        summ=summarizer(sentence,max_length=2000, min_length=100, do_sample=False)

        st.write(summ)
