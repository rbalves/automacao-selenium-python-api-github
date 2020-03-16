from github import Github
from automation import Automation

github = Github('rbalves')
projects = github.get_formatted_repositories()

automation = Automation()
automation.add_projects(projects)
