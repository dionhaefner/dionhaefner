### {{ input_data['main-title'] }}

{{ input_data.get('description') }}

{% for section_data in input_data['sections'] %}
### {{ section_data['title'] }}

{{ section_data.get('description') }}

{% for repo in section_data['repos'] %}
{% set stats = get_stats(repo) %}
![{{ stats['owner']['login'] }}]({{ stats['owner']['avatar_url'] }}&s=16)
<a href="{{ stats['owner']['url'] }}">
<b>{{ stats['owner']['login'] }}</b>
</a>
/
<a href="{{ stats['html_url'] }}">
<b>{{ stats['name'] }}</b>
</a>
{% if stats['stargazers_count'] > 1 %} — :star: {{ stats['stargazers_count'] }}{% endif %}

> {{ stats['description'] }}

{% endfor %}
{% endfor %}

<p align="right">
<sub>
<a href="{{ meta['self_url'] }}">Last updated {{ meta['now'].strftime('%Y-%m-%d') }}</a>
</sub>
</p>