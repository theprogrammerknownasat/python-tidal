class AuthenticationError(Exception):
    pass


class MediaUnknown(Exception):
    pass


class UnknownManifestFormat(Exception):
    pass


class MediaMissing(Exception):
    pass


class StreamManifestDecodeError(Exception):
    pass


class MPDUnavailableError(Exception):
    pass


class MPDDecodeError(Exception):
    pass
