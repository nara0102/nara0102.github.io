from pathlib import Path

import yaml

source = Path("_data/cv.yml")
target = Path("_data/cv_rendercv.yml")
data = yaml.safe_load(source.read_text(encoding="utf-8"))
cv = data["cv"]
cv["headline"] = cv.pop("label", "")
address = cv.pop("address", {})
cv["location"] = ", ".join(
    value for value in (address.get("street"), address.get("city"), address.get("region")) if value
)
cv.pop("summary", None)
target.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
