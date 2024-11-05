import markdown
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader  # type: ignore


def parse(content, content_type=None):
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body and load header into dict.
    lines = content.splitlines()

    header_start = lines.index('---') + 1
    header_end = lines[header_start:].index('---') + 1
    header = '\n'.join(lines[header_start:header_end])
    body = '\n'.join(lines[header_end + 1:]).strip()
    parsed = load(header, Loader=Loader)  # noqa: S506

    # Parse body if not HTML/XML.
    if body and content_type == 'markdown':
        body = markdown.markdown(
            body,
            extensions=[
                'markdown.extensions.attr_list',
                'markdown.extensions.def_list',
                'markdown.extensions.fenced_code'
            ])

    parsed['body'] = body
    return parsed
