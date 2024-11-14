import json
from bs4 import BeautifulSoup
from datetime import datetime
import os
import sys

def format_timestamp(ts):
    """Converts a timestamp to a human-readable format."""
    return datetime.fromtimestamp(ts / 1000).strftime('%A, %B %d, %Y at %I:%M %p')

def generate_html(messages, media_directory):
    """Generates a complete HTML file with messages, a header, and relative media paths."""
    soup = BeautifulSoup("<html><head></head><body></body></html>", 'html.parser')

    title_tag = soup.new_tag("title")
    title_tag.string = "Message Viewer"
    soup.head.append(title_tag)

    style_tag = soup.new_tag("style")
    style_tag.string = """
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
            padding: 0;
        }
        .header {
            background-color: #3578E5;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
        .message-container {
            width: 60%;
            margin: 0 auto;
        }
        .message-window {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
            background-color: #ffffff;
        }
        .sender-name {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .timestamp {
            color: gray;
            font-size: small;
            margin-top: 5px;
        }
        img {
            max-width: 50%;
            height: auto;
            display: block;
            margin: 5px 0;
        }
    """
    soup.head.append(style_tag)

    header_div = soup.new_tag("div", attrs={"class": "header"})
    gen_time = datetime.now().strftime('%A, %B %d, %Y at %I:%M %p UTC-05:00')
    header_div.append(f"Generated on {gen_time}")
    soup.body.append(header_div)

    main_container = soup.new_tag("div", attrs={"class": "message-container"})
    soup.body.append(main_container)

    for message in messages:
        msg_div = soup.new_tag("div", attrs={"class": "message-window"})

        sender_div = soup.new_tag("div", attrs={"class": "sender-name"})
        sender_div.string = message.get("senderName", "Unknown")
        msg_div.append(sender_div)

        if message["type"] == "text":
            text_div = soup.new_tag("p")
            text_div.string = message.get("text", "")
            msg_div.append(text_div)
        elif message["type"] == "media" and message.get("media"):
            for media in message["media"]:
                relative_path = os.path.join(media_directory, media["uri"].split('./media/')[-1])
                media_tag = soup.new_tag("img", src=relative_path)
                msg_div.append(media_tag)

        timestamp = format_timestamp(message.get("timestamp", 0))
        timestamp_div = soup.new_tag("div", attrs={"class": "timestamp"})
        timestamp_div.string = timestamp
        msg_div.append(timestamp_div)

        main_container.append(msg_div)

    return str(soup)

def main():
    """Main function to process the JSON and generate the HTML file."""
    if len(sys.argv) != 4:
        print("Usage: python script.py [path_json] [media_path] [output]")
        sys.exit(1)

    json_path = sys.argv[1]
    media_directory = sys.argv[2]
    output_html_path = sys.argv[3]

    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as f:
        message_data = json.load(f)

    # Generate the new HTML with relative paths and styled message windows
    new_html = generate_html(message_data["messages"], media_directory)

    # Save the generated HTML
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"HTML generated at: {output_html_path}")

if __name__ == "__main__":
    main()
