---
layout: page
permalink: /certificates/
title: Certificates
nav: false
description: Certificate documents and previews.
---

## Certificate archive

This page lists certificate files uploaded to the portfolio. Select a file to open or download it.

{% assign has_certificates = false %}
{% for certificate in site.static_files %}
  {% if certificate.path contains 'assets/certificates/' and certificate.name != 'README.md' %}
    {% assign has_certificates = true %}
    {% assign file_extension = certificate.extname | downcase %}
    <section style="margin: 1.5rem 0; padding: 1rem; border: 1px solid #dee2e6; border-radius: 0.5rem;">
      <h3>{{ certificate.name }}</h3>
      <p><a href="{{ certificate.path | relative_url }}" target="_blank" rel="noopener">Open or download certificate</a></p>
      {% if file_extension == '.pdf' %}
        <details>
          <summary>Preview certificate</summary>
          <iframe src="{{ certificate.path | relative_url }}#view=FitH" title="{{ certificate.name | escape }}" style="display:block; width:100%; height:640px; margin-top:1rem; border:1px solid #dee2e6;"></iframe>
        </details>
      {% elsif file_extension == '.png' or file_extension == '.jpg' or file_extension == '.jpeg' %}
        <img src="{{ certificate.path | relative_url }}" alt="{{ certificate.name | escape }}" loading="lazy" style="display:block; max-width:100%; max-height:720px; width:auto; height:auto; margin-top:1rem; border-radius:0.25rem;">
      {% endif %}
    </section>
  {% endif %}
{% endfor %}

{% unless has_certificates %}
<p>No certificate files have been uploaded yet. Add PDF or image files to <code>assets/certificates/</code>, then publish the changes to display them here.</p>
{% endunless %}

<p><a href="{{ '/cv/' | relative_url }}">Back to CV</a></p>
