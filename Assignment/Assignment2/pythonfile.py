with open('input.txt','r') as file:
    a = file.read()

fileList = a.split("\n")
# print(fileList)

search_words = ['Python', 'C', 'OOP', "Hello", "Java"]

for search_words in search_words:
    # print(search_words)
    count = 0
    for file in fileList:
        if search_words == file:
            count += 1
        else:
            continue
    print(f"{search_words} -> {count}")