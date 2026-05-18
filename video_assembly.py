import subprocess
import os

def video_assembly():
    video_path = r"C:\Users\Nithish\Content_Automisation\videos\Minecraft Parkour 7 Minutes Free To Use Gameplay 4K _ 65.mp4"
    audio_path = r"C:\Users\Nithish\Content_Automisation\audio\output.wav"
    subtitle_path = r"C:\Users\Nithish\Content_Automisation\audio\subtitles.srt"

    output_path = r"C:\Users\Nithish\Content_Automisation\output\final_reel.mp4"

    print("\nChecking files...\n")
    print("Video Exists:", os.path.exists(video_path))
    print("Audio Exists:", os.path.exists(audio_path))
    print("Subtitle Exists:", os.path.exists(subtitle_path))
    print("\nGetting audio duration...\n")

    probe_command = [
        "ffprobe",
        "-v", "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        audio_path
        ]

    probe_result = subprocess.run(
        probe_command,
        capture_output=True,
        text=True
        )

    audio_duration = float(probe_result.stdout.strip())

    print(f"Audio Duration: {audio_duration:.2f} seconds")

    subtitle_path_ffmpeg = (
        subtitle_path
        .replace("\\", "/")
        .replace(":", "\\:")
        )
    print("\nGenerating final reel...\n")

    USE_SUBTITLES = False

    if USE_SUBTITLES:

        video_filter = (
            f"scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,"
            f"subtitles='{subtitle_path_ffmpeg}':"
            f"force_style='Alignment=10,Fontsize=20,"
            f"PrimaryColour=&HFFFFFF&,"
            f"OutlineColour=&H000000&,"
            f"BorderStyle=1,"
            f"Outline=2,"
            f"Shadow=1'"
    )

    else:

        video_filter = (
            "scale=1080:1920:force_original_aspect_ratio=increase,"
            "crop=1080:1920"
    )

    ffmpeg_command = [
        "ffmpeg",
        "-y",

    # LOOP VIDEO IF TOO SHORT
        "-stream_loop", "-1",

    # VIDEO INPUT
        "-i", video_path,

    # AUDIO INPUT
        "-i", audio_path,

    # USE ONLY VIDEO FROM INPUT 0
        "-map", "0:v:0",

    # USE ONLY AUDIO FROM INPUT 1
        "-map", "1:a:0",

    # MATCH VIDEO LENGTH TO AUDIO
        "-t", str(audio_duration),

    # SCALE FOR REELS / SHORTS
       "-vf",
        video_filter,

    # VIDEO ENCODER
        "-c:v", "libx264",

    # AUDIO ENCODER
        "-c:a", "aac",

    # AUDIO SETTINGS
        "-ar", "44100",
        "-ac", "2",
        "-b:a", "192k",

    # GOOD QUALITY + FASTER EXPORT
        "-preset", "fast",
        "-crf", "23",

    # STOP WHEN AUDIO ENDS
        "-shortest",

        output_path
    ]

    result = subprocess.run(ffmpeg_command)
    if result.returncode == 0:
        print("\nFinal reel generated successfully!")
        print(f"\nSaved at:\n{output_path}")

    else:
        print("\nFFmpeg failed!")