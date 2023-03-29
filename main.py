import requests

response = requests.get("https://gitlab.com/api/v4/users/14128024/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} \n User ID: {project['id']} \n Project Link: {project['http_url_to_repo']} \n")
