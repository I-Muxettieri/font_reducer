# Font reducer

Small script to reduce font size by keeping only selected glyph ranges.

## Requirements

- fontTools
- Pyhton

## Usage

Make sure you have font forge in PATH.

Run the script:

```bash
  python font_reducer.py <folder_name>
```

where the folder name is the folder that contains all the fonts you want to reduce.

The script create another folder named "reduced_font" with the output.
