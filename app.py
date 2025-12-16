import streamlit as st
import aisuite as ai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="男友求生翻譯機",
    page_icon="🦁",
    layout="centered"
)

# Function to generate reply
def reply(prompt, provider="groq", model="openai/gpt-oss-120b"):
    system = """
    你是一個「求生型男友翻譯 AI」。

    請將女朋友的話翻譯成：
    - 官方說法
    - 內心 OS
    - 真正意思
    - 男友存活率最高的回覆

    女朋友說：
    「{user_input}」

    請用幽默但寫實的語氣。
    """.replace("{user_input}", prompt)
    
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
st.title("🦁 男友求生翻譯機")
st.markdown("""
女友說的話，往往不是表面上的意思...
輸入她說的一句話，讓 AI 幫你解析 **真正意思** 與 **最佳回覆**，提高存活率！
""")

# Input section
user_input = st.text_area("女朋友說：", placeholder="例如：沒事，你去忙吧...", height=100)

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
        "mistral": "MISTRAL_API_KEY"
    }
    
    if os.getenv(key_var_map.get(provider)):
        st.success(f"{provider} API Key 已設定")
    else:
        st.warning(f"未偵測到 {provider} API Key，請檢查 .env 檔案")

# Button and Output
if st.button("翻譯 (求生模式啟動) 🚀", type="primary"):
    if user_input:
        with st.spinner("正在分析女友情緒..."):
            result = reply(user_input, provider, model)
            st.subheader("翻譯結果")
            st.markdown(result)
    else:
        st.warning("請先輸入女朋友說的話喔！")
