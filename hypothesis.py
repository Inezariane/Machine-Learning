import numpy as np 
from scipy import stats

before_treatment = np.array([120,122,118,130,125,128,115,121,123,119])
after_treatment = np.array([115,120,112,128,122,125,110,117,119,114])

null_hypothesis = 'The new drug has no effect on blood pressure'
alternate_hypothesis = 'The new drug has an effect on blood pressure'

t_statistic, p_value = stats.ttest_rel(after_treatment, before_treatment)

m = np.mean (after_treatment - before_treatment)
s = np.std (after_treatment - before_treatment, ddof=1)
n = len(before_treatment)
t_statistic_manual = m / (s / np.sqrt(n))

if p_value <=0.05:
    conclusion = 'Reject the null hypothesis'
else:
    conclusion = 'Fail to reject the null hypothesis'

print(f'T-statistic: (from scipy is {t_statistic:.4f}) vs (manual calculation is {t_statistic_manual:.4f})')
print(f'P-value: {p_value:.4f}')
print(f'Conclusion: {conclusion}')