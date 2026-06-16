from piper import PiperVoice
import wave
import subprocess
import time
import modules.voice.state as state

voice = PiperVoice.load(
    "voices/en_US-amy-medium.onnx"
)

def speak(text):

    start = time.time()

    state.assistant_speaking = True

    try:

        print("[TTS] START")

        with wave.open(
            "/tmp/assistant.wav",
            "wb"
        ) as wav_file:

            generate_start = time.time()

            voice.synthesize_wav(
                text,
                wav_file
            )

            print(
                "GENERATE:",
                time.time() - generate_start
            )

        play_start = time.time()

        subprocess.run(
            ["aplay", "/tmp/assistant.wav"]
        )

        print(
            "PLAYBACK:",
            time.time() - play_start
        )

        print(
            "TTS TIME:",
            time.time() - start
        )

    finally:

        state.assistant_speaking = False
        state.just_finished_speaking = True

        print("[TTS] END")