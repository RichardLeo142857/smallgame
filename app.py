import streamlit as st
import random
import time

st.set_page_config(page_title="Birthday Game", page_icon="🎂", layout="centered")

# 初始化关卡
if "level" not in st.session_state:
    st.session_state.level = 1

st.title("🎂 Happy Birthday 🎂")

# ------------------- 关卡 1 -------------------
if st.session_state.level == 1:
    st.header("关卡 1：吹蜡烛 🎂🕯️")
    if "candle_state" not in st.session_state:
        st.session_state.candle_state = 0

    if st.button("吹气！💨"):
        st.session_state.candle_state += 1

    if st.session_state.candle_state == 0:
        st.write("蜡烛安静地燃烧着 🔥")
    elif st.session_state.candle_state < 3:
        st.write("你越吹火越大了！🔥🔥")
    elif st.session_state.candle_state < 5:
        st.write("糟了！火势失控了！🔥🔥🔥🔥")
    else:
        st.error("💥 蛋糕爆炸了！不过... Happy Birthday!!!")
        if st.button("进入下一关 ➡️"):
            st.session_state.level = 2
            st.experimental_rerun()

# ------------------- 关卡 2 -------------------
elif st.session_state.level == 2:
    st.header("关卡 2：选礼物 🎁")

    wrong_gifts = ["📒 作业本", "📄 试卷", "📚 教科书", "📝 作业清单", "📊 模拟考卷"]
    correct_gift = "🎂 蛋糕！真正的礼物！"

    if "gift_revealed" not in st.session_state:
        st.session_state.gift_revealed = None

    cols = st.columns(3)
    gifts = wrong_gifts + [correct_gift]
    random.shuffle(gifts)

    for i, gift in enumerate(gifts):
        with cols[i % 3]:
            if st.button(f"礼物 {i+1}"):
                st.session_state.gift_revealed = gift

    if st.session_state.gift_revealed:
        if "蛋糕" in st.session_state.gift_revealed:
            st.success(f"你选到了 {st.session_state.gift_revealed} 🎉")
            if st.button("进入下一关 ➡️"):
                st.session_state.level = 3
                st.experimental_rerun()
        else:
            st.warning(f"糟糕！你选到了 {st.session_state.gift_revealed}")

# ------------------- 关卡 3 -------------------
elif st.session_state.level == 3:
    st.header("关卡 3：躲避作业大作战 📚")

    if "game_score" not in st.session_state:
        st.session_state.game_score = 0
        st.session_state.game_time = time.time()

    st.write("说明：点按钮来移动小人，躲开作业，吃到蛋糕加分 🍰")

    col1, col2, col3 = st.columns(3)
    if col1.button("⬅️ 左移"):
        st.session_state.game_score += random.choice([0, -1])
    if col2.button("站着不动"):
        st.session_state.game_score += random.choice([0, 1])
    if col3.button("➡️ 右移"):
        st.session_state.game_score += random.choice([0, -1, 1])

    elapsed = int(time.time() - st.session_state.game_time)
    st.write(f"⏱️ 已坚持 {elapsed} 秒")
    st.write(f"🎯 当前分数: {st.session_state.game_score}")

    if elapsed >= 15:
        st.success("你成功躲过了作业的袭击！🎉")
        if st.button("进入最后一关 ➡️"):
            st.session_state.level = 4
            st.experimental_rerun()

# ------------------- 关卡 4 -------------------
elif st.session_state.level == 4:
    st.header("关卡 4：蛋糕守护战 🎂⚔️")

    if "enemy_count" not in st.session_state:
        st.session_state.enemy_count = 0
        st.session_state.enemy_defeated = 0
        st.session_state.start_time = time.time()

    st.write("说明：点击出现的敌人把他们赶走！ 🖱️")

    if st.button("👩‍🏫 老师来抢蛋糕"):
        st.session_state.enemy_count += 1
        st.session_state.enemy_defeated += 1

    if st.button("📚 作业来抢蛋糕"):
        st.session_state.enemy_count += 1
        st.session_state.enemy_defeated += 1

    elapsed = int(time.time() - st.session_state.start_time)
    st.write(f"⏱️ 已坚持 {elapsed} 秒 | 🚫 敌人赶走 {st.session_state.enemy_defeated}")

    if elapsed >= 15:
        st.balloons()
        st.success("🎆 恭喜！你守住了蛋糕！ Happy Birthday! 🎂")
