import sys # системная библиотека, позволяющая работать с аргументами командной строки

param_data_type = sys.argv[1] # тип данных
param_sort_mode = sys.argv[2] # режим сортировки
param_file_out = sys.argv[3] # выходной файл
param_file_in = sys.argv[4] # входной файл

# Главная функция, отвечающая за сортировку
def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    # так как параметр необязателен, то elif не прописываем
    if (param_sort_mode == '-a'):
        l = merge_sort(a[:n//2])
        r =  merge_sort(a[:n//2:n])

        i = j = 0
        res = []
        while i < len(l) or j < len(r):
            if not i < len(l):
                res.append(r[j])
                j += 1
            elif not j < len(r):
                res.append(l[i])
                i += 1
            elif l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1

        return res
    else:
        l = merge_sort(a[:n//2])
        r =  merge_sort(a[:n//2:n])

        i = j = 0
        res = []
        while i < len(l) or j < len(r):
            if not i < len(l):
                res.append(r[j])
                j += 1
            elif not j < len(r):
                res.append(l[i])
                i += 1
            elif l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1

        return res       

# Тело программы
if __name__ == '__main__':
    
    if (len(sys.argv) > 0): # если указаны аргументы
        # Открытие файлов для записи и чтения
        file_out = open(param_file_out, 'w')
        file_in = open(param_file_in, 'r')
        # Число
        if (param_data_type == '-i'):
            A = [] # Рабочий массив
            line = file_in.readline()
            while line:
                A.append(line),
                line = file_in.readline()
            print('Before:')
            for i in range(len(A)):
                print(A[i])
            A = merge_sort(A)
            print('After:')
            for i in range(len(A)):
                print(A[i])
                file_out.write(A[i])# Запись результата
        # Строка
        elif (param_data_type == '-s'):
            A = [] # Рабочий массив
            line = file_in.readline()
            while line:
                A.append(line),
                line = file_in.readline()
            print('Before:')
            for i in range(len(A)):
                print(A[i])
            A = merge_sort(A)
            print('After:')
            for i in range(len(A)):
                print(A[i])
                file_out.write(A[i])# Запись результата
        else:
            # Аварийное завершение программы и выход, если не указан тип данных
            print('Error! Tell me the type')
            sys.exit(1)
        # Окончание работы с файлами
        file_in.close()
        file_out.close()
    else:
        # Аварийное завершение программы и выход, если не указаны аргументы
        print('Error! No arguments provided')
        sys.exit(1)


    
    