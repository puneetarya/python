class UrlBuilder:
    def __init__(self):
        self.scheme = ''
        self.host = ''
        self.path = ''
        self.query_params = {}

    def with_scheme(self, scheme):
        self.scheme = scheme
        return self

    def with_host(self, host):
        self.host = host
        return self

    def with_path(self, path):
        self.path = path
        return self

    def with_query_param(self, key, value):
        self.query_params[key] = value
        return self

    def build(self):
        url = self.scheme + '://' + self.host + self.path
        if self.query_params:
            query_str = '&'.join([f'{k}={v}' for k, v in self.query_params.items()])
            url += f'?{query_str}'
        return url
