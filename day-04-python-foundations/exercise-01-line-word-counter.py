# Question 1 - Line & Word Counter

with open("diary.txt", "w") as f:
    f.write("Today I practiced file handling in Python.\n")
    f.write("It was easier than I expected.\n")
    f.write("Tomorrow: error handling and logging.\n")

def line_word_counter(path):
    with open(path, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return (num_lines, num_words)


print(line_word_counter("diary.txt"))