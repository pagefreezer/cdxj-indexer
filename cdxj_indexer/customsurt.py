import re
from urllib.parse import urlparse, parse_qs, urlencode, quote_plus

def url_to_surt(url: str):
    try:
        if (not url.startswith("https:")) and (not url.startswith("http:")):
            return url
        parsed_url = urlparse(url.lower())
        host_parts = parsed_url.hostname.split(".")
        if len(host_parts) > 1 and re.match(r'^www\d*$', host_parts[0]):
            host_parts = host_parts[1:]
        host_parts = reversed(host_parts)
        surt = ",".join(host_parts)
        if parsed_url.port is not None:
            surt += ":" + str(parsed_url.port)
        surt += ")"
        if parsed_url.path == "":
            surt += "/"
        else:
            surt += parsed_url.path
        if parsed_url.query != "":
            query = normalize_query(parsed_url.query)
            parsed_url = parsed_url._replace(query=query)
            surt += "?" + parsed_url.query
        return surt
    except Exception as e:
        return url

def normalize_query(query: str):
    query_params = parse_qs(query, keep_blank_values=True)
    sorted_query_params = sorted(query_params.items())
    query = urlencode(sorted_query_params, doseq=True)
    # remove '=' in query params when there is no value
    pattern = r'=(?=[&]|$)'
    return re.sub(pattern, '', query).replace('~', '%7E')


def normalize_query_new(query: str) -> str:
    # Parse the query string into a dictionary (key: list of values)
    query_params = parse_qs(query, keep_blank_values=True)

    # Sort the query parameters by key
    sorted_query_params = sorted(query_params.items())

    # Rebuild the query string manually
    normalized_query = []

    # Get the keys and whether they have associated values
    kv = check_query_keys(query)

    # Convert kv list to a dictionary for easier lookup
    kv_dict = dict(kv)

    for key, values in sorted_query_params:
        encoded_key = quote_plus(key).replace('~', '%7E')

        # Check if the key should be without a value
        if not kv_dict.get(key, False):
            normalized_query.append(f"{encoded_key}")
        else:
            for value in values:
                if value == '':
                    normalized_query.append(f"{encoded_key}=")
                else:
                    encoded_value = quote_plus(value, '' ).replace('~', '%7E')
                    normalized_query.append(f"{encoded_key}={encoded_value}")

    # Join the components into a normalized query string
    return '&'.join(normalized_query)


def check_query_keys(query: str):
    # Split the query string by '&' to get individual key-value pairs
    pairs = query.split('&')

    # Initialize a list to store the results
    result = []

    for pair in pairs:
        # Split each pair by '=' to separate the key and the value
        parts = pair.split('=', 1)

        # If the split results in a list with only one part, it means there was no '=' in the pair
        key = parts[0]
        has_equal_sign = len(parts) > 1

        # Append a tuple to the result list
        result.append((key, has_equal_sign))

    return result
