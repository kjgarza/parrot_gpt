import os
import openai
import logger
import json
from parrot_gpt.prompts import EXAMPLES, schema_prompt, enrich_prompt, peerreview_prompt
from parrot_gpt.exceptions import EmptyMetadataError, UnsupportedSchemaStandard

class ParrotGpt:
    def __init__(self, api_key=None):
      # Load your API key from an environment variable or secret management service
      openai.api_key = os.getenv("OPENAI_API_KEY")
      self.model_params = {
          'model': "text-davinci-003",
          'temperature': 0.2,
          'max_tokens': 900,
          'top_p': 1.0,
          'frequency_penalty': 0.0,
          'presence_penalty': 0.0,
      }

      self._supported_schema_standards = ["DATS", "cff", "crossref_xml", "JATS", "BioSchema", "Codemeta", "RIF-CS", "EDMI", "DCAT", "DCAT-AP", "DCAT-AP-NO", "DCAT-AP-SE", "DCAT-AP-DE", "DCAT-AP-IT", "DCAT-AP-CH", "DCAT-AP-ES", "DCAT-AP-GB", "DCAT-AP-IE", "DCAT-AP-NO", "DCAT-AP-SE", "DCAT-AP-AT", "DCAT-AP-PT", "DCAT-AP-RO", "DCAT-AP-GR", "DCAT-AP-LV", "DCAT-AP-LT", "DCAT-AP-HU", "DCAT-AP-CZ", "DCAT-AP-SK", "DCAT-AP-BE", "DCAT-AP-NL", "DCAT-AP-FR", "DCAT-AP-PL", "DCAT-AP-EE", "DCAT-AP-FI", "DCAT-AP-I", "DataCite", "DataCite-XML", "DataCite-JSON", "Crossref", "Crossref", "schema.org", "bibtex", "DC-XML", "DC-JSON", "Dublin Core"]


    def _transform_metadata(self, metadata, initial_schema, target_schema):
        # Use the OpenAI API to transform metadata to the target schema
        # Return the transformed metadata

        metadata = self.serialize(metadata, initial_schema, target_schema)

        prompt = schema_prompt.format(
            metadata = metadata,
            target_schema= target_schema,
            metadata_example=EXAMPLES['metadata'],
            result_example=EXAMPLES['result_dc'],
            initial_schema=initial_schema
        )

        try:
            response = openai.Completion.create(**self.model_params, prompt=prompt)
        except Exception as e:
            print(e)
            return {}

        return response.choices[0].text
    
    def _enrich_metadata(self, metadata):

        metadata = self.serialize(metadata)

        prompt = enrich_prompt.format(
            metadata = metadata,
            metadata_example=EXAMPLES['metadata'],
            result_example=EXAMPLES['result_dc'],
        )

        try:
            response = openai.Completion.create(**self.model_params, prompt=prompt)
        except Exception as e:
            print(e)
            return {}

        return response.choices[0].text
    

    def _peerreview_article(self, article, venue):

        article = self.serialize(article)

        prompt = peerreview_prompt.format(
            article = article,
            venue = venue,
        )

        try:
            response = openai.Completion.create(**self.model_params, prompt=prompt)
        except Exception as e:
            print(e)
            return {}

        return response.choices[0].text


    def serialize(self, metadata_file, initial_schema=None, target_schema=None):
      
        if metadata_file is None:
            raise EmptyMetadataError("metadata_file cannot be empty for schema generation request!")

        # if target_schema not in self._supported_schema_standards:
        #     raise UnsupportedSchemaStandard(f"{target_schema} standard isn't supported for schemas!")

        with open(metadata_file, 'r') as f:
            metadata = f.read()

        if len(metadata) > 2500:
            raise Exception("Metadata file is too large and it would require too many tokens. Please use a smaller file.")

        return metadata
        # return self._transform_metadata(metadata, initial_schema, target_schema)
        

