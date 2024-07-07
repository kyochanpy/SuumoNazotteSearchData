from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import MedicalInstitutionXmlParser
from .main import MedicalInstitution


def main():
    config = load_config()
    government_offices = MedicalInstitution(
        config,
        DB(config),
        S3(config),
        MedicalInstitutionXmlParser(),
        "government_offices",
    )
    for i in range(47):
        government_offices.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()