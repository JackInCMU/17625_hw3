import unittest

from client import inventory_client as client
from client.get_book_titles import getTitles
from service import library_server as server
from unittest.mock import patch, MagicMock
from service import InventoryService_pb2 as is_pb2

class BaseTestCases:
    class BaseTest(unittest.TestCase):
        mock_client = None
        isbns = ['10001','10002']

        def setUp(self):
            server.serve()
            self.mock_client = client.inventory_client()
        
        def tearDown(self):
            server.stop_serve()

#test for question 5
class SubTest1(BaseTestCases.BaseTest):

    @patch('client.inventory_client.inventory_client.getBook')
    def testSub1(self,getBook_mock):
        books = [{
            'id' : '10001',
            'title' : 'book1',
            'author' : 'author1',
            'genre' : 'GENRE_FANTASY',
            'publishYear' : 2020
        },{
            'id' : '10002',
            'title' : 'book2',
            'author' : 'author2',
            'genre' : 'GENRE_DYSTOPIAN',
            'publishYear' : 2021
        }]
        book1 = is_pb2.GetBookResponse(title=books[0]['title'],author=books[0]['author'],genre=books[0]['genre'],publishYear=books[0]['publishYear'])
        book2 = is_pb2.GetBookResponse(title=books[1]['title'],author=books[1]['author'],genre=books[1]['genre'],publishYear=books[1]['publishYear'])
        mock_data = []
        mock_data.append(book1)
        mock_data.append(book2)
        getBook_mock.side_effect = iter(mock_data)
        res = getTitles(self.isbns,self.mock_client)
        expected = ['book1','book2']
        self.assertCountEqual(res,expected)

#test for question 6
class SubTest2(BaseTestCases.BaseTest):

    def testSub2(self):
        res = getTitles(self.isbns,self.mock_client)
        expected = ['book1','book2']
        self.assertCountEqual(res,expected)

if __name__ == '__main__':
    unittest.main()
    
