
import os
from dotenv import load_dotenv
from github_agent import GitHubAgent

def main():
    load_dotenv()
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")

    agent = GitHubAgent(github_token)
    
    # Example usage
    repo_owner = "octocat"
    repo_name = "Hello-World"
    
    # List issues
    issues = agent.list_issues(repo_owner, repo_name)
    print(f"Current issues in {repo_owner}/{repo_name}:")
    for issue in issues:
        print(f"- {issue['title']} (#{issue['number']})")
    
    # Create a new issue
    new_issue = agent.create_issue(
        repo_owner,
        repo_name,
        title="Test issue from GitHub Agent",
        body="This is a test issue created by the GitHub Issue Agent.",
        labels=["bug", "automated"]
    )
    print(f"Created new issue: {new_issue['title']} (#{new_issue['number']})")

if __name__ == "__main__":
    main()
