from cleverbotfree.cbfree import Cleverbot as CBFree


class Cleverbot:
    def __init__(self):
        self.session = CBFree()
        self.is_usable = True
        try:
            self.session.browser.get(self.session.url)
        except Exception as e:
            raise e

    def ask(self, query):
        if self.is_usable is False:
            raise Exception("The session is unusable.")
        try:
            self.session.get_form()
        except Exception as e:
            raise e
        self.session.send_input(query)
        return self.session.get_response()

    def close(self):
        self.session.browser.close()
        self.is_usable = False
