class Daemon(object):
    def __init__(self, backend):
        self._backend = backend

    def info(self):
        return self._backend.info()

    def height(self):
        return self._backend.info()['height']

    def send_transaction(self, tx, relay=True):
        return self._backend.send_transaction(tx.blob, relay=relay)

    def mempool(self):
        return self._backend.mempool()
