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

# Locations for mapping (simplified addresses based on your itinerary)
locations = {
    "10am": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan",  # Airbnb
    "1015am": "Shinjuku Gyoen, 11 Naitomachi, Shinjuku-ku, Tokyo",       # Shinjuku Gyoen
    "1115am": "Himawari Sushi Okubo, 1-16-16 Okubo, Shinjuku-ku, Tokyo", # Himawari Sushi (approx.)
    "1215pm": "Meiji Jingu, 1-1 Yoyogikamizonocho, Shibuya-ku, Tokyo",   # Meiji Shrine
    "1pm": "Edo Castle East Gardens, 1-1 Chiyoda, Chiyoda-ku, Tokyo",    # Edo Castle Gardens
    "230pm": "Roppongi Hills Mori Tower, 6-10-1 Roppongi, Minato-ku, Tokyo", # Mori Tower
    "5pm": "teamLab Borderless, Azabudai Hills, 1-2-4 Azabudai, Minato-ku, Tokyo", # teamLab
    "730pm": "Sushi Tokyo Ten, 1-3-10 Azabudai, Minato-ku, Tokyo",       # Sushi Tokyo Ten (approx.)
    "9pm": "2-chome-19-9 Okubo, Shinjuku City, Tokyo 169-0072, Japan"    # Back to Airbnb
}

# Generate main day2.html with maps
main_content = '<ul>'  # No duplicate h1
main_content += f'<li><strong class="top-level">Overview:</strong> {data["overview"]}</li>'
prev_time = None
for time, sections in {k: v for k, v in data.items() if k != "overview"}.items():
    time_display = time.replace("am", " AM").replace("pm", " PM")
    main_content += f'<li><strong class="top-level">{time_display} - {time.upper()}:</strong>\n<ul>'
    main_content += f'<li><strong class="second-level">Base:</strong> {sections["base"].replace("\n", "<br>")}<br>'
    main_content += f'[<a href="{time}_short_story.html">Short Story</a>] [<a href="{time}_long_story.html">Long Story</a>] '
    main_content += f'[<a href="{time}_facts.html">Facts</a>] [<a href="{time}_places.html">Places</a>]'

    # Add Google Maps link if not the first stop
    if prev_time:
        travel_mode = "walking" if "walk" in sections["base"].lower() else "transit"
        origin = locations[prev_time]
        destination = locations[time]
        waypoints = ""
        substop_note = ""
        if time == "1015am" and "substop_teahouse" in sections:  # Tea House in Shinjuku Gyoen
            substop_note = " (includes Tea House View)"
        elif time == "1215pm" and "substop_harajuku" in sections:  # Harajuku Peek
            waypoints = "&waypoints=Takeshita Street, Harajuku, Tokyo"
            substop_note = " (via Harajuku Peek)"
        elif time == "230pm" and "substop_spider" in sections:  # Spider Statue in Mori Garden
            substop_note = " (includes Spider Statue)"

        map_url = f"https://www.google.com/maps/dir/?api=1&origin={origin.replace(' ', '+')}&destination={destination.replace(' ', '+')}{waypoints}&travelmode={travel_mode}&hl=en"
        route_summary = {
            "10am-1015am": "Walk southeast on Okubo-dori, turn right onto Meiji-dori, enter Shinjuku Gyoen.",
            "1015am-1115am": "Exit Shinjuku Gyoen, walk northwest on Meiji-dori, left onto Okubo-dori to Himawari Sushi.",
            "1115am-1215pm": "Walk southwest on Okubo-dori, right onto Meiji-dori, left onto Shinjuku-dori to Meiji Shrine.",
            "1215pm-1pm": "JR Yamanote from Harajuku to Tokyo Station, walk 500m to Edo Castle Gardens.",
            "1pm-230pm": "JR Yamanote to Shibuya, Hibiya Line to Roppongi, walk 500m to Mori Tower.",
            "230pm-5pm": "Walk northwest on Roppongi-dori, left onto Azabudai to teamLab Borderless.",
            "5pm-730pm": "Walk east on Azabudai, Sushi Tokyo Ten is nearby.",
            "730pm-9pm": "Hibiya Line to Hibiya, JR Yamanote to Shin-Okubo, walk 300m to Airbnb."
        }.get(f"{prev_time}-{time}", "Route details to be added.")
        main_content += f'<br><a href="{map_url}" target="_blank">Google Maps Route{substop_note}</a> - {route_summary}'
    
    for key, value in sections.items():
        if key.startswith("substop_"):
            substop_name = key.split("_")[1]
            main_content += f'<br>Sub-Stop: {substop_name.capitalize()} (10 min) - {value} [<a href="{time}_{substop_name}.html">Details</a>]'
    main_content += '</li></ul></li>'
    prev_time = time

main_content += '</ul>\n<p><a href="../japan_main.html">Back to Main Itinerary</a></p>'
with open('day2/day2.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Day 2 Overview", header="Day 2 (04/01/25): Jet Lag Ease-In with Hanami, History, and teamLab", content=main_content))

# Generate subpages (unchanged)
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