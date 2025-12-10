from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Phone:
    brand: str
    model: str
    price: float
    color: str
    storage_gb: int
    is_in_stock: bool

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if discount_percent < 0:
            raise ValueError("Discount percent cannot be negative.")
        self.price -= self.price * (discount_percent / 100)

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        status = self.check_availability()
        return (
            f"{self.get_full_name()} | Цвет: {self.color} | "
            f"Память: {self.storage_gb}GB | Цена: ${self.price:,.2f} | {status}"
        )


def demo() -> None:
    iphone = Phone("Apple", "iPhone 15", 1199.0, "черный", 256, True)
    pixel = Phone("Google", "Pixel 8", 899.0, "серебристый", 128, False)
    galaxy = Phone("Samsung", "Galaxy S24", 1099.0, "серый", 512, True)
    xiaomi = Phone("Xiaomi", "13T Pro", 749.0, "синий", 256, True)

    phones = [iphone, pixel, galaxy, xiaomi]

    print("Полные названия:")
    for phone in phones:
        print(f"- {phone.get_full_name()}")

    print("\nСкидка 10% на все модели:")
    for phone in phones:
        phone.apply_discount(10)
        print(f"- {phone}")

    print("\nПроверка наличия:")
    for phone in phones:
        print(f"- {phone.get_full_name()}: {phone.check_availability()}")


if __name__ == "__main__":
    demo()

