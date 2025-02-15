import urllib.request, json

# Get a organizations repo
def get_org_repositories(org):
    url = 'https://api.github.com/orgs/' + org + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

# Get a users repo
def get_user_repositories(user):
    url = 'https://api.github.com/users/' + user + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

# Get a user profile
def get_user(user):
    url = 'https://api.github.com/users/' + user 
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return data

# Get a organizations profile
def get_org(org):
    url = 'https://api.github.com/orgs/' + org 
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return data

# Get all the github emojis cuz why not?
def get_emoji():
    url = 'https://api.github.com/emojis'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return data

# Get a repos branches
def get_repo_branches(user, repo):
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/branches'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return data

# Get organizations projects
def get_org_projects(org):
    url = 'https://api.github.com/orgs/' + org + '/projects'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return data