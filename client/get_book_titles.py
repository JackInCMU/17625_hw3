from client import inventory_client

def getTitles(isbns,client):
    res = []
    for isbn in isbns:
        response = client.getBook(isbn)
        res.append(response.title)
    return res

if __name__ == '__main__':
    client = inventory_client()
    isbns = ['10001','10002']
    titles = getTitles(isbns,client)
    for title in titles:
        print(title)
