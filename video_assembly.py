import subprocess
import os

def video_assembly():

    # PATHS
    video_path = r"C:\Users\Nithish\Content_Automisation\videos\Fotnite.mp4"
    audio_path = r"C:\Users\Nithish\Content_Automisation\audio\output.wav"
    subtitle_path = r"C:\Users\Nithish\Content_Automisation\audio\subtitles.srt"

    output_path = r"C:\Users\Nithish\Content_Automisation\output\final_reel.mp4"

    # FILE TO STORE VIDEO OFFSET
    offset_file = r"C:\Users\Nithish\Content_Automisation\video_offset.txt"

    # CHECK FILES
    print("\nChecking files...\n")

    print("Video Exists:", os.path.exists(video_path))
    print("Audio Exists:", os.path.exists(audio_path))
    print("Subtitle Exists:", os.path.exists(subtitle_path))

    # GET AUDIO DURATION
    
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

    # LOAD PREVIOUS OFFSET
    
    if os.path.exists(offset_file):

        with open(offset_file, "r") as f:
            start_time = float(f.read().strip())

    else:
        start_time = 0

    print(f"\nStarting gameplay from: {start_time:.2f} seconds")

    # SAVE NEXT OFFSET
    next_offset = start_time + audio_duration

    with open(offset_file, "w") as f:
        f.write(str(next_offset))

    print(f"Next reel will start from: {next_offset:.2f} seconds")

    # FIX SUBTITLE PATH FOR FFMPEG
    subtitle_path_ffmpeg = (
        subtitle_path
        .replace("\\", "/")
        .replace(":", "\\:")
    )

  
    # SUBTITLE TOGGLE

    USE_SUBTITLES = False

    # VIDEO FILTERS
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

    # FFMPEG COMMAND

    print("\nGenerating final reel...\n")

    ffmpeg_command = [

        "ffmpeg",
        "-y",

        # START VIDEO FROM OFFSET
        "-ss", str(start_time),

        # LOOP VIDEO IF TOO SHORT
        "-stream_loop", "-1",

        # VIDEO INPUT
        "-i", video_path,

        # AUDIO INPUT
        "-i", audio_path,

        # USE VIDEO ONLY FROM GAMEPLAY
        "-map", "0:v:0",

        # USE AUDIO ONLY FROM GENERATED AUDIO
        "-map", "1:a:0",

        # MATCH OUTPUT LENGTH TO AUDIO
        "-t", str(audio_duration),

        # VIDEO FILTERS
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

        # QUALITY
        "-preset", "fast",
        "-crf", "23",

        # TIMESTAMP FIX
        "-avoid_negative_ts", "make_zero",

        # STOP WHEN AUDIO ENDS
        "-shortest",

        output_path
    ]

    # RUN FFMPEG
    result = subprocess.run(ffmpeg_command)

    if result.returncode == 0:

        print("\nFinal reel generated successfully!")
        print(f"\nSaved at:\n{output_path}")

    else:
        print("\nFFmpeg failed!")
