immutable_var = tuple([22, 'movie', 47, 'file'])
print(immutable_var)
immutable_var = ([[22, 'movie'], 47, 'file'])
immutable_var[0][1] = 3
print(immutable_var)#Картежи являются неизменяемым типом данных, т.к. пайтон не поддерживает...
#внутренние изменения данных в картежах, исключения бывают(например, одно из них я привел выше)...
#однако, по моим рассужденям, это получается только путем создания списка внутри самого картежа...
#иначе изменить данные внутри него нельзя.
mutable_list = [1, 'two', 3, 'four']
mutable_list.append(5)
mutable_list.remove(1)
print(mutable_list)