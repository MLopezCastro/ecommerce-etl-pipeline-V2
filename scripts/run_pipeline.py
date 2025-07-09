import logging
from ecommerce_etl import config, io, transform, validate

logging.basicConfig(
    filename=config.LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run():
    logging.info("Inicio del pipeline")

    df = io.read_csv(config.RAW_PATH)

    df = (
        df.pipe(transform.standardize_column_names)
          .pipe(transform.convert_types)
          .pipe(transform.add_total_amount)
    )

    validate.no_nulls(df, ["order_id", "order_date", "customer_id", "product_id", "product_name"])
    validate.positive_values(df, ["quantity", "unit_price"])
    validate.allowed_status(df)

    io.write_csv(df, config.OUTPUT_PATH)

    logging.info("Fin del pipeline")

if __name__ == "__main__":
    run()
