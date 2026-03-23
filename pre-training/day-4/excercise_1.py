import sys
from fetch_utils import fetch

GITHUB_HEADERS = {
        'User-Agent': 'Python-Requests-Script',
        'Accept': 'application/vnd.github+json'
    }

def print_github_summary(user):
    print("\n📄 GitHub Profile Summary\n")

    print(f"{'Username':<15}: {user['username']}")
    print(f"{'Bio':<15}: {user['bio']}")
    print(f"{'Public Repos':<15}: {user['public_repos']}")
    print(f"{'Followers':<15}: {user['followers']}")

    print("\nTop 5 Repositories:")
    print("-" * 55)
    print(f"{'#':<3} {'Name':<20} {'Stars':<7} {'Language'}")

    for i, repo in enumerate(user["top_repos"], start=1):
        print(f"{i:<3} {repo['name']:<20} {repo['stars']:<7} {repo['language']}")


def get_repo_info(repo_json):
    top_5 = sorted(repo_json, key=lambda r: r["stargazers_count"], reverse=True)[:5]
    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"] or "N/A"
        }
        for repo in top_5
    ]

def get_user_profile(username):
    return fetch(f"https://api.github.com/users/{username}", GITHUB_HEADERS)


def get_user_repos(repos_url):
    return fetch(repos_url, GITHUB_HEADERS)

def get_user_data(username):
    profile = get_user_profile(username)

    if not profile:
        raise RuntimeError("Failed to fetch profile")

    repos = get_user_repos(profile["repos_url"])

    if not repos:
        raise RuntimeError("Failed to fetch repos")

    return profile, repos


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else "sindresorhus"

    try:
        profile, repos = get_user_data(username)
        top_repos = get_repo_info(repos)

        final_user_json = {
            "username": profile["login"],
            "bio": profile["bio"] or "N/A",
            "followers": profile["followers"],
            "public_repos": profile["public_repos"],
            "top_repos": top_repos,
        }

        print_github_summary(final_user_json)

    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()