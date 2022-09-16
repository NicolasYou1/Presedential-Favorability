import csv
import matplotlib.pyplot as plt

file = open("data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
data = []
for row in csvreader:
    data.append(row)
print(data)
file.close()

#creating poll names
poll_names = []
names = []

for i in range(len(data)):
  names.append([data[i][0]]) 
   
for i in range(len(names)):
  if names[i] not in poll_names:
    poll_names.append(names[i])

print(poll_names)
print()


#creating dictionary
polls_dict = {}

for i in range(len(poll_names)):
  polls_dict.update({poll_names[i][0]:[]})

print(polls_dict)
#adding values to the dictionary
values = data[i][1:]
for i in range(len(data)):
  for key in polls_dict:
    if data[i][0] == key:
      polls_dict[key].append(values)
print(polls_dict)
#putting dates in correct place

###change favorability ratings to integers
for key in polls_dict:
  for i in range(len(polls_dict[key])):
    polls_dict[key][i][-1] = int(polls_dict[key][i][-1])
    polls_dict[key][i][-2] = int(polls_dict[key][i][-2])
#rearanging numeric integers
for key in polls_dict:
  polls_dict[key].sort()
  holder = []
  for i in range(len(polls_dict[key])):
    if polls_dict[key][i][0][1].isnumeric():
      holder.append(polls_dict[key][i])
  for j in range(len(holder)):
    if holder[j] in polls_dict[key]:
      polls_dict[key].remove(holder[j])
  for h in range(len(holder)):
    polls_dict[key].append(holder[h])
print(polls_dict)


#putting into a graph
for key in polls_dict:

  plt.subplot(2, 1, 1)

  plt.title('Favorability')

  for i in range(len(polls_dict[key])):

    plt.bar(polls_dict[key][i][0],polls_dict[key][i][1],color='blue')

  plt.xticks(rotation=90)

  #plt.ylim(25,70)

  plt.grid()

  plt.ylabel('Percentage of Population')

  plt.subplot(2,1,2)

  plt.title('Unfavorability')

  for i in range(len(polls_dict[key])):

    plt.bar(polls_dict[key][i][0],polls_dict[key][i][2],color='red')

  plt.xticks(rotation=90)

  #plt.ylim(25,70)

  plt.grid()

  plt.ylabel('Percentage of Population')

  plt.suptitle(key)

  plt.show(block=False)

  plt.pause(5)

  plt.close()



