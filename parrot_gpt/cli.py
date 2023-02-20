import argparse
import sys
import parrot_gpt

def main():
    """Console script for parrot_gpt."""
    parser = argparse.ArgumentParser()

    parser.add_argument('-mf','--metadata_file', type=str, help='metadata file to be converted')
    parser.add_argument('-i','--initial_schema', type=str, help='initial schema to convert to')
    parser.add_argument('-t','--target_schema', type=str, help='target schema to convert to')
    parser.add_argument('-f', '--fair', action='store_true', help='generate fair metadata')
    parser.add_argument('-e', '--examples', action='store_true', help='include examples of metadata')

    args = parser.parse_args()

    response = parrot_gpt.ParrotGpt().serialize(args.metadata_file, args.initial_schema, args.target_schema)
    print(response)
    return 0

if __name__ == "__main__":
    sys.exit(main())
