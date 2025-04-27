from .utils import load_config
from .client import DB, S3
from .xml_parser import XmlParser
from .point_processor import PointProcessorFactory
from tqdm import tqdm

def main():
    config = load_config()
    db = DB(config)
    s3 = S3(config)
    parser = XmlParser()

    point_types = ["fuel_station", "government_offices", "public_facilities", "medical_institution"]
    for point_type in point_types:
        print(f"processing {point_type}")
        point_processor = PointProcessorFactory.create(point_type, config, db, s3, parser)
        for i in tqdm(range(47)):
            point_processor.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()