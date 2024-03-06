import pandas as pd
from extract_features import FeatureExtractor
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("features_30_sec.csv")



class Recommender:
    @staticmethod
    def get_recommendations(song):
        user_features = FeatureExtractor.extract_features(song)
        feature_columns = ['rms_mean',
                            'rms_var', 'spectral_centroid_mean', 'spectral_centroid_var','rolloff_mean',
                            'rolloff_var', 'zero_crossing_rate_mean', 'zero_crossing_rate_var',
                            'harmony_mean', 'harmony_var', 'perceptr_mean', 'perceptr_var', 'tempo',
                            'mfcc1_mean', 'mfcc1_var', 'mfcc2_mean', 'mfcc2_var', 'mfcc3_mean',
                            'mfcc3_var', 'mfcc4_mean', 'mfcc4_var', 'mfcc5_mean', 'mfcc5_var',
                            'mfcc6_mean', 'mfcc6_var', 'mfcc7_mean', 'mfcc7_var', 'mfcc8_mean',
                            'mfcc8_var', 'mfcc9_mean', 'mfcc9_var', 'mfcc10_mean', 'mfcc10_var',
                            'mfcc11_mean', 'mfcc11_var', 'mfcc12_mean', 'mfcc12_var', 'mfcc13_mean',
                            'mfcc13_var', 'mfcc14_mean', 'mfcc14_var', 'mfcc15_mean', 'mfcc15_var',
                            'mfcc16_mean', 'mfcc16_var', 'mfcc17_mean', 'mfcc17_var', 'mfcc18_mean',
                            'mfcc18_var', 'mfcc19_mean', 'mfcc19_var', 'mfcc20_mean', 'mfcc20_var']
        
        data_features = data[feature_columns]
        scaler = StandardScaler()
        scaled_data_features = scaler.fit_transform(data_features)
        scaled_user_features = scaler.transform([user_features])
        similarity_scores = cosine_similarity(scaled_data_features, scaled_user_features)
        data['similarity'] = similarity_scores
        most_similar = data.sort_values(by='similarity', ascending=False).head(5)
        most_similar = most_similar["filename"].to_list()
        return most_similar