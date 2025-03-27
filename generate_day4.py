import json
import os

# Load JSON data with UTF-8 encoding
with open('day4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create day4 folder if it doesn't exist
os.makedirs('day4', exist_ok=True)

# HTML template
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 4 - {title}</title>
    <style>
        li strong.top-level {{ font-size: 1.2em; }}
    </style>
</head>
<body>
    <h1>{header}</h1>
    {content}
    <p><a href="../japan_main.html">Back to Main Itinerary</a></p>
</body>
</html>'''

# Generate main day4.html
main_content = '<ul>'
for key, section in data["overview"].items():
    file_name = key.replace("_", "-")  # e.g., "route_overview" -> "route-overview"
    main_content += f'<li><strong class="top-level">{section["title"]}:</strong> {section["description"]} [<a href="{file_name}.html">Details</a>]</li>'
main_content += '</ul>'
with open('day4/day4.html', 'w', encoding='utf-8') as f:
    f.write(template.format(
        title="Day 4 Overview",
        header="Day 4 (04/03/25): Travel to Ryuguden, Hakone",
        content=main_content
    ))

# Generate subpages
for key, section in data["overview"].items():
    file_name = key.replace("_", "-")  # e.g., "route_overview" -> "route-overview"
    content_html = section["content"].replace("\n", "<br>").replace("<br><br>", "</p><p>").replace("### ", "<h2>").replace("</h2>", "</h2><p>").replace("#### ", "<h3>").replace("</h3>", "</h3><p>")
    content_html = f'<p>{content_html}</p>'
    with open(f'day4/{file_name}.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            title=f'Day 4 - {section["title"]}',
            header=f'{section["title"]}: {section["description"]}',
            content=content_html
        ))