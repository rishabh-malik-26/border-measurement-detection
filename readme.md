# Border Detection and Removal Tools

A collection of Python scripts for automatically detecting and removing borders/frames from images.

## Features

- **Border Detection**: Analyze images to detect border dimensions and locations
- **Border Removal**: Automatically crop borders from images while preserving content
- **Batch Processing**: Process entire directories of images at once
- **Detailed Reporting**: Generate CSV reports with border analysis results

## Requirements

```bash
pip install -r requirements.txt
```

## Scripts

### 1. Border Detection (`border_detector.py`)

Analyzes images to detect border dimensions and generates a detailed report.

#### Usage
```bash
python border_detector.py
```

#### Features
- Detects borders on all four sides (top, bottom, left, right)
- Calculates border width and height in pixels
- Generates CSV report with detailed measurements

#### Output
Creates `border_results.csv` with the following columns:
- `filename` - Image filename
- `width/height` - Original image dimensions
- `top_border/bottom_border/left_border/right_border` - Border size on each side
- `border_width/border_height` - Maximum border dimensions
- `borders_found` - Which sides have borders detected

### 2. Border Removal (`border_remover.py`)

Automatically detects and removes borders from images, saving cropped versions.

#### Usage
```bash
python border_remover.py
```

#### Features
- Automatically detects content boundaries
- Crops borders while preserving image content
- Adds small padding to avoid cutting important content
- Skips files that already exist in output directory
- Preserves original filenames

## Directory Structure

```
your-project/
├── input/          # Images that require border removal
├── output/         # Cropped images are saved here
├── border_detector.py
├── border_remover.py
└── border_results.csv  # Generated after running detection
```

## How It Works

Both scripts use OpenCV's edge detection to identify where image content begins and ends:

1. **Edge Detection**: Uses Canny edge detection to find content boundaries
2. **Image Analysis**: Identifies the main content area within the image
3. **Border Calculation**: Measures the space between image edges and content
4. **Processing**: Either reports measurements or crops the borders

## Example Workflow

1. **Setup**: Place images in the `input/` directory
2. **Analyze**: Run `border_detector.py` to see border measurements
3. **Remove**: Run `border_remover.py` to crop borders from images
4. **Results**: Check `output/` folder for cropped images and `border_results.csv` for analysis


## Configuration

Both scripts can be easily modified:
- Change input/output directories by editing the `input_dir` and `output_dir` variables
- Adjust minimum border size threshold (default: 5 pixels)
- Modify edge detection parameters for different image types

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)

## Error Handling

- Skips corrupted or unreadable images
- Creates output directory automatically
- Provides detailed console feedback

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Pull requests welcome! Please ensure your code follows the existing style and includes appropriate error handling.
