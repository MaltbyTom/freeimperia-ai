import json
from collections import defaultdict

def merge_jsonl_graphs(file_paths, output_path):
    edge_set = set()
    merged_records = []
    node_labels = defaultdict(set)

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line.strip())
                edge_key = (record["source"], record["relation"], record["target"])

                if edge_key not in edge_set:
                    edge_set.add(edge_key)
                    merged_records.append(record)

    with open(output_path, "w", encoding="utf-8") as f_out:
        for record in merged_records:
            f_out.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Merged graph written to: {output_path}")