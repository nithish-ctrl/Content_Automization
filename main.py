from Script_generation import generate_script
from text_to_speech import text_to_speech
from subtitles_generation import subtitles_generation

if __name__ == "__main__":
    #topic = "Large Language Models"
    script = generate_script(topic = "Small Language Models")
    print(script)
    text_to_speech(script)
    subtitles_generation()
