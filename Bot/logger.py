def Read_DB(name: str, data: str):
    textList = []
    with open(f'2 course 1 semestr\\bot\\{data}\\{name}', 'r', encoding='UTF-8') as file:
        list = file.readlines()
        for line in list:
            textList.append(line)
        return textList
    
def Read_Photo(name: str, data: str):
    with open(f'2 course 1 semestr\\bot\\{data}\\img\\{name}') as file:
        return file
    


