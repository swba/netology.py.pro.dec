# Домашнее задание по теме «Decorators»

[Условие задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/3.Decorators)

Модули `task1.py` &mdash; `task3.py` содержат решения задач 
1 &mdash; 3.

В модуле `utils.py` находится пара вспомогательных функций, в том
числе функция `log_func_call(path, func, *args, **kwargs)`,
которая непосредственно записывает результат вызова функции в лог.

В третьем задании декоратор-логгер применяется к функции, которая
возвращает плоский список, используя генератор из предыдущего 
[задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/2.Iterators.Generators.Yield).