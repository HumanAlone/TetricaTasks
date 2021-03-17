import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('ru', extract_format=wikipediaapi.ExtractFormat.WIKI)

page_py = wiki_wiki.page('Категория:Животные_по_алфавиту')

letters = {}
for categorymember in page_py.categorymembers:  # Работает около 30 секунд
    if categorymember[0] == 'A':
        break
    if categorymember[0].isascii():
        continue
    letters[categorymember[0]] = letters.get(categorymember[0], 0) + 1

for letter, count in sorted(letters.items()):  # Да, Ё будет на первом месте
    print(f"{letter}: {count}")
