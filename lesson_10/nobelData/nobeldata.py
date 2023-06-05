import json

class NobelData:

    def __init__(self, name_of_file):
        self._name_of_file = name_of_file
        self._noble_json_data = ''
        
        with open(name_of_file, 'r') as infile:
            self._noble_json_data = json.load(infile)
        

    def search_nobel(self, year, category):
        # answer is going to look like: ['Curie', 'Miller']
        names = [] 

        for data in self._noble_json_data['prizes']:
            if data['year'] == year and data['category'] == category:
                for winner in data['laureates']: 
                    names.append(winner['surname'])
        return names 


nd = NobelData('nobels.json')
print(nd.search_nobel("2001", "economics"))