file_name = "day1-inputs.txt"

# Get formatted inputs from file
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]


# count how many times depth increased
def count_increase(values):
    increased_depth_count = 0

    i = 0
    while i < len(values):
        if i > 0:
            if values[i] > values[i-1]:
                increased_depth_count += 1
        i += 1
  
    return increased_depth_count


# get list of sums
def get_sums(values):
    sums = []

    i = 0
    while i < len(values)-1:
        if i > 0:
            sums.append(values[i-1] + values[i] + values[i+1]) 
        i += 1

    return sums


print("increased depth count: " + str(count_increase(get_formatted_inputs(file_name))))
print("increased depths of sums: " + str(count_increase(get_sums(get_formatted_inputs(file_name)))))

