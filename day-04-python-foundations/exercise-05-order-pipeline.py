# Question 5 - Order Pipeline with Logging
import csv
import json
import logging

# --- SETUP ---
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "item", "qty", "price"])
    writer.writerow(["1", "Keyboard", "2", "45.00"])
    writer.writerow(["2", "Mouse", "not_a_number", "15.00"])   # bad qty
    writer.writerow(["3", "Monitor", "1", "-120.00"])          # negative price
    writer.writerow(["4", "USB Cable", "5", "4.50"])


# --- ANSWER ---
def process_orders(csv_path, json_path, log_path):
    logger = logging.getLogger("orders")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()   # avoid duplicate handlers if called twice

    handler = logging.FileHandler(log_path, mode="w")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s"))
    logger.addHandler(handler)

    valid_rows = []
    num_valid = 0
    num_invalid = 0

    try:
        with open(csv_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row_number, row in enumerate(reader, start=1):
                try:
                    qty = int(row["qty"])
                    price = float(row["price"])
                except ValueError as e:
                    logger.error(f"Row {row_number}: bad qty/price "
                                 f"({row['qty']!r}, {row['price']!r}) - {e} - SKIPPED")
                    num_invalid += 1
                    continue

                if qty < 0 or price < 0:
                    logger.error(f"Row {row_number}: negative qty or price "
                                 f"({qty}, {price}) - SKIPPED")
                    num_invalid += 1
                    continue

                row["qty"] = qty
                row["price"] = price
                row["total"] = round(qty * price, 2)
                valid_rows.append(row)
                num_valid += 1
                logger.info(f"Row {row_number}: order {row['order_id']} processed successfully")

    except FileNotFoundError:
        logger.critical(f"Input file not found: {csv_path}")
        return (0, 0)

    finally:
        logger.info("Finished reading input CSV")

    with open(json_path, "w") as f:
        json.dump(valid_rows, f, indent=2)

    return (num_valid, num_invalid)


print(process_orders("orders.csv", "orders_clean.json", "orders_pipeline.log"))
# expected: (2, 2)

print("\n--- orders_clean.json ---")
with open("orders_clean.json") as f:
    print(f.read())

print("\n--- orders_pipeline.log ---")
with open("orders_pipeline.log") as f:
    print(f.read())
