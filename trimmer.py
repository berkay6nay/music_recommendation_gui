import librosa
import numpy as np
import soundfile as sf
class Trimmer:
    """Class for getting the first 30 seconds of a signal"""
    @staticmethod
    def trim(y , sr):
        stft = np.abs(librosa.stft(y))
        mean_mag = np.mean(stft, axis=0)
        max_mag_index = np.argmax(mean_mag)
        segment_duration = 30  
        segment_start = max_mag_index * librosa.samples_to_time(samples = 1, sr = sr)
        segment_end = segment_start + segment_duration
        segment = y[int(librosa.time_to_samples(times = segment_start,sr = sr)):int(librosa.time_to_samples(times = segment_end, sr = sr))]
        return segment

     
        
    def save(y , sr):
        sf.write("segment.wav" , data=y ,samplerate=sr)