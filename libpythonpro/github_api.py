import requests


def search_avatar(user):
    """
    Search avatar of an user in GitHub
    :param user: str with name of user on GitHub
    :return: str url to avatar picture
    """

    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    return response.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('fernando-stteffen'))
