import argparse
from google.cloud import resourcemanager_v3


def delete_all_projects_and_folders(parent_folder_id):
    """
    Deletes all projects and folders under the given parent folder.

    Args:
        parent_folder_id: The ID of the parent folder.
    """

    client = resourcemanager_v3.FoldersClient()

    # Recursively delete projects and folders starting from the deepest level
    delete_projects_and_folders_recursively(client, parent_folder_id)

    # Finally, delete the parent folder
    delete_folder(client, parent_folder_id)


def delete_projects_and_folders_recursively(client, folder_id):
    """
    Recursively deletes projects and folders starting from the deepest level.

    Args:
        client: The FoldersClient object.
        folder_id: The ID of the folder to be deleted.
    """
    page_result = client.list_folders(parent=folder_id)
    for response in page_result:
        delete_projects_and_folders_recursively(client, response.name)

    # Delete projects in the current folder
    delete_projects_in_folder(folder_id)

    # Delete the folder if it has no subfolders
    delete_folder(client, folder_id)


def delete_projects_in_folder(folder_id):
    """
    Deletes all projects in the given folder.

    Args:
        folder_id: The ID of the folder.
    """
    client = resourcemanager_v3.ProjectsClient()

    # Initialize request argument(s)
    request = resourcemanager_v3.ListProjectsRequest(
        parent=folder_id,
    )

    # Make the request
    project_list = client.list_projects(request=request)
    # project_list = client.search_projects(query=f"parent.id:{folder_id}")
    for project in project_list:
        try:
            operation = client.delete_project(name=project.name)
            print(f"Waiting for deleting {project.name} to complete...")
        except Exception as e:
            print(f"Error deleting project {project.name}: {e}")
        operation.result()
        print(f"Delete {project.name} requested successfully.")


def delete_folder(client, folder_id):
    """
    Deletes a folder.

    Args:
        client: The FoldersClient object.
        folder_id: The ID of the folder to be deleted.
    """
    try:
        client.delete_folder(name=folder_id)
        print(f"Folder {folder_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting folder {folder_id}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", required=True, type=str)
    args = parser.parse_args()
    parent_folder_id = args.parent
    delete_all_projects_and_folders(parent_folder_id)
