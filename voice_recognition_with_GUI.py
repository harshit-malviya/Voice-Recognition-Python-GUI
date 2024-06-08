import streamlit as st
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please wait, adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=5)
        st.write("Listening...")
        audio = r.listen(source)
    try:
        st.write("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        st.header("User Said")
        # st.write(f"User said: {query}\n")
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio. Please try again.")
        return "None"
    except sr.RequestError:
        st.write("Could not request results from the speech recognition service; check your network connection.")
        return "None"
    except Exception as e:
        st.write(f"An error occurred: {e}")
        return "None"
    return query

def main():
    st.title("Speech Recognition App")
    st.write("Click the button below and speak into your microphone.")

    if st.button("Start Listening"):

        query = takeCommand().lower()
        if query != "None":
            st.write(query)
        else:
            st.write("No valid command recognized.")

if __name__ == "__main__":
    main()
