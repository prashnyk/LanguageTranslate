import streamlit as st
import openai
import prog1

# Set the model engine and your OpenAI API key.
model_engine = "gpt-3.5-turbo-instruct"
openai.api_key = prog1.My_Key

# Define function to handle the translation process.

def translation_process(content,target_lang):
    prompt = f"Translate '{content}' into {target_lang}"
    response = openai.completions.create(
        model=model_engine,
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract translated text from the response.
    translated = response.choices[0].text.strip()
    return translated

'''test_text = "How are you"
output = translation(test_text, "Hindi")
print(output)
'''
def main():
    st.sidebar.header("Language Translation")
    st.sidebar.write("This is language translation service. Enter the text to translate and target language")

    # Setting up the input values
    input_content = st.text_input("Enter the text for translation")
    target_languages = ['Arabic','English','Hindi','Kannada','German',]
    target_lang = st.selectbox("Select target language", target_languages)
    # Add button to start translation
    trans_button = st.button("Translate")
    # Add plac holder for output text
    output_text = st.empty()

    # Hit the button
    if trans_button:
        output_text.text("Translating....")
        output_text.text(translation_process(input_content,target_lang))

 # Driving code
if __name__ == "__main__":
    main()


