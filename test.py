import argparse
import requests

parser = argparse.ArgumentParser(description='Test api')
parser.add_argument(
    '--host',
    metavar='host',
    default='localhost',
    action='store',
    type=str,
    help='api host in format "X.X.X.X"'
)
parser.add_argument(
    '--port',
    metavar='port',
    default='4000',
    action='store',
    type=str,
    help='api port'
)

if __name__ == '__main__':
    args = parser.parse_args()
    url = f'http://{args.host}:{args.port}'

    print('Send image "image.jpg" to', f'{url}/upload')
    post_request = requests.post(
        f'{url}/upload',
        files={'file': open('image.jpg', 'rb')}
    )
    id = post_request.text
    print('Receive id:', id)

    print('Get image "image_test.jpg" from', f'{url}/get')
    get_request = requests.get(f'{url}/get', params={'id': id})

    with open('image_test.jpg', 'wb') as f:
        f.write(get_request.content)
