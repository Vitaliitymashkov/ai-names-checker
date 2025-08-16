from langchain.tools import tool
import os
import json

@tool
def list_files_in_directory(directory_path: str) -> str:
    """List all files in a directory with their extensions"""
    try:
        files = []
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)
                files.append(f"{file} ({ext})")
        
        if not files:
            return f"No files found in {directory_path}"
        
        return f"Files in {directory_path}:\n" + "\n".join(f"- {file}" for file in files)
    except Exception as e:
        return f"Error listing files in {directory_path}: {str(e)}"

@tool
def read_names_base_json(file_path: str) -> str:
    """Read names-base.json and return a list of people with their name combinations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Expecting a list of dicts with 'id' and 'names'
        people = []
        for person in data:
            person_id = person.get("id")
            names = person.get("names", [])
            people.append({"id": person_id, "names": names})
        return f"People in {file_path}:\n" + json.dumps(people, ensure_ascii=False, indent=2)
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"

@tool
def read_names_base_json2(file_path: str) -> str:
    """Read names-base.json and return a list of people with their name combinations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        people = data

        if isinstance(data, dict) and "data" in data:
            people = data["data"]
        else:
            people = data
        id_count = sum(1 for person in people if isinstance(person, dict) and person.get("id") is not None)
        print(f"Read {len(people)} people from {file_path}, {id_count} ids")
        return f"People in {file_path} ({id_count} ids):\n" + json.dumps(people, ensure_ascii=False, indent=2)[:50] + "[...50]..."
           
        ## print(f"Read {len(people)} people from {file_path}")
        ## return f"People in {file_path}:\n" + json.dumps(people, ensure_ascii=False, indent=2)
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"