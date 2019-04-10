# Нормальные алгоритмы Маркова

### Постановка задачи
Программа эммулирует работу нормальных алгоритмов Маркова
### Use cases
GUI интерфейс создается при помощи Tkinter. При вводе некорректных данных или нажатии кнопок не в той последовательности ввыводится информация в диагностичекое окно, что пользователь делает не так.
### GUI интерфейс
![picture](https://github.com/maksim090897/Semester-project/blob/master/GUI.jpg)
---
### Описание виджетов:
  1. Метка <Название работы>
  2. Метка
  3. Тексовое поле для начального слова. (изменияемое поле)
  4. Метка
  5. Тексовое поле для выходного слова (поле не изменяется пользователем). При пошаговом проходе программы в это поле загружается стартовое слово и изменяется с каждым шагом программы
  6. Метка
  7. Текстовое поле (пока не предполагается его менять). Задан начальный алфавит **A = {a,b,c}**
  8. Метки
  9. Текстовое поле, в которое пользователь вводит правила. Считаем обычная стрелка отображается как **->**, терминальная отображается как **=>**
  10. Listbox, которым нельзя управлять пользователям. Форматированное отображение правил, все правила пронумерованы. Правило, которое выполняется на данный момент или которое было выполнено последним, подсвечивается на данный момент.
  11. Кнопка **Start** - запускает выполнение алгоритма и получаем конечное состояние в поле 5
  12. Кнопка **Step** - запускает пошаговое выполнение алгоритма, каждый шаг изменяет поле 5
  13. Кнопка **Stop** - останавливает выполнение алгоритма, если произошло зацикливание, выводит настоящее значение выходного слова в поле 5 и диагностическую информацию в поле 15
  14. Кнопка **Exit** - выход из программы (завершение работы)
  15. Текстовое поле для вывода диагностичекое информации о работе программы
