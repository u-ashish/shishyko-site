import os
import re
import shutil
from pathlib import Path
import markdown
import yaml
from jinja2 import Template

def read_markdown_with_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split frontmatter and markdown content
    parts = re.split(r'^---\s*$', content.strip(), maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return None, content
    
    frontmatter = yaml.safe_load(parts[1])
    markdown_content = parts[2].strip()
    
    return frontmatter, markdown_content

def convert_markdown_to_html(markdown_content):
    # Initialize Markdown converter with extensions
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'footnotes'])
    return md.convert(markdown_content)

def build_site():
    # Create output directory
    output_dir = Path('essays')
    output_dir.mkdir(exist_ok=True)
    
    # Read template
    with open('templates/essay.html', 'r') as f:
        template = Template(f.read())
    
    # Process all markdown files
    content_dir = Path('content/essays')
    for md_file in content_dir.glob('*.md'):
        # Read and parse markdown file
        frontmatter, content = read_markdown_with_frontmatter(md_file)
        if not frontmatter:
            print(f"Skipping {md_file}: No frontmatter found")
            continue
        
        # Convert markdown to HTML
        html_content = convert_markdown_to_html(content)
        
        # Generate HTML file
        output_file = output_dir / f"{md_file.stem}.html"
        with open(output_file, 'w') as f:
            f.write(template.render(
                content=html_content,
                **frontmatter
            ))
        
        print(f"Generated {output_file}")
    
    # Copy essay-styles.css to essays directory
    shutil.copy2('essay-styles.css', output_dir)
    print("Copied essay-styles.css")

    print("Site built successfully!")

if __name__ == '__main__':
    build_site() 