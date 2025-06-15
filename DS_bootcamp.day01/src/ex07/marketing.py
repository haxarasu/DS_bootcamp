import sys

clients = [
    'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com'
]
participants = [
    'walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
]
recipients = [
    'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
]


def get_non_viewed_clients(clients, participants, recipients):
    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)   
    non_viewed_clients = (clients_set - recipients_set) | (participants_set - recipients_set)
    return list(non_viewed_clients)


def get_potential_clients(participants, clients, recipients):
    participants_set = set(participants)
    clients_set = set(clients)
    recipients_set = set(recipients)
    potential_clients = (participants_set - clients_set) | (recipients_set - clients_set)
    return list(potential_clients)


def get_non_participating_clients(clients, participants, recipients):
    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)
    non_participating_clients = (clients_set - participants_set) | (recipients_set - participants_set)
    return list(non_participating_clients)


def main(task_name):
    if task_name == 'call_center':
        result = get_non_viewed_clients(clients, participants, recipients)
        print("Have not seen the letter", result)
    elif task_name == 'potential_clients':
        result = get_potential_clients(participants, clients, recipients)
        print("Not clients", result)
    elif task_name == 'loly_program':
        result = get_non_participating_clients(clients, participants, recipients)
        print("Did not participate:", result)
    else:
        print("Incorrect input")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect input")
    else:
        task_name = sys.argv[1]
        main(task_name)