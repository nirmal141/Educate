import streamlit as st
from model_handler import LocalLLM
from prompts import EDUCATIONAL_PROMPTS

def main():
    st.title("Simple Educational Assistant")
    
    # Initialize LLM
    llm = LocalLLM(device="npu")
    
    # Simple subject selection
    subject = st.selectbox(
        "Choose Subject:",
        ["Mathematics", "Science", "Language"]
    )
    
    # Mode selection
    mode = st.radio(
        "Choose Mode:",
        ["Learn Concept", "Practice Questions", "Get Explanation"]
    )
    
    # User input
    user_input = st.text_area("Enter your question or topic:")
    
    if st.button("Generate"):
        prompt = EDUCATIONAL_PROMPTS[mode].format(
            subject=subject,
            topic=user_input
        )
        
        response = llm.generate(prompt)
        st.write(response)

if __name__ == "__main__":
    main()
