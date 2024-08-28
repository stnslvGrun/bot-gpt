Бот @contextq24_bot
Точка входа index.py
Файл wiki.py - извлечение статей
Файл var.py набор переменных

Как запустить
- Установить виртуальное окружение
- Установить requirements.txt
- Определить переменные var.py ( по необходимости )
- Запустить index.py

index.py ( Список функций )
- keyboard(message)  - определяет кнопку help 
- cmd_start(message) - стартует бота, добавляет кнопку help
- termlist(message)  - выводит лист кастомных терминов wiki
- help(message)      - выводит список команд
- reset(message)     - сбрасывает историю бота, глобальнуюб переменную MESSAGE_BOT
- message_answer(message) - функция ответа бота
- asyncio.run(main())- стартует поллинг 
