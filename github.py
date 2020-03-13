import requests


class Github:

    def __init__(self, user):
        self.user = user

    def get_repositories_github(self):
        response = requests.get('https://api.github.com/users/' + self.user + '/repos')
        return response.json()

    # Limpa a data para ficar no formato AAAA-MM-DD
    @staticmethod
    def format_date(date):
        return date[0:10]

    # Extrai apenas as informações relevantes para o cadastro
    def clean_repository(self, repository):
        return {
            'title': repository['name'] or 'None',
            'description': repository['description'] or 'None',
            'created_at': self.format_date(repository['created_at']) or 'None',
            'language': repository['language'] or 'None',
        }

    def get_formatted_repositories(self):
        repositories = self.get_repositories_github()
        return list(map(lambda repository: self.clean_repository(repository), repositories))
