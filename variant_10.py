import csv
import xml.etree.ElementTree as ET

with open("books.csv", encoding="cp1251", newline="") as file:
    books = list(csv.DictReader(file, delimiter=";"))


def year(book):
    return int(book["Дата поступления"].split()[0][-4:])

print("Задание 1")
print("Книг с названием длиннее 30 символов:", sum(len(book["Название"]) > 30 for book in books))

print("\n\nЗадание 2")
recent = [book for book in books if year(book) >= 2018]
author = input("Введите автора для поиска: ").casefold()
found = [book for book in recent if author in book["Автор"].casefold()] if author else []
print("Найденные книги от 2018 года:")
for book in found:
    print(f'{book["Автор"]}. {book["Название"]} - {year(book)}')
print("Найдено:", len(found))


# Задание 3
with open("bibliography_links.txt", "w", encoding="utf-8") as file:
    for number, book in enumerate(recent[:20], 1):
        file.write(f'{number}. {book["Автор"]}. {book["Название"]} - {year(book)}\n')


print("\n\nЗадание 4")
currency = {
    item.findtext("Name"): item.findtext("CharCode") for item in ET.parse("currency.xml").getroot()
}
print("Валюты (Name - CharCode):", currency)


print("\n\nДопЗадание 1")
tags = sorted({tag.strip() for book in books for tag in book["Жанр книги"].split("#") if tag.strip()})
print("Теги без повторений:")
print(*tags, sep="; ")


print("\n\nДопЗадание 2")
print("20 самых популярных книг:")
for book in sorted(books, key=lambda book: int(book["Кол-во выдач"]), reverse=True)[:100]:
    print(f'{book["Название"]} — {book["Кол-во выдач"]} выдач')



