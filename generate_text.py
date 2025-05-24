import google.generativeai as genai

API_KEY = "AIzaSyCNz0hQ7OE_I1FVz2IY8eSdNSo-rbg7OxU"
genai.configure(api_key=API_KEY)

def generate_text(prompt: str):
    model = genai.GenerativeModel.get("models/gemini-1.5-pro")
    session = genai.ChatSession(model=model)  # pass the model object here
    response = session.send_message(prompt)
    return response.text

if __name__ == "__main__":
    output = generate_text("Write a short explanation of how neural networks work.")
    print(output)
