import os
import pdfkit

id = 122326132
user_name = "Margo Skorobohatova"
age = 21
city = 'Odessa'

with open('./index.html', 'r', encoding='utf-8') as file:
    html_template = file.read()

html_template = html_template.replace('{{ id }}', str(id))
html_template = html_template.replace('{{ user_name }}', user_name)
html_template = html_template.replace('{{ age }}', str(age))
html_template = html_template.replace('{{ city }}', city)

output_directory = './output'
output_path = os.path.join(output_directory, 'output.pdf')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

try:
    pdfkit.from_file(output_path, html_template)
    print(f"PDF generated and saved to {os.path.abspath(output_path)}")
except Exception as e:
    print(f"Error: {e}")