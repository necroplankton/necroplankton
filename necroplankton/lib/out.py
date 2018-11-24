import json


class Put(object):
    def __init__(self):
        self._dir = './'

    @staticmethod
    def name_it(name, suffix):
        if name.endswith(suffix):
            return name
        else:
            return name + suffix

    def py(self, obj, filename="dump"):

        name = self.name_it(filename, '.py')

        with open(self._dir + name, 'w') as file:
            file.write('data = ' + str(obj))

    def json(self, obj, filename="dump"):

        name = self.name_it(filename, '.json')

        with open(self._dir + name, 'w') as file:
            json.dump(obj, file, ensure_ascii=False, indent=4)

    def md(self, obj, filename="dump"):

        name = self.name_it(filename, '.md')

        _text = [filename]
        with open(self._dir + name, 'w') as file:
            for key in obj:
                _text.append(f'## {key}')
                for value in obj[key]:
                    _text.append(f'- {value}')
            file.write('\n\n'.join(_text))
