from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import GovernmentOfficesXmlParser
from .main import GovernmentOffices


def main():
    config = load_config()
    government_offices = GovernmentOffices(
        config,
        DB(config),
        S3(config),
        GovernmentOfficesXmlParser(),
        "government_offices",
    )
    for i in range(47):
        government_offices.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()