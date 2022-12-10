# 17625_hw3_and_hw4
The hw3 and hw 4 repo for cmu 17625

## Under this folder
## Run `python main.py` to get the test result, the second test needs 10s wating time

I am not very familiar with Python, so I met a lot import problems when I am implementing the solution. 

For HW3, I use postman to test my server, which is run `python library_server.py` under service folder. And then send request to grpc. The result was good and I got the screenshot in the screenshot folder.

However, in order to finish hw4, I modified some import syntax in some files. For example, in `InventoryService_pb2.py`, one import was `import Book_pb2 as Book__pb2` when this file was generated. And I change it to `from service import Book_pb2 as Book__pb2` in order to run my unit test. If I need to run `python library_server.py` again to use postman to test my HW3. There will be error says `no model named service`.

As a result, I keep the code as how it was after finishing HW4. Testing the result from HW3 requires multiple import modification.

