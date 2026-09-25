# SaltySec Study Guides

Static GitHub Pages site for `https://saltysec.github.io/studyguides/`.

## Publish

1. Create a **public** GitHub repository named `studyguides` under `saltysec`.
2. Upload the contents of this folder to the **root** of its `main` branch. Do not upload the enclosing folder itself: `index.html` must be at the top level.
3. In the repository, open **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, branch to **main**, folder to **/(root)**, and save.
4. After deployment, visit `https://saltysec.github.io/studyguides/`.

| File | URL path |
| --- | --- |
| `index.html` | `/studyguides/` |
| `region-viii-emt.html` | `/studyguides/region-viii-emt.html` |
| `illinois-class-c.html` | `/studyguides/illinois-class-c.html` |
| `roadwise.html` | `/studyguides/roadwise.html` |

The landing page links use relative paths, so all files should remain alongside `index.html`. To update a guide or RoadWise, replace the corresponding HTML file and commit the change. The included `roadwise.html` is the current RoadWise app supplied by the owner and edited for this package.

Study-guide progress is saved separately for each visitor in that browser's `localStorage`. The site has no accounts or shared progress. RoadWise depends on external map libraries and live OpenStreetMap/Nominatim/Overpass services; it needs internet access and those services may rate-limit requests.
