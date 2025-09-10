import socket

def start_client():
    host = '127.0.0.1'
    port = 123

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.settimeout(1000)

    print(f"Conectado ao servidor em {host}:{port}")

    received_questions = receive_questions(client_socket)
    print_questions(received_questions)

    answers = input_answers()
    send_answers(client_socket, answers)

    client_socket.close()

def receive_questions(client_socket):
    received_questions = []

    for _ in range(2):
        question = client_socket.recv(1024).decode()
        received_questions.append(question)

    return received_questions

def print_questions(questions):
    for question in questions:
        print(question)

def input_answers():
    answers = []
    for _ in range(2):
        answer = input("Resposta letra: ").lower()
        answers.append(answer)

    return answers

def send_answers(client_socket, answers):
    for answer in answers:
        client_socket.send(answer.encode())

if __name__ == "__main__":
    start_client()
