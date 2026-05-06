import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Naughty's Agri-AI", page_icon="🌱")

# 2. API Key Setup
API_KEY = "AIzaSyAGuIK5pstHzXHiGCqN6RU2LsAAtsHgd4I" 
genai.configure(api_key=API_KEY)

# 3. AI ki Personality
instruction = "Aap Naughty ke personal assistant aur Agriculture expert hain."

# 4. Model Setup (Line 20 aur 21 ko dhyan se dekhein)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    system_instruction=instruction
)

# 5. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌱 Naughty's Personal AI")

# Purani baatein dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Input aur Response
if prompt := st.chat_input("Puchiye, Naughty..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(prompt)
        ai_message = response.text
        with st.chat_message("assistant"):
            st.markdown(ai_message)
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
    except Exception as e:
        st.error(f"Dikkat aa rahi hai: {e}")

