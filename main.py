import requests

def get_user_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()

        data = response.json()
        user_ip = data['ip']

        return user_ip
    except requests.exceptions.RequestException as e:
        print(f'Hata oluştu: {e}')
        return None

def get_country_from_ip(ip_address):
    try:
        access_key = 'Kendi API Anahtarınızı Gireceksiniz '
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={access_key}')
        response.raise_for_status()

        data = response.json()
        country_name = data['country_name']

        return country_name
    except requests.exceptions.RequestException as e:
        print(f'Hata oluştu: {e}')
        return None

if __name__ == '__main__':

    user_ip = get_user_ip()

    if user_ip:
        print(f'Kullanıcının dış IP adresi: {user_ip}')

        country = get_country_from_ip(user_ip)

        if country:
            print(f'IP adresinin bulunduğu ülke: {country}')
        else:
            print('Ülke bilgisi alınamadı.')
    else:
        print('Dış IP adresi alınamadı.')