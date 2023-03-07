import re

def findPython(file):

    #reads file and assigns to value    
    text = file.read()

    # Separate lines in text
    line_lst = text.split('\n')
    # iterate over lines to find match
    for line in line_lst:
        py = re.findall("^Python.+", line)
        if len(py) > 0:
            print(*py)

    # lsit comprehension to find all numbers then convert to integer
    nums = [int(i) for i in re.findall("[0-9]+", text)] 
    # sum of numbers
    sum_nums = sum(nums) 
    # highest number
    highest_num = max(nums) 
    # vowel count
    num_vowels = len(re.findall("[aeiouAEIOU]", text)) 
    # 'Python' count
    num_python = len(re.findall("Python", text))
    
    print(f"\nThe sum of all the files is {sum_nums}\nThe highest number is {highest_num}\nThe total vowel count is {num_vowels}\nPython word count is {num_python}")
    
    file.close()

# opens the file
PyTxt = open('D:/Documents/files/1st year/SEM2/OUTPUTS/Computer Programming II/regex_sum_42.txt')
# calling the findPython function and passing the opened file as argument
findPython(PyTxt)

