import numpy as np
import pandas as pd

name_helper = []
maths_helper =[]
eng_helper = []
soc_helper = []

print("Enter the number of entries youn want to include")
n = int(input())

count = 1
while(count<=n):
    print("Enter the name of the entry number", count)
    name_ele = input()
    name_helper.append(name_ele)

    print("Enter the grade for maths of", name_ele)
    maths_ele = int(input())
    maths_helper.append(maths_ele)

    print("Enter the grade for english of", name_ele)
    eng_ele = int(input())
    eng_helper.append(eng_ele)

    print("Enter the grade for social of", name_ele)
    soc_ele = int(input())
    soc_helper.append(soc_ele)

    count = count + 1

name = np.array(name_helper)
maths = np.array(maths_helper)
eng = np.array(eng_helper)
social = np.array(soc_helper)

data = np.zeros(n, dtype=([('Name', 'U10'), ('Maths', 'i4'), ('English', 'i4'), ('Social', 'i4')]))
data['Name'] = name_helper
data['Maths'] = maths_helper
data['English'] = eng_helper
data['Social'] = soc_helper

final_data = pd.DataFrame(data)
print(final_data)
