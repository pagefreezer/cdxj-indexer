import surt
import customsurt

# List of URLs
urls = [
    "https://www2.ed.gov/fund/grants-college.html?src=pn",
    "https://test.org/s?test=aap&koe",
    "https://test.org/s?t ~est^2=aap koe",
    "https://test.org/s?t ~est^2=",
    "https://test.org/s?t ~est^2",
    "http://example.com/path/to/resource?query=param",
    "http://example.com/path/to/resource?query=",
    "http://example.com/path/to/resource?query",
    "https://sub.domain.org/some/path",
    "https://test.org/s?e st2",
    # Add more URLs here
    "http://www.archive.org/",
    "http://archive.org/" ,
    "http://archive.org/goo/?",
    "http://archive.org/goo/",
    "http://archive.org/goo/?b&a",
    "http://archive.org/goo/?a=2&b&a=1",
    "http://archive.org/goo/?a=2&b&a=1#aa2",

    'https://test.org/s?test^2=',
    "https://test.org/s?test^2",
]

# List of verification SURTs
verify_surts = [
    "gov,ed)/fund/grants-college.html?src=pn",
    "org,test)/s?koe&test=aap",
    "org,test)/s?t+%7Eest%5E2=aap+koe",
    "org,test)/s?t+%7Eest%5E2=",
    "org,test)/s?t+%7Eest%5E2",
    "com,example)/path/to/resource?query=param",
    "com,example)/path/to/resource?query=",
    "com,example)/path/to/resource?query",
    "org,domain,sub)/some/path",
    "org,test)/s?e+st2",
    # Add more SURTs here
    'org,archive)/',
    'org,archive)/',
    'org,archive)/goo/',
    'org,archive)/goo/',
    'org,archive)/goo/?a&b',
    'org,archive)/goo/?a=2&a=1&b',
    'org,archive)/goo/?a=2&a=1&b',

    'org,test)/s?test%5E2=',
    'org,test)/s?test%5E2',

]

# Loop through each URL, convert to SURT, and verify against the SURTs
for i, url in enumerate(urls):
    #print(f"Original URL: {url}")
    custom_surt_url = customsurt.url_to_surt(url)


   # print(f"orv SURT: {surt.surt(url)}")

    if custom_surt_url != verify_surts[i]:
        print("Verification Failed!")
        print(f"Original URL: {url}")
        print(f"Converted SURT: {custom_surt_url}")
        print(f"Verify    SURT: {verify_surts[i]}")


    print('---')
