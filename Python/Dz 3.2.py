
def correct_sentence(text):
    text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text

text = str(input(": "))

corrected_text = correct_sentence(text)
print(corrected_text)




