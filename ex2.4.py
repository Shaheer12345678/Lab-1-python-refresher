import timeit

def count_vowels(content):
    vowel_count=0
    word_count=0
    found_line = False
    for i in range(len(content)):
        line=content[i]

        if found_line or line=="CHAPTER 1. Loomings.":
            found_line = True
        else:
            continue

        words=line.split(" ")
        word_count+=len(words)
        for word in words:
            for c in word:
                if c == "a" or c == "A" or c == "e" or c == "E" or c == "o" or c == "O" or c == "i" or c == "I" or c == "i" or c == "y" or c == "Y" or c == "u" or c == "U":
                    vowel_count+=1
    return vowel_count/word_count


file= open("pg2701.txt",'r')
content=file.read().split('\n')

iterations = 100
total_time = timeit.timeit(lambda: count_vowels(content), number=iterations)
average_time = total_time/iterations

print(f'Average elapsed time: {average_time} seconds')


file.close()

