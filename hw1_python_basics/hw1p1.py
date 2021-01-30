#!/usr/bin/env python
import person
import numpy as np
import matplotlib.pyplot as plt


list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  
name_size = [len(x) for x in list_of_names]

people = {}

for x in range(len(list_of_names)):
  new_person = person.person(name=list_of_names[x], age=list_of_ages[x], height=list_of_heights_cm[x])
  people.update({list_of_names[x] : new_person})

print(people)

age_array = np.array(list_of_ages)
height_array = np.array(list_of_heights_cm)

avg_age = np.mean(age_array)
print(f"The average age is {avg_age}")

plt.scatter(list_of_ages, list_of_heights_cm, color='b')
plt.grid(True)
plt.xlabel('Age (yrs)')
plt.ylabel('Height (cm)')
plt.title('Height vs Age')
plt.savefig('plot.png')
plt.show()