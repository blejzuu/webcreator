from operator import index
import os 

def create_folders_and_files(folder_name, location):
    # tworzenie glownego folderu z podana nazwa
    folder_path = os.path.join(location, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Tworzenie pliku index.html w głownym folderze
    index_html_path = os.path.join(folder_path, "index.html")
    with open(index_html_path, "w") as index_html_file:
        index_html_file.write(f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>blejzusz3f</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>""")
        
    # tworzenie folderu css w głównym folderze
        css_folder = os.path.join(folder_path, "css")
        os.makedirs(css_folder, exist_ok=True)

    # tworzenie pliku style.css w folderze "css"
    index_css_path = os.path.join(css_folder, "index.css")
    with open(index_css_path, "w") as index_css_file:
        index_css_file.write("body {}")

    # tworzenie folderu images w głównym folderze
        images_folder = os.path.join(folder_path, "images")
        os.makedirs(images_folder, exist_ok=True)

if __name__ == "__main__":
    folder_name = input("Podaj nazwę folderu docelowego:")
    location = input("Podaj lokalizację docelową w, której chcesz utworzyć foldery i pliki: ")
    create_folders_and_files(folder_name, location)
    print("Struktura folderu głównego i plików została poprawnie utworzona.")

        
