import os
import openai
import logger
import json
from parrot_gpt.model_interface import *
from parrot_gpt.prompts import *
from parrot_gpt.exceptions import EmptyMetadataError, UnsupportedSchemaStandard


class ParrotGpt:

    def __init__(self, model):
        self.model = model
        self.prompt = { "system": "", "user": ""}

    def serialize(self, input_metadata, args):
        self._create_prompt(input_metadata, args)
        transformed_prompt = self.model.transform_prompt(self.prompt)
        # transformed_metadata = self._transform_metadata(transformed_prompt)
        return transformed_prompt

    def _create_prompt(self, input_metadata, args):

        if args.prompt_type == "enrichment":
            self.prompt["user"] = fair_prompt.format(
                metadata = input_metadata,
                fair= args.fair
            )
        elif args.prompt_type == "peer_review":
            self.prompt["user"] = peer_review_prompt.format(
                metadata = input_metadata,
                venue= args.venue
            )
        elif args.prompt_type == "crosswalk":
            self.prompt["system"] = crosswalk_system_prompt
            self.prompt["user"] = crosswalk_prompt.format(
                target_schema= args.target_schema,
                initial_schema= args.initial_schema
            )
        else:
            self.prompt["system"] = schema_system_prompt
            self.prompt["user"] = schema_prompt.format(
                metadata = input_metadata,
                target_schema= args.target_schema,
                initial_schema= args.initial_schema
            )
