import streamlit as st

from transformers import pipeline
pipe = pipeline("text-generation", model="facebook/xglm-564M")

