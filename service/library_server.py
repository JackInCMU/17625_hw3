import grpc
from concurrent import futures

from service import InventoryService_pb2_grpc as is_pb2_grpc
from service import InventoryService_pb2 as is_pb2


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

class InventoryService(is_pb2_grpc.InventoryServiceServicer):
    def CreateBook(self, request, context):
        tmp = request.newBook
        new = {
            'id' : tmp.id,
            'title' : tmp.title,
            'author' : tmp.author,
            'genre' : tmp.genre,
            'publishYear' : tmp.publishYear
        }
        books.append(new)
        return is_pb2.CreateBookResponse(message='created!')

    def GetBook(self, request, context):
        isbn = request.isbn
        theBook = {}
        for book in books:
            if str(book['id']) == isbn:
                theBook['title']=book['title']
                theBook['author']=book['author']
                theBook['genre']=book['genre']
                theBook['publishYear']=book['publishYear']
                break
        return is_pb2.GetBookResponse(title=theBook['title'],author=theBook['author'],genre=theBook['genre'],publishYear=theBook['publishYear'])

server = None
'''
    in this server function, the wait_for_termination() is commented
    because when testing I can't let it wait
    so if tested in postman, the line should be uncommented
'''
def serve():
   global server
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   is_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
   server.add_insecure_port("[::]:50051")
   server.start()
   #server.wait_for_termination()

'''
    stop the grpc funtion gracefully
'''
def stop_serve():
    global server
    done_event = server.stop(5)
    done_event.wait(5)


if __name__ == "__main__":
   print("running the gRPC server")
   serve()