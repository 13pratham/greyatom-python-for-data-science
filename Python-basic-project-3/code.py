# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record = np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data, new_record), axis=0)

age = np.array([i[0] for i in census])

max_age = np.max(age)
min_age = np.min(age)

age_mean = np.mean(age)
age_std = np.std(age)

race_0 = np.array([i[2] for i in census if i[2]==0])
race_1 = np.array([i[2] for i in census if i[2]==1])
race_2 = np.array([i[2] for i in census if i[2]==2])
race_3 = np.array([i[2] for i in census if i[2]==3])
race_4 = np.array([i[2] for i in census if i[2]==4])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
minimum = min([len_0, len_1, len_2, len_3, len_4])

if (minimum == len_1):
    minority_race = 1
elif (minimum == len_2):
    minority_race = 2
elif (minimum == len_3):
    minority_race = 3
elif (minimum == len_4):
    minority_race = 4
else:
    minority_race = 0

senior_citizens = [i for i in census if i[0]>60]
senior_citizens_len = len(senior_citizens)
working_hours_sum = 0
for i in senior_citizens:
    working_hours_sum += i[6]

avg_working_hours = working_hours_sum/senior_citizens_len

print(avg_working_hours)

high = [i for i in census if i[1]>10]
low = [i for i in census if i[1]<=10]

sum = 0
for i in high:
    sum += i[7]
avg_pay_high = sum/len(high)

sum = 0
for i in low:
    sum += i[7]
avg_pay_low = sum/len(low)



