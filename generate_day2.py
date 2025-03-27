import json
import os

# Load JSON data with UTF-8 encoding
with open('day2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create day2 folder if it doesn't exist
os.makedirs('day2', exist_ok=True)

# HTML template
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 2 - {title}</title>
    <style>
        li strong.top-level {{ font-size: 1.2em; }}
        li strong.second-level {{ font-size: 1.0em; }}
    </style>
</head>
<body>
    <h1>{header}</h1>
    {content}
    <p><a href="../day2/day2.html">Back to Day 2</a></p>
</body>
</html>'''

# Generate main day2.html
main_content = '<h1>Day 2 (04/01/25): Jet Lag Ease-In with Hanami, History, and teamLab</h1>\n<ul>'
main_content += f'<li><strong class="top-level">Overview:</strong> {data["overview"]}</li>'
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    main_content += f'<li><strong class="top-level">{time.replace("am", " AM").replace("pm", " PM")} - {time.upper()}:</strong>\n<ul>'
    main_content += f'<li><strong class="second-level">Base:</strong> {sections["base"].replace("\n", "<br>")}<br>'
    main_content += f'[<a href="{time}_short_story.html">Short Story</a>] [<a href="{time}_long_story.html">Long Story</a>] '
    main_content += f'[<a href="{time}_facts.html">Facts</a>] [<a href="{time}_places.html">Places</a>]'
    for key, value in sections.items():
        if key.startswith("substop_"):
            substop_name = key.split("_")[1]
            main_content += f'<br>Sub-Stop: {substop_name.capitalize()} (10 min) - {value} [<a href="{time}_{substop_name}.html">Details</a>]'
    main_content += '</li></ul></li>'
main_content += '</ul>\n<p><a href="../japan_main.html">Back to Main Itinerary</a></p>'
with open('day2/day2.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Day 2 Overview", header="Day 2 (04/01/25): Jet Lag Ease-In with Hanami, History, and teamLab", content=main_content))

# Generate subpages
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    for section, content in sections.items():
        if section in ["base", "short_story", "long_story", "facts", "places"]:
            if section == "facts" or section == "places":
                content_html = f'<ul>{"".join(f"<li>{line}</li>" for line in content.split("\n"))}</ul>'
            else:
                content_html = f'<p>{content.replace("\n", "<br>")}</p>'
            filename = f'day2/{time}_{section}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time.replace("am", " AM").replace("pm", " PM")} {section.replace("_", " ").title()}',
                    header=f'{section.replace("_", " ").title()}: {time.replace("am", " AM").replace("pm", " PM")} - {time.upper()}',
                    content=content_html
                ))
        elif section.startswith("substop_"):
            substop_name = section.split("_")[1]
            filename = f'day2/{time}_{substop_name}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time.replace("am", " AM").replace("pm", " PM")} {substop_name.capitalize()}',
                    header=f'Sub-Stop: {substop_name.capitalize()} (10 min)',
                    content=f'<p>{content}</p>'
                ))