from dotenv import load_dotenv
import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖", layout="centered")

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6a6a, #ffb86c, #8be9fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        text-align: center;
        color: #999;
        margin-bottom: 1.5rem;
    }
    .mode-badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        background: #262730;
        color: #fafafa;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🤖 GenAI Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Pick a mode, then start chatting</div>', unsafe_allow_html=True)

model = ChatMistralAI(model="mistral-small-2603", temperature=0.7, max_tokens=100)

MODE_MAP = {
    "😢 Sad Mode": "You are a Sad AI Agent",
    "😂 Funny Mode": "You are a Funny AI Agent",
    "😠 Angry Mode": "You are an Angry AI Agent",
}

# ---------- Mode selection (locked once chat has started, same as CLI's one-time choice) ----------
if "mode_label" not in st.session_state:
    st.session_state.mode_label = None
    st.session_state.messages = None

if st.session_state.mode_label is None:
    st.write("**Choose your AI model:**")
    choice = st.radio(
        "Select a mode",
        list(MODE_MAP.keys()),
        label_visibility="collapsed",
    )
    if st.button("Start Chat 🚀", use_container_width=True):
        st.session_state.mode_label = choice
        st.session_state.messages = [SystemMessage(content=MODE_MAP[choice])]
        st.rerun()

else:
    st.markdown(f'<div class="mode-badge">Mode: {st.session_state.mode_label}</div>', unsafe_allow_html=True)

    # Render existing conversation (skip the system message)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    prompt = st.chat_input("Type your message...")

    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.write(response.content)

    if st.button("🔄 Change Mode"):
        st.session_state.mode_label = None
        st.session_state.messages = None
        st.rerun()