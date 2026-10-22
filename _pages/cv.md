---
layout: cv
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_format: rendercv
description: Education, experience, research support, and technical skills of Lukman Hakim.
toc:
  sidebar: left
---

## Downloadable CV

A downloadable PDF and an on-page preview will appear here when the finalized CV file is uploaded.

{% assign cv_pdf_path = '/assets/pdf/Lukman_Hakim_CV.pdf' | relative_url %}
{% assign uploaded_cv_pdf = site.static_files | where: 'path', 'assets/pdf/Lukman_Hakim_CV.pdf' | first %}
{% if uploaded_cv_pdf %}
<p><a class="btn btn-primary" href="{{ cv_pdf_path }}" download>Download CV (PDF)</a></p>
<div class="cv-pdf-preview" style="width:100%; margin:1rem 0 2rem;">
  <iframe src="{{ cv_pdf_path }}#view=FitH" title="Lukman Hakim CV PDF preview" style="width:100%; height:800px; border:1px solid #dee2e6; border-radius:0.5rem;"></iframe>
</div>
{% else %}
<p><em>The finalized PDF has not been added yet. Once uploaded, this section will display the download button and PDF preview automatically.</em></p>
{% endif %}
