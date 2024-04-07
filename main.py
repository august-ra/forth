from settings import DATA_PATH
from products.categories import Categories


def main():
    categories = Categories.load_from_file(DATA_PATH)
    print(categories.to_json())


if __name__ == '__main__':
    main()
