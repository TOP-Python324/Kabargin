# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имя n ничего не говорит о том, какое значение ассоциировано с данной переменной, а имена h и m слишком сокращены — вместо них стоило назвать переменные minutes, hour и minute
n = int(input())
# КОММЕНТАРИЙ: в дальнейшем у вас будут десятки и сотни переменных, поэтому, чтобы среди этого множества удобно ориентироваться необходимо сразу привыкать давать переменным значащие имена

# УДАЛИТЬ: данные переменные используются каждая только единожды — неоптимально
# КОММЕНТАРИЙ: если бы операции, выполняемые для вычисления значений этих переменных, были бы более сложными и длинными, то можно было оправдать создание отдельных переменных — в данном случае операции тривиальны и вполне могут быть прописаны и выполнены вместо использования данных переменных
h = n // 60
m = n % 60

print(f'{n} мин - это {h} час {m} минут.')


# 290
# 290 мин - это 4 час 50 минут.


# ИТОГ: хорошо, немного доработать — 2/3
