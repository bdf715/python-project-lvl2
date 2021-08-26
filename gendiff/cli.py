import argparse


def get_path_to_files():
    '''
    return paths to files to compare
    '''
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    return args.first_file, args.second_file
