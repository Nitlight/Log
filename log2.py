import json
from log import LoggerParam


class Logger:
    @staticmethod
    def write_to_json(data : dict) -> None:
        path_to_file = "data.json"
        with open(path_to_file, 'a') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @ staticmethod
    def info(message : str, param : LoggerParam = None):
        if param is None:
            param = LoggerParam(tag="INFO", message=message)

        Logger.write_to_json(param.parse_to_dict())


def plus(a, b):
    Logger.info(f"{plus.__name__} opened with parameters {a} и {b}")
    res = a + b
    Logger.info(f"{plus.__name__} finish with resultat: {res}")
    return res


def main():
    plus(1, 5)


if __name__ == "__main__":
    main()