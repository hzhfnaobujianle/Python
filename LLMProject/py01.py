import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="猫酱",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 侧边栏
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("big")
st.header("middle")
st.subheader("small")

# 段落文字
st.write("布偶猫是公认的 “仙女猫”，体态优雅蓬松，毛发柔软顺滑如丝绒，体型偏大却气质温柔。")
st.write(
    "它们有着澄澈明亮的蓝眼睛，像盛着一汪湖水，面部、耳朵、四肢与尾部常带有深浅不一的重点色，搭配蓬松的大围脖和丰厚尾毛，颜值极高。")
st.write("性格温顺黏人，叫声轻柔软糯，待人友善亲人，被抱起时身体会放松绵软，像柔软的布偶一般，因此得名。")

# 图片
st.image("resources/cat.png", width=1000)

# 音频


# 视频


# logo
st.logo("resources/cat.png")

# 表格
# 表格
data_list = {
    "姓名": ["奶糖", "年糕", "泡芙", "布丁", "元宵"],
    "年龄": [2, 1, 3, 0.5, 4],
    "品种": ["布偶猫", "英短银渐层", "美短虎斑", "曼基康矮脚", "暹罗猫"]
}
st.table(data_list)

# 输入框
name = st.text_input("请输入姓名：")
st.write(f"姓名：{name}")

password = st.text_input("请输入密码：", type="password")
st.write(f"密码：{password}")

# 单选按钮
gender = st.radio("请输入性别：", ["M", "F", "未知"])
st.write(f"性别：{gender}")
