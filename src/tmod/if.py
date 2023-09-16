distributions: str = 'https://raw.githubusercontent.com/designermadsen-public-dataset/TMOD/load_by_script/distribution.providers.json'

def get_distribution_providers() -> str:
    global distributions
    return distributions
