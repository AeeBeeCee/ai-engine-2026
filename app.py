import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCrvl1HVL4yt4tuFS2e0uGRtVcgCGOJkkA"

import streamlit as st
from engine.news_agent import fetch_news
from engine.writer_agent import generate_all_posts

st.set_page_config(page_title="2026 Verified AI Engine", layout="wide")

st.title("🛡️ Reliable Content Engine")
st.caption("Verified sources + AI drafting")

with st.sidebar:
    topic = st.text_input("Niche/Topic", "AI and Tech News")

if st.button("Generate Verified Content"):
    with st.spinner("Finding reliable sources..."):
        # Step 1: Fetch news with URLs
        raw_news = fetch_news(topic)
        
        # Step 2: Show the Sources (The "Reliability" Section)
        st.subheader("🔗 Verified Sources Found")
        st.info("Review these links to ensure the data is coming from trusted outlets.")
        st.markdown(raw_news) # This will show the links clearly
        
        st.divider()
        
        # Step 3: Generate the drafts based on those specific links
        final_content = generate_all_posts(raw_news)
        
        st.subheader("📢 Multi-Platform Drafts")
        st.text_area("Drafts for Review:", final_content, height=400)