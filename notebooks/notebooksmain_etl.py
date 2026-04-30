dbutils.widgets.text("group_id", "")
group_id = dbutils.widgets.get("group_id")

print(f"Running for {group_id}")

header_df = spark.sql(f"""
SELECT * FROM control_header
WHERE group_id = '{group_id}' AND is_active = 'Y'
""")

if header_df.count() == 0:
    raise Exception("Invalid GROUP_ID")

detail_df = spark.sql(f"""
SELECT * FROM l0_detail
WHERE group_id = '{group_id}' AND is_active = 'Y'
""")

row = detail_df.collect()[0]

source_path = row["source_path"]
file_format = row["file_format"]
target_table = row["target_table"]
write_mode = row["write_mode"]

if file_format == "json":
    df = spark.read.json(source_path)
else:
    raise Exception("Unsupported format")

df.write.format("delta") \
  .mode(write_mode) \
  .saveAsTable(target_table)

print("ETL Completed")