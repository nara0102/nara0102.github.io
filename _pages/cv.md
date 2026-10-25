---
layout: cv
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_format: rendercv
cv_pdf: /assets/rendercv/rendercv_output/Lukman_Hakim_CV.pdf
description: "Education, professional experience, skills, and certificates."
toc:
  sidebar: left
---

<style>
  .cv .card {
    min-width: 0;
  }

  .cv #experience + div > ul.list-group {
    list-style: none;
    padding-left: 0;
  }

  .cv #experience + div > ul.list-group > li.list-group-item {
    list-style: none;
  }

  .cv #experience + div > ul.list-group > li > .row {
    display: grid !important;
    grid-template-columns: minmax(9rem, 11rem) minmax(0, 1fr);
    align-items: start;
    gap: 0 1.25rem;
    margin: 0;
  }

  .cv #experience + div .date-column {
    width: auto !important;
    min-width: 0;
    max-width: none;
    padding: 0;
    text-align: left !important;
  }

  .cv #experience + div .date-column .table-cv {
    width: 100%;
    margin: 0;
    table-layout: fixed;
  }

  .cv #experience + div .date-column .location {
    margin: 0.5rem 0 0;
    line-height: 1.4;
    overflow-wrap: anywhere;
  }

  .cv #experience + div > ul.list-group > li > .row > div:not(.date-column) {
    width: auto !important;
    min-width: 0;
    max-width: none;
    margin: 0 !important;
    padding: 0;
  }

  .cv #experience + div h6 {
    max-width: 100%;
    line-height: 1.4;
    overflow-wrap: anywhere;
  }

  @media (max-width: 767px) {
    .cv #experience + div > ul.list-group > li > .row {
      grid-template-columns: minmax(0, 1fr);
      gap: 0.5rem;
    }

    .cv #experience + div .date-column .table-cv,
    .cv #experience + div .date-column .table-cv tbody {
      display: block;
    }

    .cv #experience + div .date-column .table-cv tbody {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 0.4rem 1rem;
    }

    .cv #experience + div .date-column .table-cv tr,
    .cv #experience + div .date-column .table-cv td {
      display: block;
      padding: 0;
    }

    .cv #experience + div .date-column .location {
      margin: 0;
    }
  }
</style>

<p class="cv-certificate-link">
  Looking for certificates? <a href="/certificates/">View the certificate archive</a>.
</p>
