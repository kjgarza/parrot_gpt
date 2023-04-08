import argparse
import sys
import parrot_gpt

def main():
    """Console script for parrot_gpt."""
    parser = argparse.ArgumentParser()

    parser.add_argument('-mf','--metadata_file', type=str, help='metadata file to be converted')
    parser.add_argument('-a','--article_file', type=str, help='article file to be peer reviewed')
    parser.add_argument('-v','--venue', type=str, help='venue to be peer reviewed')
    parser.add_argument('-i','--initial_schema', type=str, help='initial schema to convert to')
    parser.add_argument('-t','--target_schema', type=str, help='target schema to convert to')
    parser.add_argument('-e','--enrich', action='store_true', help='enrich metadata')
    parser.add_argument('-f', '--fair', action='store_true', help='generate fair metadata')
    parser.add_argument('-pr', '--peer-review', action='store_true', help='generate peer review of an article')
    parser.add_argument('-ex', '--examples', action='store_true', help='include examples of metadata')

    args = parser.parse_args()

    if args.enrich:
        response = parrot_gpt.ParrotGpt()._enrich_metadata(args.metadata_file)
    elif args.fair:
        response = parrot_gpt.ParrotGpt().fair_metadata(args.metadata_file)
    elif args.peer_review:
        response = parrot_gpt.ParrotGpt()._peerreview_article(args.article_file, args.venue)
    elif args.examples:
        response = parrot_gpt.ParrotGpt().examples(args.metadata_file)
    else:
        response = parrot_gpt.ParrotGpt()._transform_metadata(args.metadata_file, args.initial_schema, args.target_schema)

    # response = parrot_gpt.ParrotGpt().serialize(args.metadata_file, args.initial_schema, args.target_schema)
    print(response)
    return 0

if __name__ == "__main__":
    sys.exit(main())
