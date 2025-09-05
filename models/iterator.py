from typing import Any

from models.category import Category


class Iterator:
    """Реализует итерацию товаров по категориям"""

    __category: Category

    def __init__(self, category: Category):
        self.__category = category
        self.current = 0

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> str:
        if self.current < len(self.__category.products_list):
            result = self.__category.products_list[self.current]
            self.current += 1
            return str(result)
        else:
            raise StopIteration
