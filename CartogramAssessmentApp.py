# Imports
import streamlit as st
import numpy as np
from PIL import Image
import time
import json
import Database as db
# import pymongo
# Importing Files
import QuizGiver as QG
import WelcomePage as Intro
import UserDetails as WP
import Feedback as FB
import ThankYouPage as Q


# Importing Files
# Imports

def app():
    # Session States
    if 'time_stamp' not in st.session_state:
        st.session_state['time_stamp'] = 0
    if 'QuizDoc' not in st.session_state:
        st.session_state['QuizDoc'] = 0
    if 'Answers' not in st.session_state:
        st.session_state['Answers'] = 0
    # if 'Key' not in st.session_state:
    #   st.session_state['Key'] = 0
    # st.session_state['Key'] = Key
    # End Session States

    # Global Variables
    st.session_state['QuizDoc'] = 'Questions.txt'
    Fin = st.empty()

    # Global Variables

    # Test Functions
    def clicked():
        st.write('Finished')
        # WriteAnswers = st.session_state['Answers']

    # Test Functions

    # Title Bar
    col1, col2 = st.columns([7, 3])
    col1.title("Cartogram Assessment")
    ph = col2.empty()
    # Title Bar

    if st.session_state['QuizDoc']:
        def Quizzer():
            (Ans, Index, NumberOfQuestions) = QG.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
            return Ans, Index, NumberOfQuestions

        (Ans, Index, NumberOfQuestions) = Quizzer()
        st.session_state['Answers'] = Ans
        # Columns Part 2
        Endcol1, Endcol2 = st.columns([6, 4])
        VanishEndcol2 = Endcol2.empty()

        # Columns Part 2

        def finish(str):
            Finish = VanishEndcol2.button(str, on_click=clicked)
            return Finish

        if Index == NumberOfQuestions:
            Finish = finish('Finish')
        else:
            Finish = False

    while Finish == False:
        mins, secs = divmod(st.session_state['time_stamp'], 60)
        ph.metric("Countdown", f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state['time_stamp'] += 1
    if Finish:
        VanishEndcol2.empty()
        Ans = st.session_state['Answers']
        #st.write(Ans)
        return Ans


if __name__ == '__main__':
    Proceed = Intro.app()
    Start = 0
    if Proceed:
        (PersonalInfo, Start) = WP.app()
    # st.write(Key)
    # st.write(Email)
    Finish = 0
    Ans = 0
    Flag = 0
    if Start:
        Ans = app()
    if Ans:
        feedback = FB.app()
    if feedback:
        print('Ready to append')
        Flag = db.app(PersonalInfo, Start, feedback)
    if Flag:
        Q.app()


