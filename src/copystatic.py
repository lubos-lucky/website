import os
import shutil



def copy_static_to_public(src = None, dst = None):
    if src is None:
        src = os.path.join("./static")
    if dst is None:
        dst = os.path.join("./public")
    directories = [os.path.join(src, d) for d in os.listdir(src)]
    
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory '{src}' does not exist.")
    os.makedirs(dst, exist_ok=True)
    
    for directory in directories:
        if os.path.isdir(directory):
            
            copy_static_to_public(directory, os.path.join(dst, os.path.basename(directory)))
        else:
             shutil.copy(directory, os.path.join(dst, os.path.basename(directory)))
    

    