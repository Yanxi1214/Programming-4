# implementor.py
# Implementor: интерфейс для отправки сообщений

class MessageSender:
    """
    Интерфейс реализации (Implementor)
    Определяет метод, который должны реализовать все конкретные отправители
    """
    def send(self, text: str) -> None:
        pass


# ConcreteImplementor 1: отправка в консоль
class ConsoleSender(MessageSender):
    def send(self, text: str) -> None:
        print(f"[Консоль] {text}")


# ConcreteImplementor 2: отправка в файл
class FileSender(MessageSender):
    def __init__(self, filename: str = "log.txt"):
        self.filename = filename

    def send(self, text: str) -> None:
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{text}\n")
        print(f"[Файл] Записано в {self.filename}")


# ConcreteImplementor 3: отправка на почту (условная)
class EmailSender(MessageSender):
    def send(self, text: str) -> None:
        # Здесь была бы реальная логика отправки email
        print(f"[Email] Отправлено: {text}")
