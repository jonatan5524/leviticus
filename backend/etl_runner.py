from etl import ETL

import arrow
import argparse
import inspect
import importlib

def main():
    parser = argparse.ArgumentParser(description='Run ETL')
    parser.add_argument('filename', help="filename")

    args = parser.parse_args()

    print(args.filename)

    match = inspect.getmembers(importlib.import_module(name=f".{args.filename}", package="etls"), lambda x: (not inspect.isabstract(x)) and inspect.isclass(x) and issubclass(x, ETL) )

    match[0][1](arrow.get(arrow.get().format('YYYY-MM-DD')))._run()

if __name__ == "__main__":
    main()