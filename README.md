# Medical Data Visualizer

https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

Explored the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices using the medical dataset.

visualized:
1. Counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with/without cardio.
2. correlation matrix using heatmap.

Data description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

DataFile name: medical_examination.csv

Feature	Variable Type	Variable	Value Type
1. Age	Objective Feature	age	int (days)
2. Height	Objective Feature	height	int (cm)
3. Weight	Objective Feature	weight	float (kg)
4. Gender	Objective Feature	gender	categorical code
5. Systolic blood pressure	Examination Feature	ap_hi	int
6. Diastolic blood pressure	Examination Feature	ap_lo	int
7. Cholesterol	Examination Feature	cholesterol	1: normal, 2: above normal, 3: well above normal
8. Glucose	Examination Feature	gluc	1: normal, 2: above normal, 3: well above normal
9. Smoking	Subjective Feature	smoke	binary
10. Alcohol intake	Subjective Feature	alco	binary
11. Physical activity	Subjective Feature	active	binary
12. Presence or absence of cardiovascular disease	Target Variable	cardio	binary
