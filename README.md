# GCP Project and Folder Cleaner

This Python script deletes all projects and folders under a given parent folder in Google Cloud Platform (GCP). It uses the Google Cloud Resource Manager API to perform the deletion.

## Prerequisites

- **Install the Google Cloud Client Library for Python:**
  ```bash
  pip install google-cloud-resource-manager

- **Set up authentication:** This code uses your default GCP credentials. Make sure you have authenticated with your GCP account. You can use the `gcloud auth application-default login` command for this.

## Usage
### Run the script:
```Bash
python gcp_folder_cleaner.py --parent <parent_folder_id>
```
Replace `<parent_folder_id>` with the actual ID of your GCP parent folder.

### How it works
- The script takes the parent folder ID as a command-line argument.

- It uses the resourcemanager_v3 library to interact with the Resource Manager API.

- It recursively deletes projects and folders starting from the deepest level of the folder hierarchy.

- It deletes projects within each folder before deleting the folder itself.

- Finally, it deletes the parent folder.

### Warning
- This script **permanently deletes projects and folders**. Make absolutely sure you understand the consequences before running it.

- There is no undo. Once a project or folder is deleted, it cannot be recovered.

- Use with extreme caution. Always test this script in a non-production environment first.

### Disclaimer
This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any data loss or other damages that may result from using this script.   
