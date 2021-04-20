<!-- This file is auto-generated. Do not edit! -->

### {{ input_data['main-title'] }}

{{ input_data.get('description', '') }}

{% for section_data in input_data['sections'] %}
---

### {{ section_data['title'] }}

{% if 'description' in section_data %}
<sup><i>{{ section_data['description'] }}</i></sup>
{% endif %}

{% for repo in section_data['repos'] %}
{% set stats = get_stats(repo) %}
<a href="{{ stats['owner']['html_url'] }}"><img src="{{ stats['owner']['avatar_url'] }}&s=16" alt="{{ stats['owner']['login'] }}" width="16"></a>
<a href="{{ stats['html_url'] }}"><b>{{ stats['owner']['login'] }}</b> / <b>{{ stats['name'] }}</b></a>
{% if stats['stargazers_count'] > 1 %} — :star: {{ stats['stargazers_count'] }}{% endif %}

> {{ stats['description'] }}

{% endfor %}
{% endfor %}

<p align="right">
<sub>
<a href="{{ meta['self_url'] }}">Last updated {{ meta['now'].strftime('%Y-%m-%d') }}</a>
</sub>
</p>
