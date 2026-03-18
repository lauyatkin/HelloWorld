import streamlit as st




from transformers import pipeline

import sys, inspect
st.write("python:", sys.version)
    try:
    import transformers
    st.write("transformers.version:", transformers.version)
    st.write("transformers file:", inspect.getsourcefile(transformers))
    try:
    importlib = import("importlib")
    importlib.invalidate_caches()
    import transformers.cache_utils as _cu
    st.write("cache_utils file:", inspect.getsourcefile(_cu))
    st.write("has SlidingWindowCache:", hasattr(_cu, "SlidingWindowCache"))
    except Exception as e:
    st.write("cache_utils import error:", str(e))
    except Exception as e:


pipe = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

st.write(messages)
