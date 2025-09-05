class MixinLog:
    """
    класс-миксин, который при создании объекта, то есть при работе метода __init__,
    печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
    """

    name: str  # Наименование продукта
    description: str  # Описание продукта
    price: float  # Стоимость
    quantity: int  # Количество

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
