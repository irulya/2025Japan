import json
import os

def generate_html(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Debug: Print the first stop to verify data
    print(f"Debugging {json_file}:")
    print(json.dumps(data['itinerary'][0], indent=2))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['day']} - {data['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; margin-top: 20px; }}
        ul {{ margin-left: 20px; padding-left: 0; list-style-type: square; }}
        li {{ margin-bottom: 10px; }}
        p {{ margin: 15px 0; }}
        strong {{ color: #e74c3c; }}
        a {{ color: #34495e; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{data['day']}: {data['title']}</h1>
    <p><strong>Overview:</strong> {data['overview']}</p>
    <h2>Itinerary</h2>
    <ul>
"""

    for i, stop in enumerate(data['itinerary'], 1):
        stop_id = f"stop{i}"
        html += f"""        <li><strong>{stop['time']} - {stop['location']}</strong>
            <ul>
                <li><a href="#{stop_id}-base">Base</a></li>
                <li><a href="#{stop_id}-must-see">Must See</a></li>
                <li><a href="#{stop_id}-short-story">Short Story</a></li>
                <li><a href="#{stop_id}-long-story">Long Story</a></li>
                <li><a href="#{stop_id}-sub-stop">Sub-Stop</a></li>
            </ul>
        </li>
"""

    html += """    </ul>
"""

    for i, stop in enumerate(data['itinerary'], 1):
        stop_id = f"stop{i}"
        html += f"""    <h2 id="{stop_id}-base">{stop['time']} - {stop['location']}</h2>
    <p>{stop.get('base', 'Missing Base')}</p>
    <h2 id="{stop_id}-must-see">Must See</h2>
    <p>{stop.get('must_see', 'Missing Must See')}</p>
    <h2 id="{stop_id}-short-story">Short Story</h2>
    <p>{stop.get('short_story', 'Missing Short Story')}</p>
    <h2 id="{stop_id}-long-story">Long Story</h2>
    <p>{stop.get('long_story', 'Missing Long Story')}</p>
    <h2 id="{stop_id}-sub-stop">Sub-Stop: {stop['sub_stop']['name']}</h2>
    <p>{stop['sub_stop'].get('details', 'Missing Sub-Stop Details')}</p>
"""

    html += """    <p><a href="day7.html">Back to Day 7 Menu</a></p>
</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    os.makedirs("E:/misc/Travel/2025Japan/day7", exist_ok=True)
    generate_html("E:/misc/Travel/2025Japan/railway-museum.json", "E:/misc/Travel/2025Japan/day7/railway-museum.html")
    generate_html("E:/misc/Travel/2025Japan/philosophers-path.json", "E:/misc/Travel/2025Japan/day7/philosophers-path.html")