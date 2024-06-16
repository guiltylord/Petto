from datetime import datetime


class message:
    def __init__(
        self,
        sender_id: int,
        receiver_id: int,
        content: str,
    ):
        # self.message_id = self.make_id()
        self.content = content
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.create_time = datetime.datetime.now()

    def make_id(self):
        ...
