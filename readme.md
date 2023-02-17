lang PV_DB Translation Generation Tool
==================

## Requirements
1. Python 3.8+
2. PV_DB with lyric_en and lyric_new fields. Easiest to combine new lyrics with Notepad++ and then use Edit > Line Operations > Sort Lines Lexicographically Ascending
3. pyo3 branch of https://github.com/diva-rust-modding/serde_divatree/ -> Used as a library for this project

## Tools
#### generate_translation_db
 ##### Usage
 - Place your edited pv_db.txt in this folder. When running the script, select this PV DB in the tool. 
 - The tool will ask for a name for your new lang translation array.
 - Wait for a little bit. The script should output everything into the toml once done.
 ##### Notes
 - The tool does not handle special characters that must be escaped very well. It has basic handling. Take your toml and then lint it with addons inside Visual Studio Code.
 - Afterwards, you must open your toml and add enabled = true to the top. I might fix this soon.


## Development Info
No license. Do whatever you want, and I'm always open to additions or commmits to fix my terrible code.