import streamlit as st




from transformers import pipeline

import streamlit as st
import sys, inspect, importlib, types

st.write("python:", sys.version)
try:
    import transformers as tfmod
    st.write("transformers object type:", type(tfmod))
try:
    st.write("transformers repr:", repr(tfmod)[:200])
    except:
pass
try:
    st.write("transformers.name:", getattr(tfmod, "name", "MISSING"))
    st.write("transformers.file:", getattr(tfmod, "file", "MISSING"))
    st.write("transformers attributes sample:", sorted(list(n for n in dir(tfmod) if not n.startswith("_")) )[:40])
    except Exception as e:
    st.write("error inspecting transformers module:", str(e))
# Try to import cache_utils explicitly
try:
    importlib.invalidate_caches()
    cu = importlib.import_module("transformers.cache_utils")
    st.write("cache_utils file:", getattr(cu, "file", "MISSING"))
    st.write("SlidingWindowCache in cache_utils:", hasattr(cu, "SlidingWindowCache"))
except Exception as e:
    st.write("cache_utils import error:", str(e))
except Exception as e:
    st.write("transformers import error (full):", str(e))



pipe = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

st.write(messages)
