import streamlit as st
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from alternate_groups import FindAlternateGroups
import base64

# Initialize the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

#Generate a downloadable link format
def get_download_link(content, filename, text):
    content = json.dumps(content)
    b64 = base64.b64encode(content.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/json;base64,{b64}" download="{filename}">{text}</a>'
    return href

# The Streamlit application.
def main():
    st.title("Domain Alternate Groups Finder")
    
    domain = st.text_input("Enter the domain name", "")
    if st.button("Submit"):
        if domain:
            results = FindAlternateGroups(domain,model)
            st.write("Here are the product alternate groups:")
            max_display = 5
            for item in results[:max_display]:
                st.write("Product Alternates:")
                for url in item["product alternates"]:
                    st.markdown(f"[Link]({url})")
            st.markdown(get_download_link(results, "results.json", "Download results in JSON format"), unsafe_allow_html=True)
        else:
            st.write("Please enter a domain name.")

if __name__ == "__main__":
    main()