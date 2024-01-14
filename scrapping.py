import json
import mailbox
from email import policy
from email.parser import BytesParser
import re

mbox_file_path = r'C:\Users\MFX-4\Desktop\cs210mail\All mail Including Spam and Trash.mbox'
output_json_path = 'email_data.json'
max_emails_to_process = 200

email_data = []

mbox = mailbox.mbox(mbox_file_path)

# Define a function to remove links from a string
def remove_links(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+|\S+\.(com|org|net|io)\S*')
    return re.sub(url_pattern, '', text)

for idx, message in enumerate(mbox):
    if idx >= max_emails_to_process:
        break

    email_message = BytesParser(policy=policy.default).parsebytes(message.as_bytes())

    email_info = {
        "subject": email_message['subject'],
        "from": email_message['from'],
        "to": email_message['to'],
        "date": email_message['date'],
        "content": []
    }

    for part in email_message.iter_parts():
        content_type = part.get_content_type()

        try:
            if content_type == 'text/plain':
                decoded_part = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                cleaned_content = remove_links(decoded_part)
                email_info["content"].append({
                    "content_type": content_type,
                    "decoded_content": cleaned_content
                })
        except Exception as e:
            print(f"Failed to decode content: {e}")

    email_data.append(email_info)

# Save the data as JSON
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(email_data, json_file, ensure_ascii=False, indent=2)

print(f"{len(email_data)} emails processed and saved to {output_json_path}")
