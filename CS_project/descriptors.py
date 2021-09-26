import logging

logger = logging.getLogger('server')


# Дескриптор для описания порта:
class Port:
    def __set__(self, instance, value=None):
        if value is None:
            logger.info(f'Не указан порт, задаю порт по умолчанию - 7777')
            value = 7777
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        elif type(value) != 'int':
            raise ValueError(f'Попытка инициализации порта с десятичным значением, допустимы только целочисленные!')
        # Если порт прошел проверку, добавляем его в список атрибутов экземпляра
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
