---
layout: default
title: Home
description: Archive and documentation hub for projects created during Dinacon Bali 2025
---

# Dinacon Bali 2025 Master Index

Welcome to the archive and documentation hub for the projects created by [Vincent Naples (@drmbt)](https://www.drmbt.com) in the Les fishing village during the [Dinacon Bali 2025](https://2025.dinacon.org/) conference and art residency.

## About

This site serves as a landing page for all related projects, including documentation, code written and employed, essays and documentation on the inspiration and implementation of my texture caching process, and a satirical column "Chron Jobs" written for the Dinachron newsletter. Featured writings include the essay <a href="{{ '/docs/On-Textures-and-Time/' | relative_url }}">"On Textures and Time"</a> and the <a href="{{ '/docs/Chron-Jobs/' | relative_url }}">"Chron Jobs" column</a>.

Feedback or questions about any project or process is welcomed via a [GitHub issue report](https://github.com/drmbt/dinacon-bali-2025/issues), or email to [vincent@drmbt.com](mailto:vincent@drmbt.com)

---

## Projects

<div class="project-grid">

<div class="project-card">
  <img src="{{ 'thumbnails/tex3d.jpg' | relative_url }}" alt="Texture Library" class="project-thumbnail">
  <div class="project-content">
    <h3><a href="https://photos.app.goo.gl/zmqjz56mBvRjYoAZ6" target="_blank" rel="noopener">Texture Library</a></h3>
    <p>A curated photo gallery of decontextualized textures collected in Bali.</p>
    <p>Read more about the philosophy and technique behind texture collection in the essay <a href="{{ '/docs/On-Textures-and-Time/' | relative_url }}">"On Textures and Time"</a>.</p>
  </div>
</div>

<div class="project-card">
  <div class="thumbnail-grid">
    <img src="{{ 'thumbnails/SLH_ramp.jpg' | relative_url }}" alt="SLH Ramp">
    <img src="{{ 'thumbnails/tex-gradient.jpg' | relative_url }}" alt="Texture Gradient">
  </div>
  <div class="project-content">
    <h3><a href="https://photos.app.goo.gl/5fgeBVUMi9ySxDxv9" target="_blank" rel="noopener">Texture Cache</a></h3>
    <p>A video collage project using the Texture Library as a lookup table.</p>
    
    <p>This method leverages TouchDesigner's texture3d and time machine operators to recall individual pixels from a cached texture array that are looked up via the luminance of an incoming key input video feed. For this project, I'm caching the above texture library shot in Les Bali to reconstitute images captured by myself, other dinacon attendees, and curated from submissions to the iNaturalist API during this residency.</p>
    
    <p>I wrote a custom shader that encodes luminance data for "low saturation" pixels into the 0.0 - 0.5 value pixel range of a grey scale key image, and ROYGBIV color sorted information into the 0.5 - 1.0 range of a luminance map to create compositions that depict local life, flora and fauna as painterly collages reconstituted from the decaying textures photographed during this trip.</p>
    
    <p>More about the technique and philosophy of this practice can be found via link, or the 4th installment of the 2025 Dinachron Newsletter in the essay <a href="{{ '/docs/On-Textures-and-Time/' | relative_url }}">"On Textures and Time"</a>, written while camera-sitting a timelapse session.</p>
  </div>
</div>

<div class="project-card">
  <img src="{{ 'thumbnails/timelapse.jpg' | relative_url }}" alt="Time Lapse Bali" class="project-thumbnail">
  <div class="project-content">
    <h3><a href="{{ '/Time-Lapse-Bali/' | relative_url }}">Time Lapse Bali</a></h3>
    <p>A collection of timelapse photography sequences captured during Dinacon and the subsequent time on the island of Bali. These sequences were shot using the <a href="https://www.matjoez.com/2018/07/30/complete-guide-to-shooting-and-editing-holy-grail-timelapses/" target="_blank" rel="noopener">"Holy Grail Method"</a> of timelapse photography, a time-intensive process involving locked off ISO and aperture, with shutter speed manually changed with the lighting conditions to produce optimal transitions across sunrise/sunset without flickering.</p>
    
    <p><strong>Locations filmed:</strong></p>
    <ul>
      <li>Kura Kura Beach and Garden</li>
      <li>Les Village Field</li>
      <li>Kintamani</li>
      <li>Mt. Butar</li>
      <li>Pantai Batu Belig near Canggu</li>
    </ul>
    
    <p><a href="https://photos.app.goo.gl/9DSYiJyWBQaMnbCb9" target="_blank" rel="noopener">View raw timelapse exports</a></p>
  </div>
</div>

<div class="project-card">
  <div class="project-content">
    <h3><a href="{{ '/Time-Cache-Bali/' | relative_url }}">Time Cache Bali</a></h3>
    <p>A non-linear collage project that consists of anachronistic time dilated gradient compositions made from static timelapse image sequences and greyscale procedurally generated feedback loop luminance maps.</p>
  </div>
</div>

<div class="project-card">
  <div class="project-content">
    <h3><a href="https://github.com/drmbt/iNaturalist-downloader" target="_blank" rel="noopener">iNaturalist Downloader</a></h3>
    <p>A script and CLI tool for querying and downloading images and information from the iNaturalist API.</p>
    
    <p>This script allowed me to pull locally sourced images of the flora and fauna found around Les fishing village, sort them by kingdom and attribution, and manually curate images for use in the texture cache project.</p>
  </div>
</div>

<div class="project-card">
  <img src="{{ 'thumbnails/iNaturalist.jpg' | relative_url }}" alt="iNaturalist Image Selects" class="project-thumbnail">
  <div class="project-content">
    <h3><a href="https://photos.app.goo.gl/2sU4z2tfgWMhbDni6" target="_blank" rel="noopener">iNaturalist Image Selects</a></h3>
    <p>Curated and processed images pulled from a time-gated query of the iNaturalist API localized within 8km of Les fishing village during dinacon, and used in the Texture Cache project.</p>
    
    <p>After curating images that would read well in landscape orientation and were of a relatively high original resolution, I processed them through lightroom for cropping, reorienting and color balancing, and then ran them through Topaz Gigapixel AI (decidedly not open source) as its the only process I'm aware of that will not just upscale an image, but increase its bit depth from 8 to 16. This is important for the texture caching process, as 8 bit compression artifacts, particularly from web scaled .jpg images create awful artifacting when used in my texture cache workflow.</p>
    
    <p>Although an AI upscaler by nature introduces some amount of hallucination, I'm not concerned in this case as their primary use is for shape, since they will be looked up anyhow and reconstituted using the hi resolution textures captured in my library.</p>
  </div>
</div>

<div class="project-card">
  <div class="project-content">
    <h3><a href="https://photos.app.goo.gl/xhbz6ERDyrVhF7Vd6" target="_blank" rel="noopener">Dinacon 2025 Photography</a></h3>
    <p>Not all of the photography I took during this trip was useful as raw assets for art making. I also spent time shooting photos for gift and trade with local resorts, hotels and homestays to help them better support themselves through their hospitality and tourism services.</p>
    
    <p>Below are albums that tell the story of my time at dinacon, curated images of life in Les fishing village Bali:</p>
    
    <ul>
      <li><a href="https://photos.app.goo.gl/xhbz6ERDyrVhF7Vd6" target="_blank" rel="noopener">Dinacon Bali 2025 Story Selects</a></li>
      <li><a href="https://photos.app.goo.gl/HKRcKAJaw3vcxCg67" target="_blank" rel="noopener">Plant Olympics</a></li>
      <li><a href="https://photos.app.goo.gl/zmqjz56mBvRjYoAZ6" target="_blank" rel="noopener">Texture Library</a> (same as above)</li>
      <li><a href="https://photos.app.goo.gl/Ff6itxBvwVcZ4hDHA" target="_blank" rel="noopener">Dinacon Last Supper</a></li>
      <li><a href="https://photos.google.com/share/AF1QipN33IcMHt-fjRAPwgRu4ngYDBPZkvTJnp9Tvofn_62XQTepPUU5FMghTsZkqBg94Q?key=U1VMSW9rZ3BDM3lhNlV0dnlqU1IxN2RWUk1iTFV3" target="_blank" rel="noopener">Kintamani Photography</a></li>
      <li><a href="https://photos.app.goo.gl/YkNgKnx1c6HRUAJP7" target="_blank" rel="noopener">Hotel Colosseum Kintamani</a></li>
    </ul>
  </div>
</div>

<div class="project-card">
  <img src="{{ 'thumbnails/3d-model-from-single-image-AI.jpg' | relative_url }}" alt="3D Model From Single Image AI" class="project-thumbnail">
  <div class="project-content">
    <h3><a href="https://drive.google.com/drive/folders/1MnnwmTJcS1NHYoNZ0laKhD3mYq3bygjI?usp=sharing" target="_blank" rel="noopener">3D Model From Single Image AI</a></h3>
    <p>As a part of the 3d modeling cohort, I experimented with leveraging open source AI models to create 3d meshes.</p>
    
    <p>This process leverages <a href="https://www.comfy.org/" target="_blank" rel="noopener">ComfyUI</a> open source local AI inference interface and the open weights <a href="https://hunyuan-3d.com/" target="_blank" rel="noopener">Hunyuan3d v2</a> model to create 3D models generated from single perspective photographs when video or multi perspective photogrametry data sets were unavailable. Although imperfect, I was impressed at how well the models turned out.</p>
    
    <p>The collection can be accessed <a href="https://drive.google.com/drive/folders/1MnnwmTJcS1NHYoNZ0laKhD3mYq3bygjI?usp=sharing" target="_blank" rel="noopener">here</a>.</p>
  </div>
</div>

</div>

---

## Featured Writing

### [Essay: On Texture and Time]({{ '/docs/On-Textures-and-Time/' | relative_url }})
Read the essay about textures and time written during the residency.

### ["Chron Jobs" Dinachron Newsletter Zine Column]({{ '/docs/Chron-Jobs/' | relative_url }})
Read the Chron Jobs column from the Dinachron newsletter.

---

<div class="text-center text-muted">
  <p>Built with ❤️ using Jekyll and GitHub Pages</p>
  <p><a href="https://github.com/drmbt/dinacon-bali-2025" target="_blank" rel="noopener">View on GitHub</a></p>
</div> 