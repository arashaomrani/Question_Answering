# server.py

import argparse
from concurrent import futures
import grpc
from transformers import pipeline

import qa_service_pb2
import qa_service_pb2_grpc

class QAServiceServicer(qa_service_pb2_grpc.QAServiceServicer):
    def __init__(self):
        self.nlp = pipeline('question-answering', model='deepset/roberta-base-squad2')

    def AnswerQuestions(self, request, context):
        text = request.text
        questions = request.questions
        answers = []
        for question in questions:
            try:
                result = self.nlp(question=question, context=text)
                answer = result['answer']
                score = result['score']
                if answer.strip() == '' or score < 0.2:
                    answer = 'out of scope'
            except Exception as e:
                answer = 'out of scope'
            answers.append(answer)
        return qa_service_pb2.QAResponse(answers=answers)

def serve():
    parser = argparse.ArgumentParser(description='QA Service Server')
    parser.add_argument('--host', type=str, default='localhost', help='Host to bind the server to')
    parser.add_argument('--port', type=str, default='50051', help='Port to bind the server to')
    args = parser.parse_args()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    qa_service_pb2_grpc.add_QAServiceServicer_to_server(QAServiceServicer(), server)
    server.add_insecure_port(f'{args.host}:{args.port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
