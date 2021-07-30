from libgen_api import LibgenSearch
import pprint
import requests
import os

# os.chdir('D:\Cs\Python\libgen_api')
os.chdir('Download')

printer = pprint.PrettyPrinter()
s = LibgenSearch()

def get_book():
    # Prompts User to searcha book titl
    book_title = input('Book Title: ')

    # prints the results
    results = s.search_title(book_title)
    for result in results:
        printer.pprint(result)
        print()

    #  prompts the user to select a book from the selection
    select = input('Select a book from the results: ')
    os.system('cls')

    # fetches download links from the request
    item_to_dowload = results[int(select) - 1]
    download_links = s.resolve_download_links(item_to_dowload)

    # prompts user to select download methods
    print('\nDownload Methods: ')
    for key, value in download_links.items():
        print(key)

    select = input("\nSelect Download Method: ")
    os.system('cls')

    # send an api request for downloading the book
    url = download_links[select]
    request = requests.get(url)

    filename = f'{item_to_dowload["Title"]}.{item_to_dowload["Extension"]}'

    # saves the contents into file
    file = open(filename, 'wb')
    file.write(request.content)
    file.close()

    print('Download Successful. :)')

get_book()
