import requests


class Github:

    def __init__(self, user):
        self.user = user

    def get_repositories_github(self):
        response = requests.get('https://api.github.com/users/' + self.user + '/repos')
        return response.json()

    # Extrai apenas as informações relevantes para o cadastro
    @staticmethod
    def clean_repository(repository):
        return {
            'title': repository['name'] or 'None',
            'description': repository['description'] or 'None',
            'created_at': repository['created_at'][0:10] or 'None',
            'language': repository['language'] or 'None',
        }

    def get_formatted_repositories(self):
        repositories = self.get_repositories_github()
        return list(map(lambda repository: self.clean_repository(repository), repositories))
