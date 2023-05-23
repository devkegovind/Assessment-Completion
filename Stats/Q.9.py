"""Q-9.  Given  the  score  of  students  in  multiple  exams
'Karan': [85, 90, 92],
'Deepa': [70, 80, 85],
'Karthik': [90, 85, 88],
'Chandan': [75, 70, 75],
'Jeevan': [95, 92, 96]
Test  the  hypothesis  that  the  mean  scores  of  all  the  students  are  the  same.  If  not,  name  the 
student  with  the  highest  score.   
"""

import numpy as np
import scipy.stats as stats

# Create a dictionary with student names as keys and their exam scores as values
student_scores = {
    'Karan': [85, 90, 92],
    'Deepa': [70, 80, 85],
    'Karthik': [90, 85, 88],
    'Chandan': [75, 70, 75],
    'Jeevan': [95, 92, 96]
}

"""
Mean scores:
Karan: (85 + 90 + 92) / 3 = 89
Deepa: (70 + 80 + 85) / 3 = 78.33
Karthik: (90 + 85 + 88) / 3 = 87.67
Chandan: (75 + 70 + 75) / 3 = 73.33
Jeevan: (95 + 92 + 96) / 3 = 94.33

"""

# Extract the scores from the dictionary and convert them to a NumPy array
scores = np.array(list(student_scores.values()))

# Perform one-way ANOVA
f_value, p_value = stats.f_oneway(*scores)

# Print the F-value and p-value
print("F-value:", f_value)
print("p-value:", p_value)


alpha = 0.05  # Set the significance level

if p_value < alpha:
    print("Reject null hypothesis - There is a significant difference in mean scores among the groups.")
    # Find the student with the highest score
    highest_score_student = max(student_scores, key=lambda x: sum(student_scores[x]))
    print("Student with the highest score:", highest_score_student)
else:
    print("Fail to reject null hypothesis - There is no significant difference in mean scores among the groups.")