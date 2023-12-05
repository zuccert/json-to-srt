import json

def json_to_srt(json_data):
    srt_content = ""
    for index, entry in enumerate(json_data["subtitles"], start=1):
        start_time = entry["startMs"] / 1000.0
        end_time = (entry["startMs"] + entry["durationMs"]) / 1000.0

        srt_content += f"{index}\n"
        srt_content += f"{convert_to_srt_time_format(start_time)} --> {convert_to_srt_time_format(end_time)}\n"
        srt_content += f"{entry['text']}\n\n"

    return srt_content.strip()

def convert_to_srt_time_format(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{int(seconds):02d},{milliseconds:03d}"

# Read JSON from file
with open("example.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Convert JSON to SRT
srt_data = json_to_srt(json_data)

# Save the SRT content to a file
output_file_path = "output.srt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(srt_data)

print(f"SRT content saved to {output_file_path}")
