from requests \
    import get

from json \
    import loads


distributions: str = 'https://raw.githubusercontent.com/designermadsen-public-dataset/TMOD/load_by_script/distribution.providers.json'

def get_distribution_providers_url() -> str:
    global distributions
    return distributions

def retrieve_providers() -> dict:
    providers_json = get(
        get_distribution_providers_url()
    )

    return loads(
        providers_json.content
    )
