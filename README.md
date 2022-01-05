# OpenAPI Downloader

Recursively download the OpenAPI specification and its dependency.
This project is able to plug multiple downloaders (e.g. 3GPP)

## Feature

- Recursively resolve `$ref` tag in the given OpenAPI specification
- Automatically trim the dependency tree to prevent redundant download
- Plugable downloader; Currently support download specifications from 3GPP FTP

## Usage

```
$ openapi-dl -h
usage: openapi-dl [-h] [-o, --output output_dir] [--dl downloader] [--dldir download_dir] spec [spec ...]

Fetch given OpanAPI specification and all of it's dependencies from 3GPP.

positional arguments:
  spec                  Filename of desired OpenAPI specification from 3GPP.

optional arguments:
  -h, --help            show this help message and exit
  -o, --output output_dir
                        The directory where will the dependent files place.
                        (Default is the current working directory)
  --dl downloader       The downloader of specification files.
                        (Currently only 3GPP is avaliable)
  --dldir download_dir  The location to store original specification files.
                        (Default is /tmp/openapi_spec/)
```

Example

```bash
# Fetch all of the dependencies of TS29549_SS_Events.yaml
# and TS29549_SS_UserProfileRetrieval.yaml
openapi-dl -o spec_test TS29549_SS_Events.yaml TS29549_SS_UserProfileRetrieval.yaml
```

```
[INFO] Fetching the list of series 29 in release 17
[INFO] Downloading https://www.3gpp.org/ftp/Specs/latest/Rel-17/29_series/29549-h30.zip
[==================================================] 100/100
[INFO] Downloaded /tmp/openapi_spec/29549-h30.zip and extracted TS29549_SS_UserProfileRetrieval.yaml
[INFO] Parsing dependency of TS29549_SS_UserProfileRetrieval.yaml#/
[INFO] Downloading https://www.3gpp.org/ftp/Specs/latest/Rel-17/29_series/29122-h40.zip
[==================================================] 100/100
[INFO] Downloaded /tmp/openapi_spec/29122-h40.zip and extracted TS29122_CommonData.yaml
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/default
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/503
[INFO] Downloading https://www.3gpp.org/ftp/Specs/latest/Rel-17/29_series/29571-h40.zip
[==================================================] 100/100
[INFO] Downloaded /tmp/openapi_spec/29571-h40.zip and extracted TS29571_CommonData.yaml
[INFO] Parsing dependency of TS29571_CommonData.yaml#/components/schemas/SupportedFeatures
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/500
...
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/schemas/TimeOfDay
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/schemas/DayOfWeek
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/schemas/TimeWindow
[INFO] Downloading https://www.3gpp.org/ftp/Specs/latest/Rel-17/29_series/29522-h40.zip
[==================================================] 100/100
[INFO] Downloaded /tmp/openapi_spec/29522-h40.zip and extracted TS29522_AnalyticsExposure.yaml
[INFO] Parsing dependency of TS29522_AnalyticsExposure.yaml#/components/schemas/AnalyticsEvent
[INFO] Parsing dependency of TS29122_MonitoringEvent.yaml#/components/schemas/MonitoringType
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/415
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/413
[INFO] Parsing dependency of TS29122_CommonData.yaml#/components/responses/411
[INFO] All dependencies of the following specification(s) are successfully downloaded.
[INFO]   TS29549_SS_Events.yaml
[INFO]   TS29549_SS_UserProfileRetrieval.yaml
```

## Installation

```bash
git clone https://github.com/nuk-icslab/openapi-dl.git
cd openapi-dl
pip install .
```

## Author

Yong-Hsiang Hu < iftnt1999 [at] gmail.com >
