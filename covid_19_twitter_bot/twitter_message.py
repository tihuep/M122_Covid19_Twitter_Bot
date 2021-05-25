class Message:
    def __init__(self, id, sender, recipient, data):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.data = data

    @staticmethod
    def from_event(event):
        message_create = event['message_create']
        id = event['id']
        recipient = message_create['target']['recipient_id']
        sender = message_create['sender_id']
        data = message_create['message_data']['text']
        return Message(
            id=id,
            sender=sender,
            recipient=recipient,
            data=data)

    def to_event(self):
        return {
            "event": {
                "type": "message_create",
                "message_create": {
                    "target": {
                        "recipient_id": self.recipient
                    },
                    "message_data": {
                        "text": self.data
                    }
                }
            }
        }