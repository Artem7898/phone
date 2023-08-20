                      Как использовать приложение:
    1. Отображение существующих записей:
        ◦ При запуске программы откроется главное окно приложения.
        ◦ Существующие записи (если есть) будут отображаться в QTextEditвиджете.
    2. Добавление новых записей:
        ◦ Нажмите кнопку «Добавить новую запись».
        ◦ Появится диалоговое окно, в котором вас попросят ввести данные новой записи.
        ◦ Введите фамилию, имя, отчество, организацию, рабочий телефон и личный телефон для новой записи.
        ◦ Нажмите кнопку «Добавить» в диалоговом окне.
        ◦ Диалоговое окно закроется, и новая запись будет добавлена в список каталогов.
        ◦ Обновленный список записей будет отображаться в QTextEditвиджете.
    3. Выход из приложения:
        ◦ Выйти из приложения можно, закрыв главное окно.
                                    Важные заметки:
    • Приложение ориентировано на отображение существующих записей и добавление новых записей. Функции редактирования и 
      поиска в настоящее время не реализованы в этой версии.
    • Программа использует QDialog.Acceptedзначение, чтобы определить, была ли нажата кнопка «Добавить» в диалоговом 
      окне. 
      Если пользователь нажимает «Добавить», диалоговое окно принимается и добавляется новая запись. Если пользователь 
      отменяет диалог, изменения не сохраняются.
    • Это упрощенный пример для демонстрации пользовательского интерфейса. Вы можете расширить и усовершенствовать 
      приложение, добавив дополнительные функции, такие как редактирование, поиск и сохранение записей в файл.
    • pip install PyQt5 Перед запуском кода убедитесь, что у вас установлен PyQt5 ( ).
    • Чтобы запустить код, выполните его в среде Python, и откроется окно графического интерфейса для взаимодействия 
      с приложением
    ____________________________________________________________________________________________________________________

         Представлена простая реализация телефонного справочника с указанными функциями в Python 3. 
         Эта реализация использует текстовый файл для хранения записей справочника. Каждая запись хранится на отдельной 
         строке в формате: surname;first name;patronymic;organization;work phone;personal phone
