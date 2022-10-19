from datetime import datetime as dt

def logger(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a') as file:
        # file.write((f'\n{data, time}.')      # Вывод в лог в 1 строку.
        file.write((f'\n{data}, \n{time}.')    # Вывод в лог в 2 строки.
                        .format(data, time))