from whitenoise.storage import CompressedManifestStaticFilesStorage


# Ripped off from https://stackoverflow.com/a/51580328/1446945
class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
