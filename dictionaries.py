city_data = {'city': 'Москва', 'temperature': '20'}
print(city_data['city'])
city_data['temperature'] = str(int(city_data['temperature']) - 5)
print(city_data)
print(city_data.get('county'))
print(city_data.get('county', 'Россия'))
city_data['date'] = '27.05.2019'
print(len(city_data))
