import numpy as np, sounddevice as sd
from faster_whisper import WhisperModel

import os
os.environ["CT2_VERBOSE"] = "-1" # warning suppression

model = WhisperModel('small')
SAMPLERATE = 16000
CHUNKDURATION = .5 # seconds
SILENCEDURATION = 2.5 # seconds
THRESHOLD = .0015


def recordAudio(verbose: bool = False):
    # can make this stream but would reauire threading
    chunks = []
    silentChunks = 0
    recording = False

    if verbose: print('Listening...')
    while silentChunks < int(SILENCEDURATION / CHUNKDURATION):
        chunk = sd.rec(
            int(SAMPLERATE * CHUNKDURATION),
            samplerate=SAMPLERATE,
            channels=1,
            dtype='float32'
        )
        sd.wait()

        rms = np.sqrt(np.mean(chunk ** 2))
        if rms > THRESHOLD:
            if not recording:
                if verbose: print('Speech detected...')
                recording = True
            silentChunks = 0
            chunks.append(chunk)
        elif recording:
            chunks.append(chunk)
            recording = False
            silentChunks = 1
        else:
            silentChunks += 1
    if verbose: print('Speech ended.')

    return np.concatenate(chunks, axis=0).squeeze() if chunks else np.array([])


def transcribeAudio(audio: np.ndarray):
    segments, info = model.transcribe(audio)
    return ' '.join([seg.text for seg in segments]).replace('  ',' ').strip()

if __name__ == '__main__':

    print(transcribeAudio(recordAudio(verbose=True)))