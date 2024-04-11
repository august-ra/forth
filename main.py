from settings import DATA_PATH
from products.categories import Categories


def main():
    result = Categories.load_from_file(DATA_PATH)

    if not result:
        exit(5)

    print(Categories.to_json())


if __name__ == '__main__':
    main()
