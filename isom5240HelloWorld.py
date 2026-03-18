pip install -U pip
pip install -U "transformers>=4.35.0" tokenizers accelerate peft safetensors

import streamlit as st

from transformers import pipeline

pipe = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

st.write(messages)
