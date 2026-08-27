import os

project_folder = "my_website"  # Tera project folder
output_file = "project_output.txt"

def merge_files_to_txt():
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(project_folder):
            # Ignore unwanted folders
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv']]
            
            for file in files:
                if file.endswith(('.py', '.html', '.css', '.js', '.txt', '.env')):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_folder)
                    
                    out.write(f"\n{'='*60}\n")
                    out.write(f"📄 FILE: {relative_path}\n")
                    out.write(f"{'='*60}\n\n")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            out.write(f.read())
                        out.write("\n\n")
                    except Exception as e:
                        out.write(f"⚠️ Error reading file: {e}\n\n")
    
    print(f"✅ Saari files '{output_file}' mein merge ho gayin!")

if __name__ == "__main__":
    merge_files_to_txt()