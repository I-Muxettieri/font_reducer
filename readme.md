
# Font reducer

Small script for reduce font size only mantaining selected glyph ranges


## Requirements

- Fontforge
- Pyhton



## Usage
Make sure you have font forge in PATH

Run the script

```bash
  fontforge -script font_reducer.py <folder_name>
```

where the folder name is the folder that contains all the fonts you want to reduce.

The script create another folder named "reduced_font" with the output

