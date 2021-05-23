<<<<<<< HEAD
import os
from shutil import copy

# Récupération du chemin du dossier Téléchargements (ou Downloads)
down_dir = os.path.join (os.path.expanduser ("~"), "downloads")
down_dir = "%s\\" % (down_dir)
os.chdir(down_dir)

# Fonction renvoyant le chemin de folder
def fpath(folder):
    return os.path.join(down_dir, folder)

# Définition des extensions à trier
image_ext = [".png", ".jpg", ".jpeg", ".gif"]
video_ext = [".mp4", ".webm", ".avi"]
executable_ext = [".exe", ".msi"]
archive_ext = [".rar", ".zip"]
audio_ext = [".mp3", ".wav", ".aac", ".ogg"]
document_ext = [".PDF",".pdf", ".txt", ".html", ".doc", ".docx" ]

# Définition des dossiers où l'on rangera les fichiers
file_dir = [".Images", ".Videos", ".Executables", ".Archives", ".Audios", ".Documents"]

# Création des dossiers si ils n'éxistent pas encore
for dirr in file_dir:
    if not os.path.exists("%s%s\\" % (down_dir,dirr)):
        os.mkdir(dirr)

# Listage de tous les fichiers présents dans le dossier Téléchargement
file_list = []
for files in os.listdir(down_dir):
    if not files in file_dir:
        file_list.append(files)

# Fonction rangeant les fichier de certaines extensions dans les dossiers correspondants
def tidy_file(ext, dir):
    for files in file_list:
        if os.path.splitext(files)[1] in ext:
            copy(fpath(files), fpath(file_dir[file_dir.index(dir)]))
            os.remove(fpath(files))

tidy_file(image_ext, ".Images")
tidy_file(video_ext, ".Videos")
tidy_file(executable_ext, ".Executables")
tidy_file(archive_ext, ".Archives")
tidy_file(audio_ext, ".Audios")
=======
import os
from shutil import *
down_dir = os.path.join (os.path.expanduser ("~"), "downloads")
down_dir = "%s\\" % (down_dir)
os.chdir(down_dir)

def fpath(folder):
    return os.path.join(down_dir, folder)

image_ext = [".png", ".jpg", ".jpeg", ".gif"]
video_ext = [".mp4", ".webm", ".avi"]
executable_ext = [".exe", ".msi"]
archive_ext = [".rar", ".zip"]
audio_ext = [".mp3", ".wav", ".aac", ".ogg"]
document_ext = [".PDF",".pdf", ".txt", ".html", ".doc", ".docx" ]

file_dir = [".Images", ".Videos", ".Executables", ".Archives", ".Audios", ".Documents"]

for dirr in file_dir:
    if not os.path.exists("%s%s\\" % (down_dir,dirr)):
        os.mkdir(dirr)

file_list = []
for files in os.listdir(down_dir):
    if not files in file_dir:
        file_list.append(files)

def tidy_file(ext, dir):
    for files in file_list:
        if os.path.splitext(files)[1] in ext:
            copy(fpath(files), fpath(file_dir[file_dir.index(dir)]))
            os.remove(fpath(files))



tidy_file(image_ext, ".Images")
tidy_file(video_ext, ".Videos")
tidy_file(executable_ext, ".Executables")
tidy_file(archive_ext, ".Archives")
tidy_file(audio_ext, ".Audios")
>>>>>>> 731974ba4ebc0a731a0e205f32f92940b170db49
tidy_file(document_ext, ".Documents")