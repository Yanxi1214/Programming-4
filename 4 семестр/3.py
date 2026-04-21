# main.py
# Клиентский код - демонстрация работы паттерна

from implementor import ConsoleSender, FileSender, EmailSender
from abstraction import NormalMessage, WarningMessage, ErrorMessage


def main():
    print("=" * 55)
    print("Демонстрация паттерна «Мост» (Bridge Pattern)")
    print("Система вывода сообщений")
    print("=" * 55 + "\n")

    # 1. Обычное сообщение в консоль
    print("--- Сценарий 1: Обычное сообщение в консоль ---")
    console_sender = ConsoleSender()
    normal_msg = NormalMessage("Система успешно запущена", console_sender)
    normal_msg.send()
    print()

    # 2. Предупреждение в файл
    print("--- Сценарий 2: Предупреждение в файл ---")
    file_sender = FileSender("warnings.log")
    warning_msg = WarningMessage("Свободное место на диске менее 10%", file_sender)
    warning_msg.send()
    print()

    # 3. Ошибка на email
    print("--- Сценарий 3: Ошибка на email ---")
    email_sender = EmailSender()
    error_msg = ErrorMessage("Не удалось подключиться к базе данных", email_sender)
    error_msg.send()
    print()

    # 4. Гибкость: одно и то же сообщение разными способами
    print("--- Сценарий 4: Гибкость (одно сообщение - разные способы) ---")
    error_text = "Таймаут соединения"
    
    error_to_console = ErrorMessage(error_text, ConsoleSender())
    error_to_console.send()
    
    error_to_file = ErrorMessage(error_text, FileSender("errors.log"))
    error_to_file.send()
    
    error_to_email = ErrorMessage(error_text, EmailSender())
    error_to_email.send()
    print()

    # 5. Демонстрация расширяемости (комментарий)
    print("--- Расширяемость ---")
    print("✅ Легко добавить новый тип сообщения (например, InfoMessage)")
    print("✅ Легко добавить новый способ отправки (например, TelegramSender)")
    print("✅ Не требуется изменять существующие классы")


if __name__ == "__main__":
    main()
