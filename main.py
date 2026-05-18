from Script_generation import generate_script
from text_to_speech import text_to_speech
from subtitles_generation import subtitles_generation
from video_assembly import video_assembly
from video_uploading import video_uploading

video_path = r"C:\Users\Nithish\Content_Automisation\videos\Minecraft Parkour 7 Minutes Free To Use Gameplay 4K _ 65.mp4"
audio_path = r"C:\Users\Nithish\Content_Automisation\audio\output.wav"
subtitle_path = r"C:\Users\Nithish\Content_Automisation\audio\subtitles.srt"
output_video_path = r"C:\Users\Nithish\Content_Automisation\output\final_reel.mp4"
user_data_dir = r"C:\Users\Nithish\Content_Automisation\insta_session"

if __name__ == "__main__":
    topic = "Artificial Intelligence"
    script = generate_script(topic = topic)
    print(script)
    text_to_speech(script)
    subtitles_generation()
    video_assembly()
    video_uploading(topic, output_video_path, user_data_dir)

