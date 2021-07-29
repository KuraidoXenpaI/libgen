from libgen_api import LibgenSearch
import pprint
import requests
import os

os.chdir('D:\Cs\Python\libgen_api')

printer = pprint.PrettyPrinter()
s = LibgenSearch()

def get_book():
    book_title = input('Book Title: ')

    results = s.search_title(book_title)
    for result in results:
        printer.pprint(result)
        print()

    select = input('Select a book from the results: ')
    os.system('cls')

    item_to_dowload = results[int(select)]
    download_links = s.resolve_download_links(item_to_dowload)

    print('\nDownload Methods: ')
    for key, value in download_links.items():
        print(key)

    select = input("\nSelect Download Method: ")
    os.system('cls')

    url = download_links[select]
    request = requests.get(url)

    filename = input('Save as: ')
    filename += '.' + item_to_dowload['Extension']

    file = open(filename, 'wb')
    file.write(request.content)
    file.close()

    print('Download Successful. :)')

get_book()
