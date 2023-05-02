import argparse
from parrot_gpt import ParrotGpt
from parrot_gpt.model_interface import GPT4Model, GPT3Model


MODEL_MAPPING = {
    "turbo": GPT4Model(),
    "gpt3": GPT3Model(),
    # Add other models here as needed
}

PROMPT_MAPPING = {
    "enrich": "Enriches the metadata",
    "translate": "Translates the metadata to another schema",
    "crosswalk": "Generates a crosswalk between two schemas",
    "peer_review": "Generates a peer review report for the input file",
}

def main():
    parser = argparse.ArgumentParser(description="Transform metadata using a selected large language model and prompt type.")
    parser.add_argument("--model", default="gpt3", choices=MODEL_MAPPING.keys(), required=True, help="The large language model to use.")
    parser.add_argument("--prompt-type", choices=PROMPT_MAPPING.keys(), required=True, help="The type of input prompt.")
    parser.add_argument("--input-file", required=True, help="The input metadata file.")
    parser.add_argument("--output-file", required=True, help="The output metadata file.")
    parser.add_argument('-i','--initial_schema', type=str, help='initial schema to convert to')
    parser.add_argument('-t','--target_schema', type=str, help='target schema to convert to')
    parser.add_argument('-v','--venue', type=str, help='venue to be peer reviewed')


    args = parser.parse_args()

    model = MODEL_MAPPING[args.model]
    parrot_gpt = ParrotGpt(model)

    with open(args.input_file, "r") as input_file:
        input_metadata = input_file.read()
    if len(input_metadata) > 2500:
        raise Exception("Metadata file is too large and it would require too many tokens. Please use a smaller file.")

    transformed_metadata = parrot_gpt.serialize(input_metadata, args)
    print(transformed_metadata)
    with open(args.output_file, "w") as output_file:
        output_file.write(transformed_metadata)

if __name__ == "__main__":
    main()
