from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import PublicFacilitiesXmlParser
from .main import PublicFacilities


def main():
    config = load_config()
    public_facilities = PublicFacilities(
        config,
        DB(config),
        S3(config),
        PublicFacilitiesXmlParser(),
        "public_facilities",
    )
    for i in range(47):
        public_facilities.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()