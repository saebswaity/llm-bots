class Session:
    def __init__(self, llm):
        self.llm = llm

    def get_response(self, message):
        return self.llm.get_response(message)
