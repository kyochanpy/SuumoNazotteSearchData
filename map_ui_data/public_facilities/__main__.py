from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import PublicFacilitiesXmlParser
from .main import PublicFacilities


def main():
    config = load_config()
    medical_institution = PublicFacilities(
        config,
        DB(config),
        S3(config),
        PublicFacilitiesXmlParser(),
        "medical_institution",
    )
    for i in range(47):
        medical_institution.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()