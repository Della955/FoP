def file_sum (textNumbers):

    with open(textNumbers, 'r') as infile:
        numbers = [float(line.strip()) for line in infile]
    
    total = sum(numbers)

    with open ('sum_answer.txt', 'w') as sum_file:
        sum_file.write(total)
