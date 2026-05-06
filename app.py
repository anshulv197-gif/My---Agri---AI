import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Naughty's Agri-AI", page_icon="🌱")

# 2. API Key Setup (Maine aapki key yahan daal di hai)
API_KEY = "AIzaSyAGuIK5pstHzXHiGCqN6RU2LsAAtsHgd4I" 
genai.configure(api_key=API_KEY)

# 3. AI ki Personality (System Instruction)
instruction = (
    "Aap Naughty ke personal assistant hain. Aap Agriculture aur Tech "
    "(jaise GIS, Remote Sensing, Agri-Informatics) mein expert hain. "
    "Aapko polite aur accurate jawab dene hain."
)

# 4. Model Setup (Sahi model name ke saath)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=instruction
)

# 5. Chat History Maintain Karna
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌱 Naughty's Personal AI")
st.markdown("Agriculture aur Tech Expert Assistant")

# Purani chats dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Input aur AI Response
if prompt := st.chat_input("Puchiye, Naughty..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI se response lena
        response = model.generate_content(prompt)
        ai_message = response.text
        
        with st.chat_message("assistant"):
            st.markdown(ai_message)
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
    
    except Exception as e:
        # Agar fir bhi koi error aaye toh yahan dikhega
        st.error(f"Dikkat aa rahi hai: {e}")
