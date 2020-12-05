with open('day_3-input.txt') as garden:
  garden = list(garden)
  newgarden = []
  for row in garden:
    if isinstance(row,str):
      row = row.strip()
    newgarden.append(list(row))
  garden = newgarden

del garden[0]

unitmove = 3
count = 0
# rowcount = 0

for row in garden:
  if unitmove < len(row):
    if row[unitmove] == "#":
      row[unitmove] = "X"
      count += 1
    elif row[unitmove] == ".":
      row[unitmove] = "0"
    unitmove += 3
  # if unitmove >= len(row):
  #   unitmove = 0
  #   if row[unitmove] == "#":
  #     row[unitmove] = "X"
  #   elif row[unitmove] == ".":
  #     row[unitmove] = "0"
  print(row)

print(count)
