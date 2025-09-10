import socket

def start_server():
    host = '127.0.0.1'
    port = 123

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    server_socket.settimeout(1000)
    

    print(f"Servidor aguardando conexão em {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        send_questions(client_socket)
        correct_answers, incorrect_answers = receive_answers(client_socket)
        
        ##score = receive_answers(client_socket)
        ##print(f"Cliente acertou {score} questões\n")

        print(f"Cliente acertou {len(correct_answers)} questões")
        print(f"Respostas corretas: {correct_answers}")
        print(f"Respostas incorretas: {incorrect_answers}\n")


        client_socket.close()

def send_questions(client_socket):
    questions = [
        "Qual a capital da Italia?\na) Roma\nb) Paris\nc) Lisboa\nd) Londres",
        "Cumprimento em Portugues?\na) Uai\nb) Ai\nc) Oi\nd) Ui",
    ]

    for question in questions:
        client_socket.send(question.encode())

def receive_answers(client_socket):
    correct_answers = ['a', 'c']
    received_correct = []
    received_incorrect = []
    
    ##score = 0

    for _ in range(len(correct_answers)):
        answer = client_socket.recv(1024).decode().strip().lower()
        if answer == correct_answers[_]:
           received_correct.append(answer)
        else:
            received_incorrect.append(answer)

    return received_correct, received_incorrect
           ## score += 1

    ##return score

if __name__ == "__main__":
    start_server()
