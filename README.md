# Question_Answering

This project is an implementation of question answering (qa) using gRPC. The service get a txt file of document and a text file of questions and return the output text file of answers

## Project Structure

- This solution requires clean installation of Ubuntu 22.04 .
- `qa_service.proto`: The Protocol Buffers definition file for the qa service.
- `setup.sh`: Run this file (`./setup.sh`) in the Ubuntu environment to update the system, install python3 and pip3 and also install required python libararies. 
- `build.sh`: Run this file (`./build.sh`) in the Ubuntu environment to create `qa_service_pb2.py` and `qa_service_pb2_grpc.py` from `qa_service.proto`.
- `server.py`: The Python script for the qa service server.
- `client.py`: The Python script for the qa service client.

## Run Server:
### Run server locally:
To run server locally, can use following command: `python3 server.py --host localhost --port 50051`
### Run server remotely: 
To run server to be accessible from a remote machine, can use following command: `python3 server.py --host 0.0.0.0 --port 50051` 
The --host argument of the server script should be set to 0.0.0.0 to accept connections from any IP address.

## Run Client:
To run client, run the following command: `python3 client.py --input_documents input.txt --input_questions questions.txt --output output.txt --host server_public_ip_or_hostname --port 50051`

Client can accept 2 inputs (`input_documents`, `input_questions`).

The format of input and ouput images should be txt.

If the question is outside the scope of the input text (document), it will give a generic answer "out of scope".
