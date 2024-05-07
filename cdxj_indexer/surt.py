import re
from urllib.parse import urlparse, parse_qs, urlencode

def url_to_surt(url: str):
    try:
        if (not url.startswith("https:")) and (not url.startswith("http:")):
            return url
        parsed_url = urlparse(url.lower())
        host_parts = parsed_url.hostname.split(".")
        if len(host_parts) > 1 and host_parts[0] == "www":
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
    return re.sub(pattern, '', query)
