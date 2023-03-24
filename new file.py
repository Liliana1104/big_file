import pandas as pd
from pathlib import Path
import pathlib
import os


def main_function(column_name):
    """
    определить корневую директорию ,
    найти путь до папки с исходными файлами,
    создание пустой папки для выходных данных,
    парсим исходные данные,
    применяем multy_column к исходным данным,
    сохраняем модифицированные файлы в папку для выходных данных.

    """

    current_dir = Path.cwd()  # ТЕКУЩАЯ ДИРЕКТОРИЯ
    file = current_dir.joinpath('iinput_data')  # путь до папки с исходными файлами
    # for currentFile in file.iterdir():
    #     print(currentFile)
    od_path = current_dir.joinpath('ooutput_file') # путь до новой папки

    nf = current_dir.joinpath('Big_File.txt')
    if nf.is_file():
        os.remove(nf)  # удаление файлов олпредленного расширения
        print('УДАЛИЛИ СТАРЫЕ ФАЙЛЫ')

    if od_path.is_dir(): # проверка на существование  пути к новой папке
        for txt_path in od_path.glob("*.txt"):  # свертка по файлам определенного расширения
            os.remove(os.path.join(od_path, txt_path))  #удаление файлов олпредленного расширения
            print('УДАЛИЛИ СТАРЫЕ ФАЙЛЫ')
    else:
        od_path.mkdir()  #создать новую папку
        print('СОЗДАЛИ ПАПКУ')

    for txt_path in file.glob("*.txt"):
        df = pd.read_csv(txt_path, sep="\s+", header=0, index_col=False, engine='python', encoding='cp1251')  # header=0
        # print(df.columns[0])
        # print(df.columns[1:])
        c1=df.columns[0]
        # print(c1)

        c2=df.columns.to_list()
        print(c2)
        c3=c2[1:]
        # print(c3)
        c4 = c3.append(c1)
        # print(c3)
        df.columns=c3
        # print(df.columns)  # индексы колонок
        # print(df)

    # table = table.copy()
        column = df.loc[1:, column_name]
        column = column.astype(float) * (-1)
        df.loc[1:, column_name] = column # переприсовили

        k1 = df.columns[-1]
        # print(k1)

        k2 = df.columns.to_list()
        k3 = k2[:-1]
        # print(k3)
        k4 = k3.insert(0,k1)
        # print(k3)
        df.columns = k3
        # print(df.columns)

        name = txt_path.name
        new_file = od_path.joinpath(name)

        print(df.to_string())
        with open("Big_File.txt", "a") as f:
            f.write(df.to_string()+'\n')

        # file = open(new_file, 'r')
        # print(file)
        # with open(big_file, 'r+') as f:
        #     f.write(,delimiter='\n')
            # f.write('Thank you.\n')

        # with open('file.txt', 'r+') as f:
        #     # ...
        #     f.seek(0, 2)  # перемещение курсора в конец файла
        #     f.write('blabla')  # собственно, запись
        # logging.info("Создаю одноименные файла ")




if __name__ == '__main__':
    column_name = input('Введи название необходимого столбца : ')
    print(column_name)
    main_function(column_name)

# line1 = []
# line1.append("xyz ")
# line1.append("abc")
# line1.append("mno")
#
# file = open("File.txt", "w")
# for i in range(3):
#     file.write(line1[i])
#     file.write("\n")
# file = open("File.txt", "r")
# for line in file:
#     print(line)
# file.close()
