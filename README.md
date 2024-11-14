# FacebookMessengerE2EE_JSON_Convertor

After Facebook transitioned to End-to-End Encrypted (E2EE) chats, message data is now stored in JSON format. Previously, you could download your messages in an easy-to-read HTML format. This tool converts the new E2EE JSON data back into a readable HTML format, similar to the old style.

## Prerequisites

Make sure you have the following installed:
- Python 3.x
- `beautifulsoup4` (for parsing and generating HTML)

You can install `beautifulsoup4` via pip:

```bash
pip install beautifulsoup4
```

## How to Download Your E2EE Messages

1. Open your Facebook app or website.
2. Navigate to:  
   **Messenger Icon** → **Privacy & Safety** → **End-to-End Encrypted Chats**.
3. Select **Download secured storage data** → **Download file**.
4. This will provide a ZIP file containing all your E2EE messages and associated media.

## How to Run

To convert your E2EE JSON data to an easy-to-read HTML format:

```bash
python FacebookMessengerE2EE_JSON_Convertor.py [path_to_json] [path_to_media] [output_location]
```

### Parameters:
- `path_to_json`: The path to the `messages.json` file extracted from the downloaded ZIP.
- `path_to_media`: The path to the media folder within the extracted ZIP.
- `output_location`: The desired output path for the generated HTML file.

### Example:
```bash
python FacebookMessengerE2EE_JSON_Convertor.py ./messages.json ./media ./output.html
```

## Features

- **Readable HTML Output**: Converts E2EE JSON to HTML with a clean layout.
- **Media Support**: Images and other media are embedded from the media folder.
- **Preserves Timestamps**: Displays accurate message timestamps.
