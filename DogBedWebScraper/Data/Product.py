class Product:
    def __init__(self, vendor: str, product_name: str, price: str, url: str):
        self.vendor = vendor
        self.product_name = product_name
        self.price = price
        self.url = url
        if 'Small' in product_name:
            self.size_class = 'Small'
        elif 'Medium' in product_name:
            self.size_class = 'Medium'
        elif 'X-Large' in product_name:
            self.size_class = 'X-Large'
        elif 'Large' in product_name:
            self.size_class = 'Large'
        elif 'medium' in product_name:
            self.size_class = 'Medium'
        elif 'x-large' in product_name:
            self.size_class = 'X-Large'
        elif 'large' in product_name:
            self.size_class = 'Large'
        elif 'small' in product_name:
            self.size_class = 'Small'

    def __str__(self):
        return f'{self.vendor},{self.size_class},{self.product_name},{self.price},{self.url}'
