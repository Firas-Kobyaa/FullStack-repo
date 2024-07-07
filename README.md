This repository uses GitHub Actions to automate the synchronization of submodules between Front-repo, Back-repo, and FullStack-repo. Here’s how it works:

    Trigger: The workflow is triggered by a push event to the main branch or changes in the Front-repo and Back-repo directories.
    Checkout Repositories: It checks out the FullStack-repo and initializes its submodules.
    Pull Updates: It pulls the latest changes from the main branch of Front-repo and Back-repo.
    Add Changes: Any updates in the submodules are added to the staging area.
    Commit and Push: The workflow commits these changes with a predefined message and pushes them back to the main branch of FullStack-repo.

The workflow ensures that FullStack-repo remains up-to-date with the latest changes from its submodules.