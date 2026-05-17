from Script_generation import generate_script
from text_to_speech import text_to_speech


if __name__ == "__main__":
    #topic = "Large Language Models"
    script = generate_script(topic = "Large Language Models")
    print(script)
    text_to_speech(script)