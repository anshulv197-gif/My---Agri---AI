0import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (Browser mein kaisa dikhega)
st.set_page_config(page_title="Naughty's Agri-AI", page_icon="🌱")

# 2. API Key aur Model Setup
# Apni API Key yahan quotation marks ke andar likhein
API_KEY = "...gd4I" 
genai.configure(api_key=API_KEY)

# AI ki personality set karna
instruction = (
    "Aap Naughty ke personal assistant hain. Aap Agriculture aur Tech "
    "(jaise GIS, Remote Sensing) mein expert hain. Aapko sirf apne owner "
    "ko polite aur accurate jawab dene hain."
)

model = genai.GenerativeModel(
model_name='gemini-1.5-flash'

    system_instruction=instruction
)

# 3. UI Design
st.title("🌱 Naughty's Personal AI")
st.markdown("Agriculture aur Tech Expert Assistant")

# Chat history (Memory) ko initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Logic
if prompt := st.chat_input("Puchiye, Naughty..."):
    # User ka message save aur display karna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI se jawab mangna
    try:
        response = model.generate_content(prompt)
        full_response = response.text
        
        # Assistant ka jawab save aur display karna
        with st.chat_message("assistant"):
            st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    except Exception as e:
        st.error(f"Error: {e}")
