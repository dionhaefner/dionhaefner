### Hi there :wave:

{% for section_data in input_data['sections'] %}
#### {{ section_data['title'] }}

{% for repo in section_data['repos'] %}
{% set stats = get_stats(repo) %}
<a href="{{ stats['owner']['url'] }}">
<img src="{{ stats['owner']['avatar_url'] }}&s=16" alt="{{ stats['owner']['login'] }}">
<b>{{ stats['owner']['login'] }}</b>
</a>
/
<a href="stats['html_url']">
<b>{{ stats['name'] }}</b>
</a>
{% if stats['stargazers_count'] > 1 %} — :star: {{ stats['stargazers_count'] }}{% endif %}

> {{ stats['description'] }}

{% endfor %}
{% endfor %}

<p align="right">
<sub>
<a href="({{ meta['self_url'] }}">Last updated {{ meta['now'].strftime('%Y-%m-%d') }}
</sub>
</p>