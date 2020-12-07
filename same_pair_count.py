def same_pair_counter(data):
    counter = 0
    prev = ''
    for i in data:
        if i == prev:
            counter = counter + 1
        prev = i
    print(f'{data}\tsame pair count: {counter}')
    return counter


if __name__ == '__main__':
    numbers = ['11', '00', '01', '111', '101', '11001']
    # numbers = ['11001']
    outputFile = open("output_question_2", "w")

    for num in numbers:
        freq = same_pair_counter(num)
        outputFile.write(f'{num}\t{freq}\n')

    outputFile.close()
