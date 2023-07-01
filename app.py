from flask import Flask, request, render_template
import argparse
import grpc

import qa_service_pb2
import qa_service_pb2_grpc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        questions = request.form.get('questions').split('\n')

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = qa_service_pb2_grpc.QAServiceStub(channel)
            response = stub.AnswerQuestions(qa_service_pb2.QARequest(text=text, questions=questions))
        
        answers = response.answers

        return render_template('index.html', answers=answers, text=text, questions=questions)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
