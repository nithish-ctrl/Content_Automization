from faster_whisper import WhisperModel

def subtitles_generation():
    model = WhisperModel(
        "base",
        device="cuda",
        compute_type="float16"
    )

    segments, info = model.transcribe(
        r"C:\Users\Nithish\Content_Automisation\audio\output.wav",
        beam_size=5
    )

    def format_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)

        return (
            f"{hours:02}:{minutes:02}:"
            f"{secs:02},{millis:03}"
        )

    with open(
        r"C:\Users\Nithish\Content_Automisation\audio\subtitles.srt",
        "w",
        encoding="utf-8"
    ) as f:

        for i, segment in enumerate(segments, start=1):

            f.write(f"{i}\n")

            f.write(
             f"{format_time(segment.start)} --> "
                f"{format_time(segment.end)}\n"
            )

            f.write(segment.text.strip() + "\n\n")

    print("SRT generated successfully!")