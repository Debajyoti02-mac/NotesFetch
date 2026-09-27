def save_file(content , filename:str):
    with open(file=filename ,mode='w') as file:
        file.write(content)
    return f' done saving : {filename}'