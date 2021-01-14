### Hi there :wave:

{% for section, section_data in sections.items() %}
#### {{ section }}

{% for repo, stats in section_data.items() %}
![{{ stats['owner']['login'] }}]({{ stats['owner']['avatar_url'] }}&s=24)
**[{{ stats["full_name"] }}]({{ stats["html_url"] }})**
{% if stats["stargazers_count"] > 1 %}— :star: {{ stats["stargazers_count"] }}{% endif %}

{{ stats["description"] }}

{% endfor %}
{% endfor %}

[Last updated {{ meta["time"].strftime("%Y-%m-%d") }}]({{ meta["self_url"] }})