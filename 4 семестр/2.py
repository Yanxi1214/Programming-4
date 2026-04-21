# abstraction.py
# Abstraction и RefinedAbstractions

from implementor import MessageSender


class Message:
    """
    Абстракция (Abstraction)
    Хранит ссылку на объект реализации (MessageSender)
    """
    def __init__(self, sender: MessageSender):
        self._sender = sender

    def send(self) -> None:
        """Базовый метод отправки (должен быть переопределён)"""
        pass


# RefinedAbstraction 1: Обычное сообщение
class NormalMessage(Message):
    def __init__(self, text: str, sender: MessageSender):
        super().__init__(sender)
        self._text = text

    def send(self) -> None:
        self._sender.send(f"Обычное: {self._text}")


# RefinedAbstraction 2: Предупреждение
class WarningMessage(Message):
    def __init__(self, text: str, sender: MessageSender):
        super().__init__(sender)
        self._text = text

    def send(self) -> None:
        self._sender.send(f"Предупреждение: {self._text}")


# RefinedAbstraction 3: Ошибка
class ErrorMessage(Message):
    def __init__(self, text: str, sender: MessageSender):
        super().__init__(sender)
        self._text = text

    def send(self) -> None:
        self._sender.send(f"Ошибка: {self._text}")
