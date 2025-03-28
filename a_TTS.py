from TTS.api import TTS

# tts --list_models

tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
# tts = TTS(model_name="tts_models/de/css10/vits-neon", progress_bar=True, gpu=False)


tts.tts_to_file(text="Das dritte Semesster. Das dritte Semester.Das dritte Semesster.", file_path="a.mp3")

