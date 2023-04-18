#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt

def switch_doors_experiment():
    # compute the correct door randomly
    correct_door = random.choice([1, 2, 3])
    # choose a door randomly
    door = random.choice([1, 2, 3])

    # Among two remaining door, get a random incorrect door
    doors = [1,2,3]
    try:
        doors.remove(door)
        doors.remove(correct_door)
    except:
        pass

    random_incorrect_door = random.choice(doors)

    # Remove the random incorrect door from the options available to you
    doors = [1, 2, 3]
    doors.remove(random_incorrect_door)

    # Now among your original choice of door and the new set of options,
    # switch your choice

    # Remove your original choice from the options
    doors.remove(door)
    # Now as only one option is there within
    final_choice = doors[0]

    # If the final choice is the correct door, then return 1, else return 0
    if final_choice == correct_door:
        return 1
    else:
        return 0

def probability_of_success_on_switch_door(precision):
    switch_door = 0
    # run the switch door experiment precision amount of times 
    # and increment the outcome in switch_door counter
    for i in range(precision):
      switch_door = switch_door + switch_doors_experiment()

    # Probability of success while switching doors = 
    #   num of times the experiment was successful / total number of runs
    return switch_door/precision

# Do 100 runs with precision 100000
runs = 100
total = 0
x = []
y = []
precision = 100000

for i in range(runs):
    total = total + probability_of_success_on_switch_door(precision)
    x.append(i+1)
    y.append(total/(i+1))

# Plot the probability vs runs on a matplotlib graph
plt.plot(x, y)

plt.xlabel('Runs')
plt.ylabel('Probability of Success while Switching')

plt.title('Monty Hall problem')

plt.ylim(0,1)
plt.xlim(1,runs)

plt.show()
print("Probability of Success on switching door for {} precision and {} runs is {}".format(precision, runs, total/runs))


# In[ ]:




