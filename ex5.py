array = ["Georgii Ignatov 22", "Alexander Karavayev 11", "Matthew Verbitsky 20", "Robert Pattinson 19"]
array = sorted(array, key = lambda x: int(x[-2]))
answer = array[0]
for i in range(0, len(array) - 1):
  if array[i] < answer:
    answer = array[i]
print(answer)