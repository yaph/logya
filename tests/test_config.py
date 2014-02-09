# -*- coding: utf-8 -*-
import yaml

config = {
    'site': {
        'base_url': 'http://localhost:8080',
        'disqus_shortname': None,
    },
    'templates': [
        {'content_type': 'index', 'template': 'index.html'},
        {'content_type': 'doc', 'template': 'post.html'}
    ],
    'indexes': [
        {'var': 'tags', 'path': 'tags'}
    ]
}

with open('tests/site.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

with open('tests/site.yaml', 'r') as f:
    yaml_config = yaml.load(f)

assert config == yaml_config
