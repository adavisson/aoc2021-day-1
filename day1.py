
file_name = "day1-inputs.txt"
with open(file_name) as f:
  lines = f.readlines()

increased_depth_count = 0

i = 0
while i < len(lines):
  if i > 0:
    if int(lines[i].strip()) > int(lines[i-1].strip()):
      increased_depth_count += 1
  i += 1

print(increased_depth_count)
