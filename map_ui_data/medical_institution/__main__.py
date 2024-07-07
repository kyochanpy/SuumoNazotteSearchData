from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import MedicalInstitutionXmlParser
from .main import MedicalInstitution


def main():
    config = load_config()
    medical_institution = MedicalInstitution(
        config,
        DB(config),
        S3(config),
        MedicalInstitutionXmlParser(),
        "medical_institution",
    )
    for i in range(47):
        medical_institution.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()