# 1. Вначале, как обычно, импортируем в проект библиотеку Pandas:
import pandas as pd

# 2. Скачаем библиотеку Matplotlib через Python Packages — Install packages.
# 3. Импортируем библиотеку Matplotlib:
import matplotlib.pyplot as plt

# 4. Создадим простой словарь, из которого сделаем датафрейм:

data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

# 5. Создадим график, который поможет визуализировать данные из датафрейма.
# Для этого мы будем использовать библиотеку Matplotlib:

df['value'].hist()
plt.show()

df.boxplot(column='value')
plt.show()

# Удаление выброса
print(df.describe())

# определим первый (Q1) и третий (Q3) квартили, используя функцию
# quantile():
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)

# рассчитаем межквартальный размах (IQR), для этого пропишем:
IQR = Q3 - Q1

# На основе вычисленных значений определим нижнюю и верхнюю границы
# для определения выбросов. Пропишем переменные для границ:
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

# Таким образом мы найдём значения для верхней и нижней границы.
# А теперь необходимо удалить выбросы, которые не входят в очерченный
# диапазон. Создадим новый датафрейм:

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new.boxplot(column='value')
plt.show()