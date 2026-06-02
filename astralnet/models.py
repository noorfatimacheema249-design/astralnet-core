import numpy as np
import pandas as pd

class AdvancedAstralModel:
    def __init__(self):
        # Peer-reviewed baseline validation logs (Ntaios et al., 2012)
        self.intercept = -4.95
        self.coefficient = 0.245

    def predict_cohort_risk(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Ingests high-volume clinical registries and runs vectorized ASTRAL calculations.
        Expects keys: 'age', 'nihss', 'onset_delay_hrs', 'visual_defect', 'glucose_mmol', 'impaired_loc'
        """
        df = dataframe.copy()
        
        # Vectorized Point Computations (Blazing fast array processing)
        age_points = df['age'] // 5
        nihss_points = df['nihss']
        time_points = np.where(df['onset_delay_hrs'] > 3.0, 2, 0)
        visual_points = np.where(df['visual_defect'] == True, 2, 0)
        glucose_points = np.where((df['glucose_mmol'] > 7.3) | (df['glucose_mmol'] < 3.7), 1, 0)
        loc_points = np.where(df['impaired_loc'] == True, 3, 0)
        
        total_score = age_points + nihss_points + time_points + visual_points + glucose_points + loc_points
        
        # Logistic regression log-odds transformation
        logits = self.intercept + (self.coefficient * total_score)
        probabilities = 1 / (1 + np.exp(-logits))
        
        df['astral_score'] = total_score.astype(int)
        df['poor_outcome_probability_pct'] = np.round(probabilities * 100, 2)
        
        return df
