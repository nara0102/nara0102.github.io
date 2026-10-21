---
layout: page
permalink: /blog/
title: blog
description: Selected photography, place reviews, and stories from community and digital work.
nav: true
nav_order: 1
---

# Visual Journal

A curated collection of photographs and short stories. This space will feature selected posts from my personal Instagram, photography from places I visit, and reviews I write on platforms such as Google Maps and Grab. I also plan to share selected TikTok videos here as that channel develops.

{% assign field_notes = site.posts | where_exp: "post", "post.categories contains 'field-notes'" | sort: "date" | reverse %}

{% if field_notes.size > 0 %}
<div class="post-list">
  {% for post in field_notes %}
  <article class="mb-4">
    {% if post.thumbnail %}
    <p><img src="{{ post.thumbnail | relative_url }}" alt="{{ post.title }}" loading="lazy" style="max-width: 100%; height: auto;"></p>
    {% endif %}
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="text-muted">{{ post.date | date: "%B %d, %Y" }}</p>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
    <p><a href="{{ post.url | relative_url }}">Read the story</a></p>
  </article>
  {% endfor %}
</div>
{% else %}
<p>Selected posts are being prepared. Each entry will include the original source link and any relevant photo or review context.</p>
{% endif %}
