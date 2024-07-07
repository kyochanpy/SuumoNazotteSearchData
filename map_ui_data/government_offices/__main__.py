from ..common.utils import load_config  # type: ignore
from ..common.client import DB, S3  # type: ignore
from .parser import GovernmentOfficesXmlParser  # type: ignore
from .main import GovernmentOffices  # type: ignore


def main():
    config = load_config()
    government_offices = GovernmentOffices(
        config,
        DB,
        S3,
        GovernmentOfficesXmlParser,
        "government_offices",
    )
    for i in range(47):
        government_offices.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()