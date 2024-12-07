import streamlit as st
from model_handler import LocalLLM
from prompts import EDUCATIONAL_PROMPTS

def main():
    st.title("Simple Educational Assistant")
    
    # Initialize LLM
    llm = LocalLLM(device="npu")
    
    # Add grade selection
    grade = st.selectbox(
        "Select Grade:",
        ["1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade",
         "6th Grade", "7th Grade", "8th Grade", "9th Grade", "10th Grade"]
    )
    
    # Rest of the selections
    subject = st.selectbox(
        "Choose Subject:",
        ["Mathematics", "Science", "Language"]
    )
    
    mode = st.radio(
        "Choose Mode:",
        ["Learn Concept", "Practice Questions", "Get Explanation"]
    )
    
    user_input = st.text_area("Enter your question or topic:")
    
    if st.button("Generate"):
        prompt = EDUCATIONAL_PROMPTS[mode].format(
            subject=subject,
            topic=user_input,
            grade=grade
        )
        
        # Remove subject parameter as it's not defined in the generate method
        response = llm.generate(prompt)
        st.write(response)

if __name__ == "__main__":
    main()
