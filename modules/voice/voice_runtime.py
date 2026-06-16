import asyncio
import tempfile
import wave
import audioop
import sounddevice as sd

from faster_whisper import WhisperModel

from core.event_bus import emit
import modules.voice.state as state
import time
VOICE_THRESHOLD = 9000
print("[Voice] Loading Whisper Base...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("[Voice] Whisper Loaded")


running = True
audio_stream = None


async def real_voice_listener():

    global audio_stream

    loop = asyncio.get_running_loop()

    audio_stream = sd.RawInputStream(
        samplerate=16000,
        blocksize=16000,
        dtype="int16",
        channels=1
    )

    audio_stream.start()

    print("\n[Voice] Listening...\n")

    audio_buffer = b""
    last_voice_time = time.time()

    try:

        while running:

            if state.assistant_speaking:
                print("[VOICE] MUTED")
                await asyncio.sleep(0.1)
                continue
            if state.just_finished_speaking:

                await asyncio.sleep(1.0)

                state.just_finished_speaking = False
                
                continue
            data, _ = await loop.run_in_executor(
                None,
                audio_stream.read,
                3200
            )

            chunk = bytes(data)

            volume = audioop.rms(chunk, 2)

            print(f"VOL: {volume}")

            if volume > VOICE_THRESHOLD:
                print("SPEECH")

                last_voice_time = time.time()

            audio_buffer += chunk

            if (
                len(audio_buffer) > 0
                and
                time.time() - last_voice_time > 1.5
            ):

                with tempfile.NamedTemporaryFile(
                    suffix=".wav",
                    delete=False
                ) as tmp:

                    wav_path = tmp.name

                with wave.open(wav_path, "wb") as wf:

                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(16000)

                    wf.writeframes(audio_buffer)
                print(
                    f"BUFFER SIZE: {len(audio_buffer)}"
                )

                segments, info = model.transcribe(
                    wav_path,
                    language="en"
                )

                text = " ".join(
                    segment.text.strip()
                    for segment in segments
                ).strip()

                text = text.strip()

                if not text:
                    audio_buffer = b""
                    continue
                # Ignore dots/noise
                if "." in text and len(text) < 10:
                    audio_buffer = b""
                    continue
                # Ignore very short noise
                if len(text.split()) < 2:
                    audio_buffer = b""
                    continue
                print(f"\n[Voice Heard] {text}\n")
                await emit(
                    "voice_input",
                    {
                        "text": text
                    }
                )
                audio_buffer = b""

    finally:

        if audio_stream:

            audio_stream.stop()
            audio_stream.close()

            print(
                "\n[Voice] Audio stream closed.\n"
            )


def stop_voice_listener():

    global running

    running = False