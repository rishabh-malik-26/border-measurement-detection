import os
import cv2
import numpy as np

def remove_borders(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    
    # Find edges
    edges = cv2.Canny(gray, 50, 150)
    
    # Find content boundaries
    rows_with_content = np.any(edges, axis=1)
    cols_with_content = np.any(edges, axis=0)
    
    if not np.any(rows_with_content) or not np.any(cols_with_content):
        return img  # No borders detected, return original
    
    # Find crop boundaries
    top = np.argmax(rows_with_content)
    bottom = len(rows_with_content) - np.argmax(rows_with_content[::-1])
    left = np.argmax(cols_with_content)
    right = len(cols_with_content) - np.argmax(cols_with_content[::-1])
    
    # Add small padding to avoid cutting content
    padding = 5
    top = max(0, top - padding)
    left = max(0, left - padding)
    bottom = min(h, bottom + padding)
    right = min(w, right + padding)
    
    # Crop the image
    cropped = img[top:bottom, left:right]
    return cropped

def main():
    input_dir = 'input'
    output_dir = 'output'
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    processed = 0
    
    # Process all images
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
            
        try:
            cropped_image = remove_borders(input_path)
            if cropped_image is not None:
                cv2.imwrite(output_path, cropped_image)
                processed += 1
                print(f"Processed: {filename}")
            else:
                print(f"Failed: {filename}")
        except Exception as e:
            print(f"Error with {filename}: {e}")
    print(f"{processed} images")

if __name__ == "__main__":
    main()


