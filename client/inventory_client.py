import grpc

from service import InventoryService_pb2_grpc as is_grpc
from service import InventoryService_pb2 as is_pb2

class inventory_client:

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))
        self.stub = is_grpc.InventoryServiceStub(self.channel)

    def getBook(self,isbn):
        return self.stub.GetBook(is_pb2.GetBookRequest(isbn=isbn))
