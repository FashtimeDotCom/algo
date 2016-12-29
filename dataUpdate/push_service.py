# coding:utf-8


if __name__ == "__main__":
    from argparse import ArgumentParser

    parse = ArgumentParser()
    parse.add_argument('-r', '--run', dest="run_type", action="store",help="test or online")
    args = parse.parse_args()
