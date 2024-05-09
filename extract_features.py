import numpy as np
import librosa

class FeatureExtractor:

    @staticmethod
    def extract_features(audio_path):
        y, sr = librosa.load(audio_path)
        
        
        zcr = librosa.feature.zero_crossing_rate(y = y )
        mfccs = librosa.feature.mfcc(y = y, sr=sr)
        rms = librosa.feature.rms(y = y)
        spectral_centroid = librosa.feature.spectral_centroid(y = y , sr=sr)
        roll_of = librosa.feature.spectral_rolloff(y = y , sr = sr)
        

        output_list = []
        rms_mean = rms.mean()
        rms_var = rms.var()
        
        output_list.append(rms_mean)
        output_list.append(rms_var)
        
        spectral_centroid_mean = np.mean(spectral_centroid)
        spectral_centroid_var = np.var(spectral_centroid)
        
        output_list.append(spectral_centroid_mean)
        output_list.append(spectral_centroid_var)
        
        roll_of_mean = roll_of.mean()
        roll_of_var = roll_of.var()

        output_list.append(roll_of_mean)
        output_list.append(roll_of_var)

        zcr_mean = zcr.mean()
        zcr_var = zcr.var()
        
        output_list.append(zcr_mean)
        output_list.append(zcr_var)
        
        
        #tempo, _ = librosa.beat.beat_track(y = y, sr = sr)
        #output_list.append(tempo)

        mfccs = librosa.feature.mfcc(y = y, sr=sr)

        for row in mfccs:
        
            mean = np.mean(row)
            variance = np.var(row)
            
            output_list.append(mean)
            output_list.append(variance)
            
        return output_list



