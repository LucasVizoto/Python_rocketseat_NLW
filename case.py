class MyClass():
    def __enter__(self):
        print("Entrei")
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Sai")

with MyClass() as mc:
    print("Dentro do bloco")

# automatizar a criação das sessões