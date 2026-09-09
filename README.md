# t-sources

Public media library for MultiHub TV receivers. Published media belongs under
`sources/`.

## PowerPoint conversion

Uploading a `.ppt` or `.pptx` below `sources/` starts the **Render PowerPoint
slides** GitHub Action. It renders each slide with LibreOffice, stores the PNG
files under hidden `sources/.presentations/`, and writes a neighboring
`<presentation>.slides.json` loop manifest. The dashboard hides that manifest
and lets operators select the original PowerPoint after it reports **Ready to
loop**.

The workflow runs only when a PowerPoint changes. It requires the repository's
GitHub Actions workflow token to have **Read and write permissions** for
contents.
