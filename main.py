import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, loadfile: str, savefile):

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        res = requests.get(f'{url}/upload?path={savefile}&overwrite=True', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


if __name__ == '__main__':

    loadfile = r'/Users/lovkovdmitry/Downloads/anydesk.dmg'
    savefile = 'anydesk.dmg'
    token = ''
    uploader = YaUploader(token)

YaUploader.upload(YaUploader, loadfile, savefile)
