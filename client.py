# client.py

import argparse
import grpc

import qa_service_pb2
import qa_service_pb2_grpc

def run():
    parser = argparse.ArgumentParser(description='QA Service Client')
    parser.add_argument('--input_documents', type=str, required=True, help='Path to the input text file')
    parser.add_argument('--input_questions', type=str, required=True, help='Path to the questions file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output answers file')
    parser.add_argument('--host', type=str, default='localhost', help='Host of the server')
    parser.add_argument('--port', type=str, default='50051', help='Port of the server')
    args = parser.parse_args()

    with open(args.input_documents, 'r') as file:
        text = file.read()

    with open(args.input_questions, 'r') as file:
        questions = [line.strip() for line in file.readlines()]

    with grpc.insecure_channel(f'{args.host}:{args.port}') as channel:
        stub = qa_service_pb2_grpc.QAServiceStub(channel)
        response = stub.AnswerQuestions(qa_service_pb2.QARequest(text=text, questions=questions))
    
    with open(args.output, 'w') as file:
        for answer in response.answers:
            file.write(answer + '\n')

if __name__ == '__main__':
    run()
