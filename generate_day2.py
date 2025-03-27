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

# Locations and routes for mapping
locations = {
    "10am": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan",  # Airbnb
    "1015am": "Shinjuku Gyoen, 11 Naitomachi, Shinjuku-ku, Tokyo",       # Shinjuku Gyoen Okido Gate
    "1115am": "Himawari Sushi Okubo, 1-16-16 Okubo, Shinjuku-ku, Tokyo", # Himawari Sushi
    "1215pm": "Meiji Jingu, 1-1 Yoyogikamizonocho, Shibuya-ku, Tokyo",   # Meiji Shrine
    "1pm": "Tokyo Station, 1-9-1 Marunouchi, Chiyoda-ku, Tokyo",         # Edo Castle via Tokyo Station
    "230pm": "Roppongi Hills Mori Tower, 6-10-1 Roppongi, Minato-ku, Tokyo", # Mori Tower
    "5pm": "teamLab Borderless, Azabudai Hills, 1-2-4 Azabudai, Minato-ku, Tokyo", # teamLab
    "730pm": "Sushi Tokyo Ten, 1-3-10 Azabudai, Minato-ku, Tokyo",       # Sushi Tokyo Ten
    "9pm": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan"    # Back to Airbnb
}

routes = {
    "10am-1015am": ("walking", "Head southeast on Okubo-dori, turn right onto Meiji-dori, then left into Shinjuku Gyoen’s Okido Gate."),
    "1015am-1115am": ("walking", "Exit Shinjuku Gyoen’s Sendagaya Gate, head northwest on Meiji-dori, turn left onto Okubo-dori to Himawari Sushi."),
    "1115am-1215pm": ("walking", "Head south on Okubo-dori, turn right onto Meiji-dori, pass Takeshita Street, enter Meiji Jingu via torii gates.", "Takeshita Street, Harajuku, Tokyo"),
    "1215pm-1pm": ("transit", "Walk to Harajuku Station (5 min), take JR Yamanote Line to Tokyo Station (15 min)."),
    "1pm-230pm": ("transit", "From Tokyo Station, take JR Yamanote to Shibuya (10 min), transfer to Hibiya Line to Roppongi (10 min), walk 500m."),
    "230pm-5pm": ("walking", "Head west on Roppongi-dori, turn left onto Azabudai-dori, reach teamLab Borderless."),
    "5pm-730pm": ("walking", "Walk south on Azabudai-dori, turn right onto a side street to Sushi Tokyo Ten."),
    "730pm-9pm": ("transit", "Walk to Roppongi Station (10 min), take Hibiya Line to Hibiya (15 min), transfer to JR Yamanote to Shin-Okubo (10 min), walk 300m.")
}

# Generate main day2.html
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
            waypoint = route_info[2] if len(route_info) > 2 else None
            origin = locations[prev_time].replace(" ", "+")
            destination = locations[time].replace(" ", "+")
            waypoints = f"&waypoints={waypoint.replace(' ', '+')}" if waypoint else ""
            substop_note = " (via Harajuku Peek)" if waypoint else ""
            maps_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}{waypoints}&travelmode={mode}&hl=en"
            main_content += f'<br><a href="{maps_url}" target="_blank">Route from {prev_time.replace("am", " AM").replace("pm", " PM")}</a>{substop_note}: {directions}'
    
    # Add sub-stops
    for key, value in sections.items():
        if key.startswith("substop_"):
            substop_name = key.split("_")[1]
            main_content += f'<br>Sub-Stop: {substop_name.capitalize()} (10 min) - {value} [<a href="{time}_{substop_name}.html">Details</a>]'
            if substop_name == "teahouse":
                main_content += ' (Inside Shinjuku Gyoen)'
            elif substop_name == "spider":
                main_content += ' (At Mori Garden)'
    main_content += '</li></ul></li>'
    prev_time = time
main_content += '</ul>\n<p><a href="../japan_main.html">Back to Main Itinerary</a></p>'
with open('day2/day2.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Day 2 Overview", header="Day 2 (04/01/25): Jet Lag Ease-In with Hanami, History, and teamLab", content=main_content))

# Generate subpages
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    time_display = time.replace("am", " AM").replace("pm", " PM")
    base_parts = sections["base"].split("—")[0].strip().split(")")
    stop_name = base_parts[0].strip() + ")" if len(base_parts) > 1 else base_parts[0].strip()
    header = f"{time_display} - {stop_name}"
    for section, content in sections.items():
        if section in ["base", "short_story", "long_story", "facts"]:
            content_html = f'<p>{content.replace("\n", "<br>")}</p>'
            filename = f'day2/{time}_{section}.html'
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
            if "walk" in sections and section == "train":  # For stops with both (e.g., 1pm, 230pm, 9pm)
                content_html += f'<p>{sections["walk"]}</p>'
                if "places" in sections:
                    content_html += '<ul>' + "".join(f'<li>{place.replace("\n", "<br>")}</li>' for place in sections["places"]) + '</ul>'
            filename = f'day2/{time}_travel.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time_display} Travel',
                    header=f'Travel: {header}',
                    content=content_html
                ))
        elif section == "places" or section == "train_places":
            continue  # Handled in travel page
        elif section.startswith("substop_"):
            substop_name = section.split("_")[1]
            filename = f'day2/{time}_{substop_name}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(template.format(
                    title=f'{time_display} {substop_name.capitalize()}',
                    header=f'Sub-Stop: {substop_name.capitalize()} (10 min)',
                    content=f'<p>{content}</p>'
                ))