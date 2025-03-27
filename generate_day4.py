import json
import os

# Load JSON data with UTF-8 encoding
with open('day4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create day4 folder if it doesn't exist
os.makedirs('day4', exist_ok=True)

# HTML template with enhanced styling
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 4 - {title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; margin-top: 20px; }}
        h3 {{ color: #7f8c8d; margin-top: 15px; }}
        li strong.top-level {{ font-size: 1.2em; }}
        ul {{ margin-left: 20px; padding-left: 0; list-style-type: square; }}
        li {{ margin-bottom: 10px; }}
        p {{ margin: 15px 0; }}
        strong {{ color: #e74c3c; }}
    </style>
</head>
<body>
    <h1>{header}</h1>
    {content}
    <p><a href="../japan_main.html">Back to Main Itinerary</a></p>
</body>
</html>'''

# Function to generate HTML from nested content
def generate_content_html(content, level=0):
    html = ""
    if isinstance(content, str):  # Plain text sections (e.g., intro, final_take)
        html += f'<p>{content}</p>'
    elif isinstance(content, list):  # Lists (e.g., intro, steps)
        html += '<ul>'
        for item in content:
            if isinstance(item, dict):
                if "label" in item and "text" in item:
                    html += f'<li><strong>{item["label"]}:</strong> {item["text"]}'
                    if "subitems" in item:
                        html += generate_content_html(item["subitems"])
                    elif "options" in item or "steps" in item or "plan" in item:
                        html += generate_content_html(item.get("options") or item.get("steps") or item.get("plan"))
                    html += '</li>'
                elif "text" in item:
                    html += f'<li>{item["text"]}</li>'
                elif "title" in item and "description" in item:  # Attractions
                    html += f'<h3>{item["title"]}</h3><p>{item["description"]}</p>'
                elif "title" in item:  # Steps
                    html += generate_content_html(item)
            else:
                html += f'<li>{item}</li>'  # Plain string in list
        html += '</ul>'
    elif isinstance(content, dict):  # Nested sections (e.g., steps, attractions)
        for key, value in content.items():
            if key == "title":
                html += f'<h{2 if level == 0 else 3}>{value}</h{2 if level == 0 else 3}>'
            elif key in ["intro", "pros", "cons", "yes", "no", "recommendation"] and isinstance(value, str):
                if key in ["pros", "yes", "cons", "no"]:
                    html += f'<p><strong>{"Pros" if key == "pros" else "Yes, If" if key == "yes" else "Cons" if key == "cons" else "No, If"}:</strong> {value}</p>'
                else:
                    html += f'<p>{value}</p>'
            elif key in ["steps", "details", "cost_breakdown", "timing_example", "time", "tips", "options", "plan"]:
                html += generate_content_html(value, level + 1)
            elif key == "items":  # Attractions list
                html += generate_content_html(value, level + 1)
            elif key == "attractions" or key == "fit" or key == "must_see" or key == "sense":
                html += generate_content_html(value, level + 1)
    return html

# Generate main day4.html
main_content = '<ul>'
for key, section in data["overview"].items():
    file_name = key.replace("_", "-")
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
    file_name = key.replace("_", "-")
    content_html = generate_content_html(section["content"])
    with open(f'day4/{file_name}.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            title=f'Day 4 - {section["title"]}',
            header=f'{section["title"]}: {section["description"]}',
            content=content_html
        ))