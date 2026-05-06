import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Naughty's Agri-AI", page_icon="🌱")

# 2. API Key Setup
# IMPORTANT: Niche "PASTE_YOUR_KEY_HERE" ki jagah apni asli API Key dalein
API_KEY = "AIzaSyAGuIK5pstHzXHiGCqN6RU2LsAAtsHgd4I" 
genai.configure(api_key=API_KEY)

# 3. AI ki Personality (System Instruction)
instruction = (
    "Aap Naughty ke personal assistant hain. Aap Agriculture aur Tech "
    "(jaise GIS, Remote Sensing, Agri-Informatics) mein expert hain. "
    "Aapko polite aur accurate jawab dene hain."
)

# 4. Model Setup
model = genai.GenerativeModel(
    model_name='gemini-1.9-flash',
    system_instruction=instruction
)

# 5. Chat History Maintain Karna
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌱 Naughty's Personal AI")
st.markdown("Agriculture aur Tech Expert Assistant")

# Purani baatein dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Input aur AI Response
if prompt := st.chat_input("Puchiye, Naughty..."):
    # User ka message add karein
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI se jawab mangna
        response = model.generate_content(prompt)
        ai_message = response.text
        
        # AI ka message dikhana aur save karna
        with st.chat_message("assistant"):
            st.markdown(ai_message)
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
    
    except Exception as e:
        # Agar koi galti ho toh error dikhaye
        st.error(f"Dikkat aa rahi hai: {e}")

