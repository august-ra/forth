from pathlib import Path


ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "products.json")
EMPTY_PATH = ROOT_PATH.joinpath("data", "empty.json")
