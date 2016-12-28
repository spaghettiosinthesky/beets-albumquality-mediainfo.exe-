# beets-albumquality

[Beets](https://github.com/beetbox/beets) plugin to allow the usage of the imported album quality with the help from [MediaInfo](https://mediaarea.net/en/MediaInfo).

## Installation (*WIP*)

`pip install beets-albumquality`

## Configuration

`plugins: albumquality`

## Usage

Plugin adds a new album field called `quality`. This field will return one of the following depending on the album's quality.

- 96K
- 128K
- 160K
- 192K
- 224K
- 320K
- V0..V9
- VBR (only used if the LAME encoding settings cannot be determined)

```
paths:
    default: $albumartist - $album [$quality]/$track. $title
```

You can query your library for all albums whose quality is V0.

`beet list -a quality:v0`

or...

`beet list -a quality:192`