from Script_generation import generate_script
from text_to_speech import text_to_speech
from subtitles_generation import subtitles_generation
from video_assembly import video_assembly

if __name__ == "__main__":
    topic = "Artificial Intelligence"
    script = generate_script(topic = topic)
    print(script)
    text_to_speech(script)
    subtitles_generation()
    video_assembly()
