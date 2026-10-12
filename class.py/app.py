import random
import streamlit as st

st.title("🎮 Rock Paper Scissors Game")

# Session State initialize kar rahe hain taaki score browser reload par reset na ho
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "com_score" not in st.session_state:
    st.session_state.com_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Options mapping
choices = {1: "🪨 Rock", 2: "📄 Paper", 3: "✂️ Scissors"}

# Scoreboard Display
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Your Score", value=st.session_state.user_score)
with col2:
    st.metric(label="Computer Score", value=st.session_state.com_score)

st.write("---")

# Winner Check Function
def check_winner():
    if st.session_state.user_score == 5:
        st.balloons()
        st.success("🎉 Congratulations! You won the match!")
        st.session_state.game_over = True
    elif st.session_state.com_score == 5:
        st.error("😞 Sorry, Computer won the match!")
        st.session_state.game_over = True

# Game Logic Function
def play_round(user_choice):
    if st.session_state.game_over:
        return

    com_choice = random.randint(1, 3)
    st.info(f"You chose: **{choices[user_choice]}** | Computer chose: **{choices[com_choice]}**")

    if user_choice == com_choice:
        st.warning("It's a draw!")
    elif (
        (user_choice == 1 and com_choice == 3)
        or (user_choice == 2 and com_choice == 1)
        or (user_choice == 3 and com_choice == 2)
    ):
        st.success("You won this round!")
        st.session_state.user_score += 1
    else:
        st.error("Computer won this round!")
        st.session_state.com_score += 1

    check_winner()

# Game Control Buttons
if not st.session_state.game_over:
    st.subheader("Select your move:")
    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        if st.button("🪨 Rock"):
            play_round(1)
    with btn_col2:
        if st.button("📄 Paper"):
            play_round(2)
    with btn_col3:
        if st.button("✂️️ Scissors"):
            play_round(3)

# Reset Game Button
if st.button("🔄 Reset Game"):
    st.session_state.user_score = 0
    st.session_state.com_score = 0
    st.session_state.game_over = False
    st.rerun()