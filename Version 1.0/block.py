class Block:
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}'


def main():
    print(f'block.py __name__: {__name__}')


if __name__ == '__main__':
    main()
