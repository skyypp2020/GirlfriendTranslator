import streamlit as st
import aisuite as ai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="員瑛式思考產生器",
    page_icon="🌈",
    layout="centered"
)

# Function to generate reply
def reply(prompt, provider="groq", model="openai/gpt-oss-120b"):
    system = """
    請用台灣習慣的中文來寫這段 po 文：
    請用員瑛式思考, 也就是什麼都正向思維任何使用者寫的事情,
    用我的第一人稱、社群媒體 po 文的口吻說一次,
    說為什麼這是一件超幸運的事, 並且以「完全是 Lucky Vicky 呀!」結尾。
    可以適度的加上 emoji。
    """
    
    try:
        client = ai.Client()
        
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model=f"{provider}:{model}",
            messages=messages
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"發生錯誤: {str(e)}\n請確認您的 API Key 是否正確設定。"

# UI Layout
st.title("꒰*ˊᵕˋ꒱ 員瑛式思考產生器 Lucky Vicky 🌈")
st.markdown("""
請輸入一件你覺得超小事，甚至有點倒楣的事，讓我幫你用員瑛式思考，超正向的方式重新詮釋！
""")

# Input section
user_input = st.text_area("今天發生的事情是…", placeholder="例如：今天出門就下大雨, 可是忘了帶傘...", height=100)

# Sidebar for potentially changing models (Optional but good for flexibility)
with st.sidebar:
    st.header("設定")
    # Check for keys to offer options, default to Groq as per requirement
    provider = st.selectbox("選擇供應商", ["groq", "openai", "mistral"], index=0)
    
    model_options = {
        "groq": ["openai/gpt-oss-120b", "llama-3.3-70b-versatile", "gemma2-9b-it"],
        "openai": ["gpt-4o", "gpt-3.5-turbo"],
        "mistral": ["ministral-8b-latest"]
    }
    
    model = st.selectbox("選擇模型", model_options.get(provider, []), index=0)
    
    # Simple check for API Key existence in env
    key_var_map = {
        "groq": "GROQ_API_KEY",
        "openai": "OPENAI_API_KEY",
        "mistral": "MISTRAL_API_KEY" # aisuite might expect specific env vars, usually it's PROVIDER_API_KEY style or specific ones
    }
    
    if os.getenv(key_var_map.get(provider)):
        st.success(f"{provider} API Key 已設定")
    else:
        st.warning(f"未偵測到 {provider} API Key，請檢查 .env 檔案")

# Button and Output
if st.button("Lucky Vicky 魔法! ✨", type="primary"):
    if user_input:
        with st.spinner("正在施展魔法中..."):
            result = reply(user_input, provider, model)
            st.subheader("📣 員瑛式貼文")
            st.success(result)
            st.balloons()
    else:
        st.warning("請先輸入發生了什麼事喔！")

