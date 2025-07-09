import os
import cv2
import numpy as np
import pandas as pd

def detect_border(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    
    # Find edges
    edges = cv2.Canny(gray, 50, 150)
    
    # Find first and last rows/columns with content
    rows_with_content = np.any(edges, axis=1)
    cols_with_content = np.any(edges, axis=0)
    
    # Find content boundaries
    top = np.argmax(rows_with_content) if np.any(rows_with_content) else 0
    bottom = h - np.argmax(rows_with_content[::-1]) if np.any(rows_with_content) else h
    left = np.argmax(cols_with_content) if np.any(cols_with_content) else 0
    right = w - np.argmax(cols_with_content[::-1]) if np.any(cols_with_content) else w
    
    # Calculate border sizes
    top_border = top
    bottom_border = h - bottom
    left_border = left
    right_border = w - right
    
    # Determine which borders exist (minimum 5px)
    borders = []
    if top_border > 5:
        borders.append('top')
    if bottom_border > 5:
        borders.append('bottom')
    if left_border > 5:
        borders.append('left')
    if right_border > 5:
        borders.append('right')
    
    return {
        'filename': os.path.basename(image_path),
        'width': w,
        'height': h,
        'top_border': top_border,
        'bottom_border': bottom_border,
        'left_border': left_border,
        'right_border': right_border,
        'border_width': max(left_border, right_border),
        'border_height': max(top_border, bottom_border),
        'borders_found': ', '.join(borders) if borders else 'none'
    }

def main():
    input_dir = 'input'
    results = []
    
    # Process all images
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        result = detect_border(filepath)
        if result:
            results.append(result)
            print(f"Processed: {filename}")

        df = pd.DataFrame(results)
        df.to_csv('new_border_results.csv',index=False)
        print("Results saved to border_results.csv")


if __name__ == "__main__":
    main()

