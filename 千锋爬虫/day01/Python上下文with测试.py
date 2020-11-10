class A():
    def __enter__(self):
        print('--enter--')
        return 'disen'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('--exit--')
        return False


if __name__ == '__main__':
    with A() as ret:
        print(ret)
        assert isinstance(ret, int)
        print('ok')