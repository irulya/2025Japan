import json
import os

# Load JSON data with UTF-8 encoding
with open('day3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create day3 folder if it doesn't exist
os.makedirs('day3', exist_ok=True)

# HTML template
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 3 - {title}</title>
    <style>
        li strong.top-level {{ font-size: 1.2em; }}
        li strong.second-level {{ font-size: 1.0em; }}
    </style>
</head>
<body>
    <h1>{header}</h1>
    {content}
    <p><a href="../day3/day3.html">Back to Day 3</a></p>
</body>
</html>'''

# Locations and routes for mapping
locations = {
    "930am": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan",  # Airbnb
    "10am": "Tokyo Skytree, 1-1-2 Oshiage, Sumida-ku, Tokyo",            # Skytree
    "12pm": "Tsukiji Outer Market, 4-chome-16-2 Tsukiji, Chuo-ku, Tokyo", # Tsukiji
    "130pm": "Senso-ji Temple, 2-3-1 Asakusa, Taito-ku, Tokyo",          # Senso-ji
    "230pm": "Akihabara Electric Town, 1-1-1 Soto-Kanda, Chiyoda-ku, Tokyo", # Akihabara
    "4pm": "Takeshita Street, 1-chome Jingumae, Shibuya-ku, Tokyo",      # Takeshita
    "5pm": "Shibuya Crossing, 2-chome-2 Dogenzaka, Shibuya-ku, Tokyo",   # Shibuya Crossing
    "545pm": "Hachiko Statue, 2-chome-2 Dogenzaka, Shibuya-ku, Tokyo",   # Hachiko
    "615pm": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan"  # Back to Airbnb
}

routes = {
    "930am-10am": ("transit", "Walk to Shin-Okubo Station (5 min), take JR Sobu to Asakusa (25 min), transfer to Tobu to Oshiage (5 min)."),
    "10am-12pm": ("transit", "Take Tobu from Oshiage to Asakusa (5 min), transfer to Tsukuba Express to Tsukiji (15 min), walk 500m."),
    "12pm-130pm": ("transit", "Take Tsukuba Express from Tsukiji to Asakusa (10 min), walk 500m."),
    "130pm-230pm": ("walking", "Head southwest from Senso-ji, cross Kanda River, enter Akihabara’s Electric Town."),
    "230pm-4pm": ("transit", "Walk to Akihabara Station (5 min), take JR Chuo-Sobu to Yoyogi (10 min), walk 1 km."),
    "4pm-5pm": ("walking", "Head south on Meiji-dori from Takeshita Street, reach Shibuya Crossing."),
    "5pm-545pm": ("walking", "Walk 100m southeast from Shibuya Crossing to Hachiko Statue."),
    "545pm-615pm": ("transit", "Walk to Shibuya Station (5 min), take JR Yamanote to Shin-Okubo (10 min), walk 300m.")
}

# Generate main day3.html
main_content = '<ul>'
main_content += f'<li><strong class="top-level">Overview:</strong> {data["overview"]}</li>'
prev_time = None
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    time_display = time.replace("am", " AM").replace("pm", " PM")
    base_parts = sections["base"].split("—")[0].strip().split(")")
    stop_name = base_parts[0].strip() + ")" if len(base_parts) > 1 else base_parts[0].strip()
    header = f"{time_display} - {stop_name}"
    main_content += f'<li><strong class="top-level">{header}:</strong>\n<ul>'
    main_content += f'<li><strong class="second-level">Base:</strong> {sections["base"].replace("\n", "<br>")}<br>'
    main_content += f'[<a href="{time}_short_story.html">Short Story</a>] [<a href="{time}_long_story.html">Long Story</a>] '
    main_content += f'[<a href="{time}_facts.html">Facts</a>] [<a href="{time}_travel.html">Travel</a>]'
    
    # Add Google Maps link if not the first stop
    if prev_time:
        route_key = f"{prev_time}-{time}"
        if route_key in routes:
            route_info = routes[route_key]
            mode = route_info[0]
            directions = route_info[1]
            origin = locations[prev_time].replace(" ", "+")
            destination = locations[time].replace(" ", "+")
            maps_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode={mode}&hl=en"
            main_content += f'<br><a href="{maps_url}" target="_blank">Route from {prev_time.replace("am", " AM").replace("pm", " PM")}</a>: {directions}'
    
    main_content += '</li></ul></li>'
    prev_time = time
main_content += '</ul>\n<p><a href="../japan_main.html">Back to Main Itinerary</a></p>'
with open('day3/day3.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Day 3 Overview", header="Day 3 (04/02/25): Skytree Heights, Eastern Culture, and Shibuya Soul", content=main_content))

# Generate subpages
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    time_display = time.replace("am", " AM").replace("pm", " PM")
    base_parts = sections["base"].split("—")[0].strip().split(")")
    stop_name = base_parts[0].strip() + ")" if len(base_parts) > 1 else base_parts[0].strip()
    header = f"{time_display} - {stop_name}"
    for section, content in sections.items():
        if section in ["base", "short_story", "long_story", "facts"]:
            content_html = f'<p>{content.replace("\n", "<br>")}</p>'
            filename = f'day3/{time}_{section}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time_display} {section.replace("_", " ").title()}',
                    header=f'{section.replace("_", " ").title()}: {header}',
                    content=content_html
                ))
        elif section in ["walk", "train"]:
            content_html = f'<p>{content}</p>'
            if section == "train" and "train_places" in sections:
                content_html += '<ul>' + "".join(f'<li>{place.replace("\n", "<br>")}</li>' for place in sections["train_places"]) + '</ul>'
            if section == "walk" and "places" in sections:
                content_html += '<ul>' + "".join(f'<li>{place.replace("\n", "<br>")}</li>' for place in sections["places"]) + '</ul>'
            if "walk" in sections and section == "train":  # For stops with both
                content_html += f'<p>{sections["walk"]}</p>'
                if "places" in sections:
                    content_html += '<ul>' + "".join(f'<li>{place.replace("\n", "<br>")}</li>' for place in sections["places"]) + '</ul>'
            filename = f'day3/{time}_travel.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time_display} Travel',
                    header=f'Travel: {header}',
                    content=content_html
                ))
        elif section == "places" or section == "train_places":
            continue  # Handled in travel page