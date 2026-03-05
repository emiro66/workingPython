
# # Сюды
# def popopo(asd):
#     def ioioio():
#         print('выводиться перед вызовом функции')
#         asd()
#         print('выводиться после вызова функции')
        
#     return ioioio

# # Собака переводит отсюдова
# @popopo()
# def lololo():
#     print('some_func_1')

# lololo()



def hello_decorator(n):
    def actual_decorator(func):
        def wrapper():
            for i in range(n+1):
                # range(3) = [0,1,2]
                # range(3+1) = [0,1,2,3]
                # Ит. 1. i = 0 print('выводиться перед вызовом функции')
                # Ит. 2. i = 1 print('выводиться перед вызовом функции')
                # Ит. 3. i = 2 print('выводиться перед вызовом функции')
                # Ит. 4. i = 3 print('выводиться перед вызовом функции')
                print(i, 'выводиться перед вызовом функции')
            result = func()  # вызов оригинальной функции
            return result
        return wrapper
    return actual_decorator


@hello_decorator(3)
def some_func_3(): # Вот это вот оригинальная функция
    print('some_func_3')

some_func_3()

