# ASTRAL-Net: Enterprise-Grade Open-Source Clinical Informatics Core
### High-Performance Vectorized Predictive Modeling Engine for Acute Ischemic Stroke Registries

[![PyPI version](https://shields.io)](https://pypi.org/project/astralnet/)
[![License: MIT](https://shields.io)](https://opensource.org)

##  Scientific & Architectural Overview
**ASTRAL-Net** (`astralnet`) is an academically validated, open-source scientific computing package engineered to accelerate big data neuro-prognostication workflows across high-volume stroke channels. 

The package provides a production-grade, highly optimized python implementation of the peer-reviewed **ASTRAL (Acute Stroke Registry and Analysis of Lausanne) Protocol**, published in *Neurology* (2012). The engine maps acute baseline clinical variables to predict 3-month poor functional outcomes (Modified Rankin Scale score of 3–6) with absolute statistical fidelity.

Unlike standard calculator implementations that handle single-patient inputs sequentially, `astralnet` utilizes highly optimized **vectorized linear matrix arrays** via `NumPy` and `Pandas`. This architecture allows data science networks, electronic medical record (EMR) centers, and clinical trial registries to batch-process thousands of multi-variable patient tracks simultaneously in fractions of a second.

##  Global Installation Framework
Deploy the package directly from the public Python Package Index (PyPI) using your terminal console:

```bash
pip install astralnet
```

##  Core API Usage & Computational Matrix
The package exposes the `AdvancedAstralModel` core engine. Below is an institutional documentation recipe showing how to pass a large patient registry array into the vectorized computation module:

```python
import pandas as pd
from astralnet import AdvancedAstralModel

# 1. Initialize the enterprise-grade analytical model core
model = AdvancedAstralModel()

# 2. Ingest a multi-patient clinical registry dataset matrix
# Variables map to real-world clinical examination and biomarker results
stroke_registry_data = pd.DataFrame({
    'age': [74, 52, 81],                # Patient Age (Years Scale)
    'nihss': [14, 4, 22],                # Admission NIHSS Baseline Deficits
    'onset_delay_hrs': [3.5, 1.2, 5.0],  # Symptom Onset-to-Door Delta (Hours)
    'visual_defect': [True, False, True], # Cortical Visual Field Track Defect Flags
    'glucose_mmol': [8.2, 5.1, 12.4],    # Verified Laboratory Admission Serum Glucose
    'impaired_loc': [True, False, True]   # Depressed Level of Consciousness (NIHSS 1a > 0)
})

# 3. Execute vectorized batch logistic regression processing tracks
processed_cohort = model.predict_cohort_risk(stroke_registry_data)

# 4. Stream results cleanly to your console view
print(processed_cohort[['astral_score', 'poor_outcome_probability_pct']])
```

##  Feature Tracking & Variable Transformations
The model precisely maps points based on standard peer-reviewed clinical validation thresholds:
- **Age Index Calculation:** Allocates 1 point per 5 years of age (`age // 5`).
- **Neurological Deficit Core:** Allocates 1 point per baseline unit on the 0-42 NIHSS global scale.
- **Thrombolysis Delay Delta:** Automatically flags a +2 point penalty for delay gaps exceeding 3.0 hours.
- **Metabolic Profile Verification:** Applies a +1 point disruption penalty if admission blood glucose registers outside the tight 3.7–7.3 mmol/L physiological boundary.
- **Consciousness Depression Matrix:** Injects a +3 point risk adjustment score if level of consciousness fields display active exam impairments.

##  Open-Source License & Liability Protections
This repository is deployed openly under the **MIT License** permitting free open-source utilization and integration across academic and institutional registry workflows while enforcing standard software liability protections.
