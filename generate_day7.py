import json
import os

def generate_html(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{data["title"]}</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; }}
        .event {{ border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; }}
        .time {{ font-weight: bold; color: #333; }}
        .base {{ font-size: 1.2em; margin: 5px 0; }}
        .places {{ margin-left: 20px; }}
        .substop {{ margin-left: 20px; font-style: italic; }}
    </style>
</head>
<body>
    <h1>{data["title"]}</h1>
    <p><b>Date:</b> {data["day"]}</p>
    <p><b>Overview:</b> {data["overview"]}</p>
'''
    
    for time, details in data.items():
        if time in ["day", "title", "overview"]:
            continue
        html += '<div class="event">\n'
        html += f'    <span class="time">{time.replace("am", " AM").replace("pm", " PM")}</span>\n'
        html += f'    <div class="base">{details["base"]}</div>\n'
        html += f'    <p><b>Why It’s a Must-See:</b> {details["why_it’s_a_must_see"]}</p>\n'
        html += f'    <p><b>Short Story:</b> {details["short_story"]}</p>\n'
        html += f'    <p><b>Long Story:</b> {details["long_story"]}</p>\n'
        html += f'    <p><b>Facts:</b> {details["facts"].replace("\n", "<br>")}</p>\n'
        html += f'    <p><b>Walk:</b> {details["walk"]}</p>\n'
        if details["places"]:
            html += '    <div class="places"><b>Places:</b><ul>\n'
            for place in details["places"]:
                html += f'        <li>{place.replace("\n", "<br>")}</li>\n'
            html += '    </ul></div>\n'
        for key, value in details.items():
            if key.startswith("substop_"):
                substop_name = key.replace("substop_", "").replace("_", " ").title()
                html += f'    <div class="substop"><b>{substop_name}:</b> {value}</div>\n'
        html += '</div>\n'
    
    html += '''</body>
</html>'''
    
    os.makedirs('day7', exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

# Generate HTML for railway-museum.json
generate_html('railway-museum.json', 'day7/railway-museum.html')

# Placeholder for philosophers-path.json
stub_data = {
    "day": "Day 7 (04/06/25)",
    "title": "Kyoto with Philosopher’s Path",
    "overview": "Start 9:00 AM, end 6:00 PM (~9 hours), ~¥5,000 total.",
    "0900am": {
        "base": "TBD",
        "why_it’s_a_must_see": "TBD",
        "short_story": "TBD",
        "long_story": "TBD",
        "facts": "TBD",
        "walk": "TBD",
        "places": []
    }
}
with open('philosophers-path.json', 'w', encoding='utf-8') as f:
    json.dump(stub_data, f, indent=4)
generate_html('philosophers-path.json', 'day7/philosophers-path.html')