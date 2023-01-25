from ExtractTable import ExtractTable

class Extracttables:
    def __init__(self, **kw):
        print(f'New extracttables with options {kw} {kw["api-key"]}')

        et_sess = ExtractTable(api_key=kw["api-key"])

        print(et_sess.check_usage())

    def extract_tables(self, args):
        print(f"extract with args {args}")