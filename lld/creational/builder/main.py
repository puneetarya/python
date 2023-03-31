from builder import UrlBuilder

builder = UrlBuilder()
url = builder.with_scheme('https') \
            .with_host('example.com') \
            .with_path('/path/to/resource') \
            .with_query_param('param1', 'value1') \
            .with_query_param('param2', 'value2') \
            .build()

print(url)  # Output: "https://example.com/path/to/resource?param1=value1&param2=value2"

builder1 = UrlBuilder()
url1 = builder1.with_scheme('https') \
            .with_host('example.com') \
            .build()
print(url1)