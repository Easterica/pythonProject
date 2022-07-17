class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
input_line = input()

while input_line != "Stop":
    list_of_input = input_line.split()
    sender = list_of_input[0]
    receiver = list_of_input[1]
    content = list_of_input[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    input_line = input()

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())


