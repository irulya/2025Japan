import json
import os

def generate_detail_page(content, output_file, title):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>{content.replace("\n", "<br>")}</p>
</body>
</html>'''
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

def generate_main_page(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{data["title"]}</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; }}
        .event {{ margin-bottom: 10px; }}
        .time {{ font-weight: bold; color: #333; }}
        .links {{ margin-left: 20px; }}
    </style>
</head>
<body>
    <h1>{data["title"]}</h1>
    <p><b>Date:</b> {data["day"]}</p>
    <p><b>Overview:</b> {data["overview"]}</p>
'''
    
    os.makedirs('day7', exist_ok=True)
    for time, details in data.items():
        if time in ["day", "title", "overview"]:
            continue
        time_str = time.replace("am", " AM").replace("pm", " PM")
        html += '<div class="event">\n'
        html += f'    <span class="time">{time_str}</span> - {details["base"]}<br>\n'
        html += f'    <b>Why It’s a Must-See:</b> {details["why_it’s_a_must_see"]}<br>\n'
        html += '    <div class="links">\n'
        html += f'        <a href="short_story_{time}.html">[Short Story]</a>\n'
        html += f'        <a href="long_story_{time}.html">[Long Story]</a>\n'
        html += f'        <a href="facts_{time}.html">[Facts]</a>\n'
        html += f'        <a href="travel_{time}.html">[Travel]</a>\n'
        route_url = details["walk"].split("Route: ")[-1]
        html += f'        <a href="{route_url}?hl=en" target="_blank">Route from {time_str}</a>\n'
        html += '    </div>\n'
        for key, value in details.items():
            if key.startswith("substop_"):
                substop_name = key.replace("substop_", "").replace("_", " ").title()
                html += f'    <div><i>{substop_name}: {value}</i></div>\n'
        html += '</div>\n'
        
        generate_detail_page(details["short_story"], f'day7/short_story_{time}.html', f'Short Story - {time_str}')
        generate_detail_page(details["long_story"], f'day7/long_story_{time}.html', f'Long Story - {time_str}')
        generate_detail_page(details["facts"], f'day7/facts_{time}.html', f'Facts - {time_str}')
        generate_detail_page(details["walk"], f'day7/travel_{time}.html', f'Travel - {time_str}')
    
    html += '''</body>
</html>'''
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

# Generate for railway-museum.json
generate_main_page('railway-museum.json', 'day7/railway-museum.html')

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
generate_main_page('philosophers-path.json', 'day7/philosophers-path.html')