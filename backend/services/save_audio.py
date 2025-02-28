import os
import shutil

def save_audio(file_path, output_dir="data/output/"):
    """Save the processed audio file to the output directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = os.path.basename(file_path)
    output_path = os.path.join(output_dir, file_name)
    shutil.move(file_path, output_path)
    return output_path
