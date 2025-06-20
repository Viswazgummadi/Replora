from git import Repo
import os
import shutil

def clone_github_repo(repo_url, clone_dir):
    """
    Clone a public GitHub repo into the specified local directory.
    If the directory exists, prompt to remove and re-clone.
    """
    if os.path.exists(clone_dir):
        print(f"⚠️ Directory '{clone_dir}' already exists.")
        choice = input("Do you want to remove it and clone fresh? (y/n): ").strip().lower()

        if choice == 'y':
            print(f"🧹 Removing '{clone_dir}'...")
            shutil.rmtree(clone_dir)
        else:
            print("⏩ Skipping clone.")
            return

    try:
        print(f"📥 Cloning from {repo_url} into {clone_dir}...")
        Repo.clone_from(repo_url, clone_dir)
        print("✅ Clone successful.")
    except Exception as e:
        print(f"❌ Error during clone: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with any public GitHub repo
    repo_url = "https://github.com/Viswazgummadi/p2p_lan_chat.git"
    clone_dir = "./temp-dir"

    clone_github_repo(repo_url, clone_dir)
