import yaml

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = read_config('config.yaml')
    
    # Access the configuration values
    user_name = config['github_actions']['user_name']
    user_email = config['github_actions']['user_email']
    branch = config['github_actions']['branch']
    repos = config['github_actions']['repos']

    # Example usage
    print(f"GitHub Actions User Name: {user_name}")
    print(f"GitHub Actions User Email: {user_email}")
    print(f"Branch: {branch}")
    for repo in repos:
        print(f"Repository Name: {repo['name']}")
