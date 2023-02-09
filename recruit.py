# -*- coding: utf-8 -*-
import openai
import streamlit as st

openai.api_key = "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"

st.set_page_config(page_title="GPT-3 Resume Generator", page_icon=":pencil:", layout="wide")


def generate_resume(personal_info, work_description, summary_length, tone):
    prompt = (f"Generate a {tone} resume for someone with the following personal information and work description:\n\n"
              f"Personal Information: {personal_info}\n\n"
              f"Work Description: {work_description}")

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=summary_length,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def main():
    st.title("AI 求职信")

    personal_info = st.text_input("Enter your personal information (e.g. name, age, location, etc.):")
    work_description = st.text_area("Enter a description of your work experience:")
    summary_length = st.slider("Choose the length of the generated resume summary (in tokens):", 100, 500, 300)
    tone = st.selectbox("Choose the tone of the generated resume:", ["formal", "informal"])

    if st.button("Generate Resume"):
        resume = generate_resume(personal_info, work_description, summary_length, tone)
        st.success(resume)
        if st.button("Save Resume"):
            file_path = st.text_input("Enter a file name to save your resume:")
            with open(file_path, "w") as f:
                f.write(resume)
                st.success("Resume saved successfully!")


if __name__ == "__main__":
    main()
