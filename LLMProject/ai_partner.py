import os
from openai import OpenAI
import streamlit as st
from pyexpat.errors import messages
from datetime import datetime
import json

# 设置页面的配置项
st.set_page_config(
    page_title="AI_Partner",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 侧边栏
    initial_sidebar_state="expanded",
    menu_items={}
)


# 生成会话标识
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")


# 保存会话信息
def save_session():
    if st.session_state.current_session:
        session_data = {
            "name": st.session_state.name,
            "character": st.session_state.character,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)


# 加载所有的历史信息
def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for file in file_list:
            if file.endswith(".json"):
                session_list.append(file[:-5])
    session_list.sort(reverse=True)
    return session_list


# 加载指定会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.name = session_data["name"]
                st.session_state.character = session_data["character"]
                st.session_state.current_session = session_name
    except Exception as e:
        st.error("加载会话失败")


# 删除会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            if st.session_state.current_session == session_name:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception as e:
        st.error("删除会话失败")


# 大标题
st.title("AI_Partner")

# logo
st.logo("resources/cat.png")

# 系统提示词
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
规则：
    1. 每次只回1条消息
    2. 禁止任何场景或状态描述性文字
    3. 匹配用户的语言
    4. 回复简短，像微信聊天一样
    5. 有需要的话可以用emoji表情
    6. 用符合伴侣性格的方式对话
    7. 回复的内容，要充分体现伴侣的性格特征
伴侣性格：
    - %s
你必须严格遵守上述规则来回复用户。
"""

# 初始化信息
if "messages" not in st.session_state:
    st.session_state.messages = []
if "name" not in st.session_state:
    st.session_state.name = "顾珩"
if "character" not in st.session_state:
    st.session_state.character = "陆家嘴金融男"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 展示聊天信息
st.text(f"会话名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 创建客户
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 侧边栏
with st.sidebar:
    # 会话信息
    st.subheader("AI_Partner_Info")
    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        save_session()

        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()
    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(session, width="stretch", icon="📄", key=f"load_{session}",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.divider()

    name = st.text_area("名称", placeholder="请输入名称……", value=st.session_state.name)
    if name:
        st.session_state.name = name
    character = st.text_area("性格", placeholder="请输入性格……", value=st.session_state.character)
    if character:
        st.session_state.character = character

# 消息输入框
prompt = st.chat_input("请输入……")
if prompt:
    st.chat_message("user").write(prompt)
    print("调用AI大模型……，提示词：", prompt)
    # 保存用户的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.name, st.session_state.character)},
            *st.session_state.messages
        ],
        stream=True
    )

    # 输出AI大模型的结果（非流式输出）
    # print("AI大模型的结果：", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出AI大模型的结果（流式输出）
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存AI大模型的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    save_session()
