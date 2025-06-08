import streamlit as st
import dwani

# API setup
dwani.api_key = "bhavyalahoti2906@gmail.com_dwani"
dwani.api_base = "https://dwani-dwani-api.hf.space"

# Page setup
st.set_page_config(page_title="Mental Health Assistant", page_icon="🧠", layout="centered")

# App header
st.markdown("<h1 style='text-align: center;'>🧠 Psychological And Mental<br>Health Assistant</h1>", unsafe_allow_html=True)
st.write("---")

# Prompt input
prompt_input = st.text_area("📝 Please Enter Your Question Or Health Issues:")

# Language selection
languages = {
    'English': 'english',
    'Kannada': 'kan_Knda',
    'Hindi': 'hin_Deva',
}

selected_language = st.selectbox("🌐 Choose Output Language:", options=list(languages.keys()))
tgt_lang_code = languages[selected_language]

# Handle response
if st.button("💬 Get Response"):
    if prompt_input.strip():
        full_prompt = (
            f"{prompt_input} - Note you are a psychologist whose job to enhance mental health "
            "of human beings no matter what questions people are asking you have to answer it "
            "and then two things you must have to add 1)how it can impact their mental health and "
            "2) Give prescriptions to improve their mental health in that situation. - don't finish "
            "your response without prescription manage tokens accordingly. -answer in 300 words atleast"
        )
        try:
            api_response = dwani.Chat.create(
                prompt=full_prompt,
                src_lang="eng_Latn",
                tgt_lang=tgt_lang_code
            )

            response_text = api_response["response"]

            st.markdown("### 📖 Response:")
            st.markdown(response_text)

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a prompt before submitting.")





