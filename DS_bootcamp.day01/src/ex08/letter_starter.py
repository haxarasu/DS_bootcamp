import sys

def get_first_paragraph(email):
    with open('employees.tsv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                if parts[2] == email:
                    return f"Dear {parts[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."


print(get_first_paragraph(sys.argv[1]))