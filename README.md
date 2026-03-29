# µ-tube

Open source 1of10/Viewstats alternative. Find out if a youtube video is a relative outlier.

<img width="1038" alt="Screenshot 2025-04-27 at 12 14 48 AM" src="https://github.com/user-attachments/assets/7892c143-6d2b-41dc-8e55-0e8082763264" />

## Background

I made this tool for [LukeJ](https://www.youtube.com/lukejtv). There are several popular youtube analytic tools out there ([Viewstats](https://www.viewstats.com) and [1of10](https://1of10.com) to name a couple) but these tools are often expensive and closed source. A lot of the functionality behind these popular tools really isn't that complicated so this is an attempt to bring some of this functionality to people who are trying to make good content and can't afford these alternatives. As I write this, mutube's functionality is pretty basic but the hope is that I'll expand its capabilities as I continue to make videos.

## 📦 Installation

#### Unix / MacOS:

```bash
# install uv (package manager):
curl -LsSf https://astral.sh/uv/install.sh | sh

# restart your terminal, or run the following command:
source $HOME/.local/bin/env # or follow instructions

# install mutube through uv
uv tool install --python 3.13 mutube
```

## 🚀 Usage

```bash
# add api key found from google cloud for YouTube v3 (will add instructions on this later)
mutube key {YOUTUBE_API_KEY}
# currently the only supported feature is finding out if some input URL is a relative outlier compared to the 9 videos before it (screenshot at the top)
mutube analyze "{YOUTUBE_VIDEO_URL}"
```

## 🔄 Update
```bash
uv tool install --upgrade mutube
```
