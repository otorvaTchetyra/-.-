#Задание "Средний бал". Задача 1 - упорядочить элементы в классе students. Задача 2 - Вычислить среднию оценку каждого учентка. Задача 3 (дополнительно) - составить дневник с именами студентов с их оценками, а также среднию успеваемость учащихся

#создаю list
grades = [[5, 4, 5, 4], [4, 5, 5, 5], [3, 5, 4, 3], [3, 3, 3, 4], [5, 5, 5, 5]]
#создаю set
students = {'David', 'Alan', 'Betty', 'Esmeralda', 'Curtis'}

#меняем множество на список, чтобы добавились индексы и упорядочить порядок элементов

new_students = sorted(students) #с помощью функции sorted, расставляем элементы по возрастанию в алфавитном порядке элементы и переобразовываем в список
print(type(new_students)) #проверяем тип данных. Получили list

#далее складываем среднее значение всех оценок
average_of_grades = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])

#присваиваем каждому ученику его оценки
for index, (number, extra, average) in enumerate(zip(new_students, grades, average_of_grades)) : 
    print(f"{index} : {number}, {extra}, {average}") # на выходе получается, что-то вроде дневника
    


