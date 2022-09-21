def leaf(cls):
    class _wrapper(cls):
        def add(self, d):
            raise RuntimeError()

        def remove(self, d):
            raise RuntimeError()

    return _wrapper
